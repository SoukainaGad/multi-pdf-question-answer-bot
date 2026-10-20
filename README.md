
# 📚 Multi-PDF Question Answering Bot

### Retrieval-Augmented Generation (RAG) with Llama-3.3-70B, Groq, LangChain and ChromaDB

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload multiple PDF documents and ask natural-language questions about their contents.

Built with **Python**, **Streamlit**, **LangChain**, **Hugging Face embeddings**, **ChromaDB**, and **Llama-3.3-70B via Groq**, the application retrieves relevant document passages and uses them to generate context-aware answers.

---

## 🚀 Overview

The application allows users to:

1. Upload multiple PDF documents.
2. Extract and process their text.
3. Split the extracted content into smaller, overlapping chunks.
4. Generate embeddings and store them in a vector database.
5. Ask questions across the uploaded documents.
6. Retrieve relevant passages and generate answers using an LLM.

Rather than passing entire documents to the language model, the application uses semantic search to retrieve relevant information for each question.

---

## 🧠 Key Features

- **Multi-PDF support:** Upload and query multiple PDF documents.
- **Document processing:** Extract text and divide it into manageable chunks.
- **Semantic embeddings:** Convert document passages into vector representations using Hugging Face models.
- **Vector storage:** Store document embeddings locally using ChromaDB.
- **Semantic retrieval:** Identify relevant passages based on similarity to the user's question.
- **LLM integration:** Generate answers using Llama-3.3-70B through the Groq API.
- **Interactive interface:** Upload documents and ask questions through Streamlit.

---

## 🏗️ RAG Architecture

The application follows a retrieval-augmented generation workflow consisting of document ingestion, indexing, retrieval and answer generation.

### Document Processing Pipeline

```text
PDF Documents
      |
      v
Text Extraction
      |
      v
Text Chunking
      |
      v
Hugging Face Embeddings
      |
      v
ChromaDB Vector Store
```

### Question Answering Pipeline

```text
User Question
      |
      v
Query Embedding
      |
      v
Similarity Search (ChromaDB)
      |
      v
Relevant Document Chunks
      |
      v
Question + Retrieved Context
      |
      v
Llama-3.3-70B (Groq API)
      |
      v
Generated Answer
```

---

## ⚙️ How It Works

### 1. Document Ingestion

Users upload one or more PDF documents through the Streamlit interface. The application extracts text from the uploaded files.

### 2. Text Chunking

The extracted text is split into smaller, overlapping chunks to make retrieval more manageable and preserve contextual information.

### 3. Embedding Generation

The document chunks are converted into numerical vector representations using a Hugging Face sentence-transformer model.

### 4. Vector Storage

The generated embeddings are stored in ChromaDB, enabling semantic similarity searches across the uploaded documents.

### 5. Context Retrieval

When a user submits a question, the application searches the vector database for relevant document passages.

### 6. Answer Generation

The retrieved passages and the user's question are passed to Llama-3.3-70B through the Groq API to generate a context-aware response.

---

## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/SoukainaGad/multi-pdf-rag.git
cd multi-pdf-rag
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the environment.

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

If the repository includes an `.env.example` file, you can copy it and rename it to `.env`.

**Security:** Never commit your actual API key or `.env` file to GitHub. Ensure `.env` is included in `.gitignore`.

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, typically:

```text
http://localhost:8501
```

Upload your PDF documents, process them and start asking questions.

---

## 📁 Project Structure

```text
multi-pdf-rag/
│
├── app.py                  # Streamlit user interface
├── rag_utility.py          # PDF processing and RAG logic
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── README.md               # Project documentation
│
├── data/                   # Optional directory for PDF files
│
└── multi_doc_vectorstore/  # ChromaDB vector storage
```

---

## 🧰 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| User Interface | Streamlit |
| RAG Framework | LangChain |
| Embedding Models | Hugging Face Sentence Transformers |
| Vector Database | ChromaDB |
| Large Language Model | Llama-3.3-70B |
| LLM Inference | Groq API |
| PDF Processing | Unstructured |

---

## 💡 Example Use Cases

This application demonstrates how RAG can support document-based question answering in scenarios such as:

- **Research:** Exploring information across multiple research papers.
- **Technical documentation:** Finding relevant information in software documentation.
- **Legal research:** Retrieving relevant passages from legal and regulatory documents.
- **Business documents:** Querying reports, policies and internal documentation.
- **Education:** Asking questions across textbooks and study materials.

These are potential applications rather than independently validated production use cases.

---

## ⚠️ Limitations

Like other RAG-based systems, this application has several limitations:

- **Retrieval quality:** Relevant passages may be missed during similarity search.
- **Answer accuracy:** The language model may generate inaccurate or unsupported statements.
- **PDF complexity:** Scanned documents, tables and complex layouts may affect text extraction.
- **Context limitations:** Generated answers depend on the information retrieved and supplied to the model.
- **Evaluation:** Retrieval relevance, answer completeness and factual accuracy require systematic testing.

Generated answers should be verified against the original documents when accuracy is important.

---

## 🔮 Potential Improvements

Future development could explore:

- **Hybrid search:** Combine keyword-based and semantic retrieval.
- **Reranking:** Improve retrieval relevance by reordering candidate passages.
- **Source citations:** Link generated answers to supporting document passages.
- **RAG evaluation:** Measure retrieval relevance, answer faithfulness and completeness.
- **Metadata filtering:** Restrict retrieval to specific documents or categories.
- **Improved PDF processing:** Support complex layouts, tables and scanned documents.
- **Logging and monitoring:** Improve observability and error handling.

These are potential enhancements rather than confirmed features of the current implementation.

---

## 📌 Project Purpose

This project demonstrates the implementation of an end-to-end **Retrieval-Augmented Generation (RAG) pipeline**, combining document ingestion, text processing, semantic embeddings, vector retrieval and large language model inference.

It provides a foundation for exploring document question-answering systems and improving retrieval quality, answer grounding and evaluation.

---

## 👩‍💻 Author

**Soukaina Gadir**

GitHub: [SoukainaGad](https://github.com/SoukainaGad)

---

## 📄 Licence

No licence has been specified for this project. Refer to the repository for any applicable licensing terms.
