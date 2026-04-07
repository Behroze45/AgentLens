# 🚀 AgentLens

AgentLens is a Python-based recommendation agent that suggests the **top 5 open-source large language models (LLMs)** for a given user task.

It combines **DuckDuckGo web search** for up-to-date context with a **locally running Ollama model** to generate structured recommendations. The results are displayed in a clean table format in the terminal.

---

## ✨ Features

* Retrieves recent context using DuckDuckGo search
* Uses a local Ollama model for recommendations
* Returns the top 5 matching LLMs
* Displays results in formatted terminal tables
* Includes a final ranked best-choice section
* Uses strict JSON output for consistent parsing
* Managed with UV for dependency and environment management

---

## 🧰 Requirements

* Python 3.11+
* UV
* Ollama

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd AgentLens
```

Install dependencies:

```bash
uv sync
```

---

## 📦 Dependencies

This project uses the following Python packages:

* `openai`
* `langchain-community`
* `duckduckgo-search`
* `tabulate`

To add them manually:

```bash
uv add openai langchain-community duckduckgo-search tabulate
```

---

## 🛠️ Configuration

Create a `config.py` file in the project root:

```python
OLLMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "qwen2.5:3b"
```

---

## 🤖 Ollama Setup

Pull the required model:

```bash
ollama pull qwen2.5:3b
```

Start the Ollama server:

```bash
ollama serve
```

---

## ▶️ Usage

Run the application:

```bash
uv run main.py
```

Example query:

```text
Best LLM for coding on 8GB RAM laptop
```

---

## 📁 Project Structure

```bash
AgentLens/
│── .venv/
│── main.py
│── config.py
│── pyproject.toml
│── uv.lock
│── README.md
```

---

## 🧠 How It Works

1. The user enters a task or requirement.
2. DuckDuckGo search retrieves recent related information.
3. The query and web context are sent to the local Ollama model.
4. The model returns a strict JSON response.
5. The JSON is parsed and displayed as formatted tables.

---

## 🖥️ Example Output

The application displays:

* rank
* model name
* parameter size
* best use case
* system requirements
* reason for recommendation
* final best-choice ranking

---

## ⚖️ License

This project is available under the MIT License.

---

## 👨‍💻 Author

Behroze
