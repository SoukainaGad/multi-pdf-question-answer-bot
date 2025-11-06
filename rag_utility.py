import os
from dotenv import load_dotenv

from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA


# Load environment variables from .env file
load_dotenv()

working_dir = os.path.dirname(os.path.abspath((__file__)))

# Load the embedding model
embedding = HuggingFaceEmbeddings()

# Load the Llama-3.3-70B model from Groq
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def process_documents_to_chroma_db(file_names):
    """Process multiple PDFs and store all embeddings in one Chroma database"""
    all_texts = []

    for file_name in file_names:
        loader = UnstructuredPDFLoader(f"{working_dir}/{file_name}")
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        split_docs = text_splitter.split_documents(documents)
        all_texts.extend(split_docs)

    # Store all document chunks in one Chroma DB
    vectordb = Chroma.from_documents(
        documents=all_texts,
        embedding=embedding,
        persist_directory=f"{working_dir}/multi_doc_vectorstore"
    )
    vectordb.persist()
    return len(all_texts)


def answer_question_multi(user_question):
    """Answer a question across all stored documents"""
    vectordb = Chroma(
        persist_directory=f"{working_dir}/multi_doc_vectorstore",
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
