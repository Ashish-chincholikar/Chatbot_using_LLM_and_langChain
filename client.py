import requests
import streamlit as st
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from main import context
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.vectorstores import FAISS



def get_answer_from_api(question, context_value):
    response = requests.post(
        "http://localhost:8000/QA/invoke",
        json={
            'input': {
                'question': question,
                'context_value': context_value
            }
        }
    )
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('output', 'No answer provided.')
    else:
        return f"Error: {response.status_code} - {response.text}"


def main():
    st.title("LangChain QA System")
    st.write("Ask a question based on a provided context.")

    context_value = context()
    question = st.text_input("Question", placeholder="Enter your question here...")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(context_value)
    
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=os.getenv("OPENAI_API_KEY"))
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    #docs = new_db.similarity_search(question)
    
    if st.button("Get Answer"):
        if context_value and question:
            with st.spinner("Getting answer..."):
                answer = get_answer_from_api(question, context_value)
                st.success(f"Answer: {answer}")
        else:
            st.warning("Please provide both context and question!")

if __name__ == "__main__":
    main()
