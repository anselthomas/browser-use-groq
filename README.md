# 📌 browser-use-groq

A fork of browser-use that runs on Groq Cloud-supported models (mainly Llama models) for free and efficient inference with browser-use.

---

## 🚀 Features

- Runs on **Groq Cloud**, providing **free and efficient LLM access**.
- Uses **Llama-3.3-70B** by default but supports other **Groq-compatible models**.
- Simplifies running browser-use with **free cloud-based inference**.

---

## 🛠️ Prerequisites

Ensure you have:

- **Python 3.11** or newer installed. Check your version with:

  ```sh
  python --version
  ```

- A **free Groq Cloud account**:

  1. Go to [Groq Cloud](https://groq.com)
  2. **Sign up** for a free account
  3. **Generate an API Key**
  4. **Save the API Key** and bring it here

---

## 🔧 Setup & Installation

Follow these steps to set up and run `browser-use-groq` locally.

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/anselthomas/browser-use-groq.git
cd browser-use-groq
```

### 2️⃣ Create a Python Virtual Environment

```sh
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

#### Windows (PowerShell)
```sh
venv\Scripts\activate
```

#### Mac/Linux
```sh
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 5️⃣ Set Up the Groq API Key

#### Windows (PowerShell)
```sh
$env:GROQ_API_KEY="your-groq-api-key-here"
```

#### Mac/Linux
```sh
export GROQ_API_KEY="your-groq-api-key-here"
```

---

## 🎯 Running the Script

To run the program with a task, use:

```sh
python TestGroq.py "Find the latest stock price of Tesla and return the percentage change in the last 24 hours"
```

### Example Queries:

```sh
python TestGroq.py "Check the current weather in New York and summarize the forecast for the next 3 days"
python TestGroq.py "Find the latest stock price of Apple and return the percentage change in the last 24 hours"
python TestGroq.py "Search for the top three programming languages in 2025 and summarize why they are popular"
```

---

## 🔄 Changing the LLM Model

By default, the script uses **Llama-3.3-70B**, but you can switch to **any Groq-supported model**.

### Supported Models on Groq Cloud

- `llama-3.3-70b-versatile`
- `llama-3.3-8b`
- `mixtral-8x7b`
- Other models as available on **Groq Cloud**.

### How to Change the Model

"Modify the TestGroq.py script and update the model parameter to your preferred LLM:

```python
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
```

To use a different model, change the **model parameter**:

```python
llm = ChatGroq(model="mixtral-8x7b", api_key=os.getenv("GROQ_API_KEY"))
```

---

## 📜 License

This project is licensed under the **MIT License**.  
It is a **modified version of browser_use**, integrating **Groq’s LLM API** for enhanced automation with free cloud inference for LLMs.

See the **LICENSE** file for more details.

---

## 🔗 References

- **[Groq API Docs](https://groq.com/docs)**
- **Original browser_use Repository: [GitHub](https://github.com/browser-use/browser-use/)**

---



