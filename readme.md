
---

# **LangChain-based Question-Answering System**

## **Overview**

This project is a question-answering system that leverages LangChain, LangSmith, LangServe, and OpenAI’s API to process PDF and Word documents. It allows users to upload documents, ask questions, and receive detailed answers based on the content of those documents. The system is deployed using a FastAPI server and has a client interface built with Streamlit for easy interaction.

## **Key Features**
- **Document Processing**: Extracts text from PDF and Word documents to create a searchable corpus.
- **Question-Answering**: Users can ask questions based on the context of the uploaded documents, and the system provides detailed answers.
- **OpenAI Integration**: Uses OpenAI's `text-embedding-ada-002` model for creating embeddings and generating responses.
- **FAISS**: Stores and retrieves document chunks efficiently using FAISS for similarity search.
- **FastAPI**: The backend API is built using FastAPI and serves as the main interface for invoking the question-answering functionality.
- **LangChain and LangServe**: Manages prompt templates, embeddings, and serves the application via LangServe.

## **Technologies Used**
- **LangChain**: For managing and building language model chains to perform question-answering.
- **LangSmith**: For deploying and monitoring chains as web services.
- **LangServe**: To serve the API endpoints for question-answering functionality.
- **OpenAI API**: Used to embed text chunks and generate responses.
- **FAISS**: Provides fast vector searches for retrieving relevant text from document embeddings.
- **Streamlit**: A user-friendly interface for users to interact with the system by uploading documents and asking questions.
- **FastAPI**: Provides the backend API to interact with the LangChain and OpenAI models.

## **Project Structure**

```plaintext
|-- client.py           # Client-side Streamlit app to upload documents and ask questions
|-- server.py           # FastAPI server to handle API requests and serve the QA system
|-- main.py             # Core functions for extracting text from PDFs and Word documents
|-- .env                # Environment variables for storing API keys securely
```

## **How It Works**

1. **Text Extraction**: Text is extracted from uploaded PDF and Word documents using PyPDF2 and `python-docx` libraries.
2. **Text Chunking**: The extracted text is split into smaller, manageable chunks using LangChain's `RecursiveCharacterTextSplitter`.
3. **Embeddings Creation**: These text chunks are then converted into vector embeddings using OpenAI’s embedding model (`text-embedding-ada-002`).
4. **Storing in FAISS**: The embeddings are stored in FAISS for efficient similarity search and retrieval.
5. **Question Answering**: Users can ask questions in the Streamlit interface, and the system searches the FAISS index for relevant text to generate a detailed answer using OpenAI.
6. **Server**: The FastAPI server handles the question-answering process, using LangChain prompts and models to answer the user queries.
7. **Client Interaction**: The Streamlit app serves as the client-side interface, allowing users to upload documents, ask questions, and receive answers.

## **Setup Instructions**

### **Prerequisites**

- Python 3.9+
- OpenAI API Key
- LangServe and LangSmith accounts for deploying the chains
- Libraries: `langchain`, `langserve`, `openai`, `streamlit`, `fastapi`, `uvicorn`, `PyPDF2`, `python-docx`, `faiss-cpu`, `requests`, `dotenv`

## **Usage**

1. **Upload Documents**: Use the Streamlit interface to upload the relevant PDF and Word documents.
2. **Ask Questions**: After uploading the documents, enter a question based on the document’s context.
3. **Receive Answers**: The system will process the question and return a detailed answer based on the content of the uploaded documents.

## **API Endpoints**

- `/QA/invoke`: Handles the question-answering functionality using the provided context and question.
- `/openai`: Additional endpoint for future integration with other OpenAI models.

