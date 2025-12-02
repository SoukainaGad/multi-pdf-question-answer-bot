````markdown
# 📚 Multi-PDF Question Answering Bot — Powered by Llama-3.3-70B (Groq)

An intelligent **Retrieval-Augmented Generation (RAG)** application that lets you **upload multiple PDF documents** and ask natural-language questions across them.  
Built with **Streamlit**, **LangChain**, **Chroma**, and **Groq’s Llama-3.3-70B** model for lightning-fast, high-quality responses.

---

## 🚀 Demo

> Upload multiple PDFs → Process them → Ask your question → Get AI-powered answers instantly!

---

## 🧠 Key Features

- Upload and analyze **multiple PDFs at once**
- Automatic **text extraction, chunking, and embedding**
- Query **all uploaded documents simultaneously** using RAG
- Powered by **Llama-3.3-70B (Groq)** for fast, reliable answers
- Local vector storage with **ChromaDB** for reusability

---

## 🛠️ Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-pdf-rag.git
cd multi-pdf-rag
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root folder:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

*(You can copy `.env.example` and rename it to `.env`.)*

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧩 How It Works

1. **PDF Upload:** You upload one or more PDF files.
2. **Text Processing:** Each file is parsed and split into small overlapping text chunks.
3. **Embedding & Storage:** The text chunks are converted into embeddings and stored in **ChromaDB**.
4. **Question Answering:** Your question is embedded, matched with relevant chunks, and the **Llama-3.3-70B** model generates a detailed answer.

---

## 📁 Project Structure

```
multi-pdf-rag/
├── app.py                  # Streamlit frontend
├── rag_utility.py          # RAG logic (PDF loading, embedding, QA)
├── requirements.txt        # Project dependencies
├── .env.example            # Environment variable template
├── README.md               # Documentation
├── data/                   # Optional folder for uploaded PDFs
└── multi_doc_vectorstore/  # Chroma database (auto-created)
```

---

## 🧰 Tech Stack

| Category             | Tool / Library                    |
| -------------------- | --------------------------------- |
| UI Framework         | Streamlit                         |
| RAG Framework        | LangChain                         |
| Embeddings           | HuggingFace Sentence Transformers |
| Vector Database      | Chroma                            |
| Large Language Model | Llama-3.3-70B via Groq API        |
| PDF Processing       | Unstructured                      |



