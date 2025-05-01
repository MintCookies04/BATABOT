import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import pandas as pd

# Define the path to your fine-tuned model
model_path = "./fine_tuned_model6"

# Load the fine-tuned tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForQuestionAnswering.from_pretrained(model_path)

# Set up the question-answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Initialize chat history
chat_history = []

# Function to process the CSV and create a narrative context
def parse_csv_to_context(file):
    try:
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Verify if required columns exist
        required_columns = ['Date', 'Time', 'Component', 'Content', 'EventId']
        for col in required_columns:
            if col not in df.columns:
                return f"Error: Missing required column '{col}' in the CSV file."
        
        # Build the context string
        context = []
        for _, row in df.iterrows():
            timestamp = f"On *{row['Date']}* at *{row['Time']}*"
            component = f"the **{row['Component']}** component"
            event_id = f"with Event ID **{row['EventId']}**"
            message = row['Content']
            context.append(f"{timestamp}, {component} {event_id} {message}.")
        
        # Join all context lines
        context_string = "\n".join(context)
        
        # Print the generated context to the terminal
        print("\n--- Generated Context ---")
        print(context_string)
        print("\n--- End of Context ---")
        
        return context_string
    except Exception as e:
        return f"Error processing CSV file: {str(e)}"

# Function to process user input and return the answer, with chat history support
def answer_question(csv_file, question):
    global chat_history  # Use the global chat history list
    
    try:
        # Parse the CSV file to create context
        context = parse_csv_to_context(csv_file.name)
        if context.startswith("Error"):
            return context, chat_history  # Return error if CSV processing failed
        
        # Run the QA pipeline
        result = qa_pipeline(question=question, context=context)
        answer = result['answer']
        
        # Update chat history with the question and answer
        chat_history.append((question, answer))
        
        return answer, chat_history
    except Exception as e:
        return f"Error: {str(e)}", chat_history

# Gradio interface
iface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.File(label="Upload CSV File"),
        gr.Textbox(label="Ask a Question", placeholder="Type your question here..."),
    ],
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Chatbot(label="Chat History")
    ],
    title="BATA BOT",
    description="Upload a CSV log file to generate context and ask questions based on the extracted information using a fine-tuned model.",
)

# Launch the Gradio interface
iface.launch(share=True)
