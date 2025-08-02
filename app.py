import streamlit as st
from pdf_reader import extract_text_from_pdf
from embed_and_search import get_most_relevant_chunk, initialize_faiss
from llm_answer import generate_answer

st.set_page_config(page_title="StudyMate", layout="wide")
st.title("📘 StudyMate – Ask Questions from Your PDF Study Material")

pdf = st.file_uploader("Upload a PDF", type=["pdf"])

if pdf:
    st.success("PDF uploaded successfully!")
    with st.spinner("Extracting text..."):
        content_chunks = extract_text_from_pdf(pdf)

    with st.spinner("Generating embeddings and initializing search..."):
        index, chunk_list = initialize_faiss(content_chunks)

    question = st.text_input("Ask a question based on the PDF:")

    if st.button("Get Answer"):
        with st.spinner("Searching and generating response..."):
            best_chunk = get_most_relevant_chunk(question, index, chunk_list)
            answer = generate_answer(question, best_chunk)
            st.markdown(f"### 🤖 Answer:\n{answer}")
            st.markdown(f"**📖 Source Context:**\n\n{best_chunk}")
