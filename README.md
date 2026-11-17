# 🚀 Complete GenAI Series | Generative AI Projects & Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![LangGraph](https://img.shields.io/badge/LangGraph-AI%20Workflows-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Applications-red?logo=streamlit)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?logo=jupyter)
![GitHub](https://img.shields.io/badge/Status-Active-brightgreen)

A hands-on **Generative AI learning and development repository** containing practical implementations of Large Language Models (LLMs), LangChain, LangGraph, AI Agents, Prompt Engineering, Retrieval-Augmented Generation (RAG), Vector Databases, and intelligent chatbot applications.

This repository documents my journey of learning and building real-world Generative AI applications using Python and modern AI frameworks.

---

## 📌 About the Project

The **Complete GenAI Series** is a collection of Python applications and Jupyter notebooks covering important concepts in Generative AI.

It includes practical experiments with different LLM providers, conversational AI, prompt engineering, structured outputs, memory management, document processing, vector embeddings, RAG pipelines, and AI agents.

The main objective is to understand how modern AI applications work and develop practical skills by building projects.

## ✨ Key Topics Covered

- Generative AI and Large Language Models (LLMs)
- LangChain Fundamentals
- Prompt Engineering and Prompt Templates
- LLM Chains and Sequential Workflows
- Chatbots and Conversational AI
- Conversation Memory
- Structured Output with Pydantic
- Google AI and OpenAI Integrations
- Groq and Ollama Integrations
- AI Agents and Tool Calling
- Wikipedia and Google Search Integration
- Retrieval-Augmented Generation (RAG)
- Document Loading and Text Splitting
- Vector Embeddings and Vector Databases
- LangGraph and AI Agent Workflows
- Multi-Agent AI Applications
- SQL Database Agents

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| AI Frameworks | LangChain, LangGraph |
| LLM Providers | OpenAI, Google AI, Groq, Ollama |
| Application Framework | Streamlit |
| Vector Database | Chroma, FAISS (where configured) |
| Database | SQLite, SQL |
| Data Validation | Pydantic |
| Document Processing | PyPDF, BeautifulSoup |
| Development Tools | VS Code, Jupyter Notebook, Git, GitHub |

## 📂 Project Structure

```text
Complete-Gen-Ai-Project/
│
├── apps/
│   ├── doc_files/
│   ├── 1_qna_bot.py
│   ├── 2_google_agent.py
│   ├── 3_qna_fast_bot.py
│   ├── 4_sql_agent.py
│   ├── 5_RAG_agent.py
│   ├── 6_langgraph_qna_bot.py
│   ├── my_task.db
│   └── my_tasks.db
│
├── Data/
│   ├── RAG Documents
│   ├── Data Science Resources
│   ├── Medical Report Resources
│   ├── speech.txt
│   ├── sql_prompt.txt
│   └── Other Learning Resources
│
├── notebooks/
│   ├── 1_basic_langchain_with_openai.ipynb
│   ├── 2_prompt_chains.ipynb
│   ├── 3_basic_memory_with_langchain.ipynb
│   ├── 4_structured_output.ipynb
│   ├── 5_ollama_app.ipynb
│   ├── 6_groq_langchain.ipynb
│   ├── 7_streaming_response.ipynb
│   ├── 8_basic_agents.ipynb
│   ├── 9_google_search_agent.ipynb
│   ├── 10_RAG_load_docs.ipynb
│   ├── 11_RAG_splitter.ipynb
│   ├── 12_vector_embedding.ipynb
│   ├── 13_RAG_base_pdf_qna_bot.ipynb
│   ├── 14_RAG_Ai_agent.ipynb
│   ├── 15_pydantic_Data_validation.ipynb
│   ├── 16_langgraph.ipynb
│   ├── 17_chatbot.ipynb
│   ├── 18_multi_ai_agent.ipynb
│   ├── 19_RAG_with_graph.ipynb
│   └── vector.db/
│
├── .gitignore
├── .env.example
├── requirements.txt
└── README.md
```

## 📚 Applications

### 1. Question Answering Bot
- Build an AI-powered question-answering chatbot.
- Generate responses using an LLM.
- Explore conversational AI functionality.

### 2. Google AI Agent
- Explore Google AI integration.
- Build an intelligent AI agent.
- Experiment with agent-based workflows.

### 3. Fast Q&A Bot
- Develop a fast question-answering application.
- Experiment with efficient LLM-based responses.

### 4. SQL Agent
- Connect AI applications with SQL databases.
- Explore natural-language database interaction.
- Generate database queries using AI.

### 5. RAG Agent
- Implement Retrieval-Augmented Generation.
- Retrieve relevant information from external documents.
- Generate context-aware responses.

### 6. LangGraph Q&A Bot
- Explore LangGraph-based AI workflows.
- Build structured conversational applications.
- Experiment with stateful AI interactions.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later (check individual package compatibility).
- Git
- VS Code or Jupyter Notebook
- API keys for the LLM providers used in individual projects.

### Step 1: Clone the Repository

```bash
git clone https://github.com/alok745/Complete-Gen-Ai-Project.git
```

### Step 2: Navigate to the Project

```bash
cd Complete-Gen-Ai-Project
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure API Keys

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

Add only the keys required by the application you want to run.

**Security:** Never upload your `.env` file or expose API keys publicly.

## ▶️ Running Applications

Navigate to the project root and run the required application.

```bash
python apps/1_qna_bot.py
```

```bash
python apps/2_google_agent.py
```

```bash
python apps/3_qna_fast_bot.py
```

```bash
python apps/4_sql_agent.py
```

```bash
python apps/5_RAG_agent.py
```

```bash
python apps/6_langgraph_qna_bot.py
```

For Jupyter notebooks:

```bash
jupyter notebook
```

Open the `notebooks/` directory and select the notebook you want to explore.

## 🎯 Learning Objectives

Through this repository, I am focusing on:

1. Understanding the fundamentals of Generative AI.
2. Working with different Large Language Models.
3. Building applications using LangChain.
4. Implementing prompt engineering techniques.
5. Developing AI agents and tool-calling workflows.
6. Understanding document processing and embeddings.
7. Building RAG-based question-answering systems.
8. Exploring vector databases and semantic search.
9. Developing stateful workflows using LangGraph.
10. Building practical AI-powered applications.

## 🔮 Future Enhancements

- Develop advanced multi-agent systems.
- Build more RAG-based applications.
- Integrate additional LLM providers.
- Develop interactive Streamlit interfaces.
- Explore advanced LangGraph workflows.
- Implement production-ready AI applications.
- Deploy selected GenAI projects.

## 👨‍💻 About Me

**Alok Kumar Gupta**

B.Tech in Computer Science | 2026 Graduate

Passionate about Software Development, Generative AI, and building intelligent applications.

**Technical Interests:**
- Generative AI & Large Language Models
- AI Agents & Agentic AI
- LangChain & LangGraph
- Retrieval-Augmented Generation (RAG)
- Python Development
- MERN Stack Development
- SQL 

### Connect With Me

- LinkedIn: linkedin.com/in/alok-kumar-gupta-427860359

---

## ⭐ Support

If you find this repository helpful, please consider giving it a ⭐.

Feel free to explore, fork, and learn from the projects.

**Learning by Building | Exploring Generative AI | Building the Future with AI**

Made with ❤️ by Alok Kumar Gupta.
