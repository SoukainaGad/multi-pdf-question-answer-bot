````markdown
# 📚 Multi-PDF Question Answering Bot — Powered by Llama-3.3-70B (Groq)

An intelligent **RAG (Retrieval-Augmented Generation)** app that lets you **upload multiple PDFs** and ask natural-language questions across all of them.  
Built with **Streamlit**, **LangChain**, **Chroma**, and **Groq’s Llama-3.3-70B** model.

---

## 🚀 Demo

> Upload multiple PDFs → Process them → Ask any question → Get AI-powered answers instantly!

---

## 🧠 Features

- 📂 Upload and analyze multiple PDFs at once  
- 🧩 Automatic text chunking and embedding  
- ⚡ Query all documents simultaneously using RAG  
- 🧠 Powered by **Llama-3.3-70B (Groq)** for fast, high-quality responses  
- 💾 Local vector storage via **ChromaDB**

---

## 🛠️ Installation

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-pdf-rag.git
cd multi-pdf-rag
````

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the root folder and add your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

(You can copy `.env.example` and rename it to `.env`.)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at **[http://localhost:8501](http://localhost:8501)**

---

## 📁 Project Structure

```
multi-pdf-rag/
├── app.py                  # Streamlit user interface
├── rag_utility.py          # Core RAG logic
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
├── README.md               # Documentation
├── data/                   # Optional folder for uploaded PDFs
└── multi_doc_vectorstore/  # ChromaDB persistence (auto-created)
```

---

## 🧩 How It Works

1. **Upload PDFs** → Each document is read and parsed.
2. **Chunking & Embedding** → Text is split into chunks and converted into embeddings.
3. **Storage** → All embeddings are saved in a local **Chroma vector store**.
4. **Question Answering** → When you ask a question, relevant chunks are retrieved and the **Llama-3.3-70B** model generates a context-aware answer.

---

## 🧰 Tech Stack

| Component       | Library / Service                   |
| --------------- | ----------------------------------- |
| Frontend UI     | Streamlit                           |
| Vector Database | Chroma                              |
| Embeddings      | Sentence Transformers (HuggingFace) |
| LLM             | Llama-3.3-70B (Groq)                |
| RAG Framework   | LangChain                           |
| PDF Parsing     | Unstructured                        |


