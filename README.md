# BATA BOT - Log Analysis Question Answering System

## Overview
BATA BOT is an intelligent question-answering system designed to analyze log files and provide answers to questions about log events. The system uses a fine-tuned RoBERTa model to understand and answer questions about log data presented in CSV format.

## Features
- Upload and process CSV log files
- Interactive question-answering interface
- Chat history tracking
- Fine-tuned model for accurate log analysis
- Support for temporal and component-based queries

## Prerequisites
- Python 3.7+
- Required Python packages:
  - transformers
  - gradio
  - pandas
  - datasets
  - torch

## Installation
1. Clone this repository
2. Install the required packages:
```bash
pip install transformers gradio pandas datasets torch
```

## Project Structure
- `ui5.py`: Main application interface using Gradio
- `tune_script3.py`: Script for fine-tuning the question-answering model
- `train_data4.json`: Training dataset for model fine-tuning
- `val_data4.json`: Validation dataset for model fine-tuning
- `fine_tuned_model6/`: Directory containing the fine-tuned model (generated after training)

## Usage

### Running the Application
1. Start the application:
```bash
python ui5.py
```
2. Open the provided Gradio interface in your web browser
3. Upload a CSV file containing log data
4. Ask questions about the log data in natural language

### CSV File Format
The system expects CSV files with the following columns:
- Date
- Time
- Component
- Content
- EventId

### Example Questions
- "What happened on [specific date]?"
- "Show me all events from [component name]"
- "What was the error message for Event ID [number]?"

## Model Training
To fine-tune the model with your own data:
1. Prepare your training and validation datasets in JSON format
2. Run the training script:
```bash
python tune_script3.py
```
The fine-tuned model will be saved in the `fine_tuned_model6` directory.

## Documentation
- `i22-1732_1590_1723_1633_UserGuide.docx`: Detailed user guide
- `i22-1732_1590_1723_1633_Report.docx`: Project report and documentation


## Acknowledgments
- Based on the RoBERTa model from Hugging Face
- Uses Gradio for the web interface 