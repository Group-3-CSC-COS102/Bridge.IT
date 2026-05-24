# Bridge.IT — AI Awareness App

Bridge.IT is an AI awareness and information system designed to help users understand Artificial Intelligence, explore AI tools, learn useful AI skills, and interact with an AI assistant.

---

## Prerequisites
- Python, installed on your system
- Internet connection (optional, only required for AI assistant features)

---

## 1) Install Python packages

Open **Command Prompt** (Windows) or **Terminal** (macOS/Linux).

Navigate to the app directory (the folder containing `main.py`) and run:

```bash
pip install -r requirements.txt
```
---

## 2) (Optional) Enable the AI Assistant Feature

To use the AI chatbot, you must provide a **Groq API key**.

### Step 1: Create a `.env` file

In the **same folder as `main.py`**, create a file named:

```text
.env
```

### Step 2: Add your API key

Inside the `.env` file, add:

```text
GROQ_API_KEY=your_groq_api_key_here
```

### Notes

- The chatbot uses the **Groq API** and requires a valid API key.
- You can get a key from the [Groq Console](https://console.groq.com/).
- Other API keys may not work with the app.
- If no API key is provided, offline features of the app will still function.

---

## 3) Run the Application

From the project directory, run:

```bash
python main.py
```

The GUI should open automatically.

After signing up or logging in, use the navigation tabs to explore:

- Basics of AI
- AI Tools  
- AI Skills
- AI Assistant

## Troubleshooting

### CSV Data Errors

Ensure the following files exist inside the `data/` folder:

```text
data/
├── lessons.csv
├── tools.csv
├── skills.csv
```

### Missing Packages

If a module error appears, run:

```bash
pip install -r requirements.txt
```

again.

---
