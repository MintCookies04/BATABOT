<!-- HEADER -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:2d0057,100:6a00f4&height=200&section=header&text=BATABOT&fontSize=62&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=AI-Powered%20Log%20File%20Question%20Answering%20System&descColor=d4aaff&descSize=15&descAlignY=60" width="100%"/>
</div>

<!-- TYPING ANIMATION -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=2500&pause=800&color=A855F7&center=true&vCenter=true&width=700&lines=🤖+Ask+Questions+About+Your+Log+Files;🧠+Fine-Tuned+RoBERTa+for+Log+Intelligence;📋+Upload+CSV+Logs+%E2%86%92+Get+Instant+Answers;🌐+Interactive+Gradio+Web+Interface" />
</p>

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/RoBERTa-Fine--Tuned-A855F7?style=for-the-badge&logo=huggingface&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradio-Web_Interface-FF6B35?style=for-the-badge&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-Powered-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Model-RoBERTa_QA-a855f7?style=flat-square" />
  <img src="https://img.shields.io/badge/Input-CSV_Log_Files-7c3aed?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" />
</p>

---

## 📖 Overview

**BATABOT** is an intelligent question-answering system for log file analysis. Upload a CSV log file, ask natural language questions about the events it contains, and get accurate, targeted answers — powered by a fine-tuned **RoBERTa** model trained specifically on log data. No API keys. No cloud dependency. All inference runs locally.

---

## ⚡ Features

- 🤖 **Natural Language Q&A** — Ask questions like *"What happened on 2024-01-15?"* or *"Show all events from the Auth component"*
- 🧠 **Fine-Tuned RoBERTa** — Question-answering model fine-tuned on log event data for accurate, context-aware responses
- 📋 **CSV Log Ingestion** — Upload any CSV log file directly through the web interface
- 💬 **Chat History** — Multi-turn conversation with full session history tracking
- 🌐 **Gradio Interface** — Clean browser-based UI — no CLI knowledge required
- ⚡ **Local Inference** — Runs entirely on your machine; no data leaves your environment
- 🔧 **Fine-Tuning Pipeline** — Includes training scripts to retrain the model on your own log data

---

## 🛠️ Tech Stack

<p>
  <img src="https://skillicons.dev/icons?i=python,pytorch&theme=dark" />
  &nbsp;
  <img src="https://img.shields.io/badge/HuggingFace_Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black" height="48"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Gradio-Web_UI-FF6B35?style=flat-square&logoColor=white" height="48"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Pandas-Data_Processing-150458?style=flat-square&logo=pandas&logoColor=white" height="48"/>
</p>

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/MintCookies04/BATABOT.git
cd BATABOT

# Install dependencies
pip install transformers gradio pandas datasets torch
```

---

## 💻 Usage

### Running the Application

```bash
python ui5.py
```

Open the Gradio interface in your browser, then:

1. **Upload** a CSV log file
2. **Ask** a natural language question about the log data
3. **Read** the answer and continue the conversation

**Example questions:**

```
"What happened on [date]?"
"Show me all events from [component name]"
"What was the error message for Event ID [number]?"
"Were there any critical events in the last hour?"
```

### CSV Log Format

BATABOT expects CSV files with the following columns:

| Column | Description |
|---|---|
| `Date` | Event date |
| `Time` | Event time |
| `Component` | System component that generated the event |
| `Content` | Event message / description |
| `EventId` | Unique event identifier |

---

## 🔧 Model Training

To fine-tune BATABOT on your own log data:

**Step 1 — Prepare training data** in JSON format (`train_data4.json`, `val_data4.json`)

**Step 2 — Run the fine-tuning script:**
```bash
python tune_script3.py
```

The fine-tuned model is saved to `fine_tuned_model6/` and used automatically by `ui5.py`.

---

## 📁 Project Structure

```
BATABOT/
├── ui5.py                     # Gradio web interface & main app
├── tune_script3.py            # RoBERTa fine-tuning script
├── train_data4.json           # Training dataset
├── val_data4.json             # Validation dataset
├── fine_tuned_model6/         # Fine-tuned model weights (post-training)
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

<!-- FOOTER -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6a00f4,50:2d0057,100:0d1117&height=100&section=footer" width="100%"/>
  <sub>Local AI for log intelligence — no cloud, no keys · <a href="https://github.com/MintCookies04">MintCookies04</a></sub>
</div>
