import os
import streamlit as st
from rag_utility import process_documents_to_chroma_db, answer_question_multi

# Set working directory
working_dir = os.path.dirname(os.path.abspath((__file__)))

st.title("📚 Multi-Document RAG by Soukaina - Powered by Llama-3.3-70B (Groq)")

# File uploader (allow multiple PDFs)
uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    file_names = []
    for file in uploaded_files:
        save_path = os.path.join(working_dir, file.name)
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())
        file_names.append(file.name)

    num_chunks = process_documents_to_chroma_db(file_names)
    st.success(f"✅ Processed {len(file_names)} PDFs into {num_chunks} text chunks!")

# Text area for user question
user_question = st.text_area("Ask a question across your uploaded documents")

if st.button("Get Answer"):
    with st.spinner("Querying the documents..."):
        answer = answer_question_multi(user_question)
    st.markdown("### 🧠 Llama-3.3-70B Answer")
    st.write(answer)
