from transformers import AutoModelForQuestionAnswering, Trainer, TrainingArguments, AutoTokenizer
from datasets import load_dataset

# Load the model and tokenizer
model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the dataset
data = load_dataset('json', data_files={'train': 'train_data4.json', 'validation': 'val_data4.json'})

# Preprocessing function
def preprocess_function(examples):
    questions = [q.strip() for q in examples["question"]]
    inputs = tokenizer(
        questions, 
        examples["context"], 
        max_length=384, 
        truncation="only_second", 
        padding="max_length", 
        return_offsets_mapping=True  # For calculating token positions
    )
    
    start_positions = []
    end_positions = []

    for i, offsets in enumerate(inputs["offset_mapping"]):
        answer = examples["answers"][i]
        start_char = answer["answer_start"][0] if answer["answer_start"] else 0
        end_char = start_char + len(answer["text"][0]) if answer["text"] else 0

        # Map character positions to token positions
        start_token = next((idx for idx, (s, e) in enumerate(offsets) if s <= start_char < e), 0)
        end_token = next((idx for idx, (s, e) in enumerate(offsets) if s < end_char <= e), 0)

        start_positions.append(start_token)
        end_positions.append(end_token)

    inputs["start_positions"] = start_positions
    inputs["end_positions"] = end_positions
    del inputs["offset_mapping"]  # No need to keep this

    return inputs

# Apply preprocessing function to the dataset
tokenized_data = data.map(preprocess_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",                
    evaluation_strategy="epoch",           
    learning_rate=2e-5,                    
    per_device_train_batch_size=8,         
    per_device_eval_batch_size=8,          
    num_train_epochs=3,                    
    weight_decay=0.01,                     
    logging_dir='./logs',                  
    logging_steps=10,                      
    save_total_limit=2,                    
    save_strategy="epoch",                 
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data["train"],
    eval_dataset=tokenized_data["validation"],
    tokenizer=tokenizer
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./fine_tuned_model6")
tokenizer.save_pretrained("./fine_tuned_model6")

print("Model fine-tuning complete. Saved in './fine_tuned_model6'")
