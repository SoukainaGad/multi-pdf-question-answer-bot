import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
VECTOR_DIR = os.path.join(WORKING_DIR, "vectorstore")

embedding = HuggingFaceEmbeddings()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

def process_documents_to_chroma_db(file_paths):
    """Process multiple PDFs and store embeddings in Chroma."""
    all_texts = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

    for path in file_paths:
        loader = PyPDFLoader(path)
        documents = loader.load()
        split_docs = text_splitter.split_documents(documents)
        all_texts.extend(split_docs)

    vectordb = Chroma.from_documents(
        documents=all_texts,
        embedding=embedding,
        persist_directory=VECTOR_DIR
    )
    vectordb.persist()
    return len(all_texts)

def answer_question_multi(user_question):
    """Answer a question across all stored PDFs."""
    vectordb = Chroma(
        persist_directory=VECTOR_DIR,
        embedding_function=embedding
    )
    retriever = vectordb.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
    )
    response = qa_chain.invoke({"query": user_question})
    return response["result"]
