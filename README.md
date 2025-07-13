# 🧠 Prompt Quality Evaluator (Hindi + English)

This project is a terminal-based tool that evaluates and compares two AI-generated responses (A vs B) for the same prompt. It records which response is better, your reasoning, and quality scores — and saves everything to a structured CSV file.

> 🎯 Inspired by real-world LLM evaluation tasks like those at **Welocalize**, **Scale AI**, **Remotasks**, etc.

---

## 🌟 Features

- Supports both Hindi and English prompts
- Compares two AI-generated responses (A and B)
- Collects feedback: preference, reason, helpfulness, correctness, tone, safety
- Saves each entry immediately to a CSV file
- Works fully offline using [Ollama](https://ollama.com)

---

## 📦 Requirements

- Python 3.8 or higher
- [Ollama](https://ollama.com) installed locally
- Model pulled locally (e.g. `llama3`)

Install Python dependencies:

```bash
pip install ollama pandas
```
## 🚀 How to Run

## ✅ Step 1: Clone the repository

```bash
git clone https://github.com/Sourabsb/prompt-quality-evaluator
cd prompt-quality-evaluator
```
## ✅ Step 2: Install Python dependencies

```bash
pip install ollama pandas
```
## ✅ Step 3: Pull the model using Ollama

```bash
ollama pull llama3
```

## ✅ Step 4: Run the evaluator script

```bash
python evaluator.py
```
## ✅ Step 5: Enter prompts and evaluate
Follow the prompts in the terminal:

📝 Enter a user prompt (Hindi or English)

🅰️ View Response A and Response B

✅ Choose the better one (A or B)

💬 Give your reason for the choice

📊 Rate the responses:

Helpfulness (1–5)

Correctness (1–5)

Tone (1–5)

Any unsafe/biased content (Yes/No)

## ✅ Step 6: View the saved dataset
```bash
ollama_prompt_evaluation_dataset.csv
```

## 📂 Project Structure

prompt-quality-evaluator/

├── evaluator.py # Main evaluator script

├── ollama_prompt_evaluation_dataset.csv # Output CSV (auto-generated)

├── README.md # Project documentation

## 🛡 Disclaimer
This tool is built for educational and research purposes only. The responses and evaluations are generated using local models and are not intended to be used in production without human review.


## 🙌 Acknowledgements

- Thanks to the open-source community for inspiration on LLM evaluation tasks.
- Powered by [Ollama](https://ollama.com) for local large language model access.
- Built using [Python](https://python.org) and [Pandas](https://pandas.pydata.org/) for scripting and data handling.
- Prompt evaluation logic inspired by common practices in instruction tuning, response ranking, and alignment testing.
