1. Business Problem
1.1. Business Objective:
The objective is to develop a question-answering system that can interact with PDF
and Word documents using OpenAI's API, providing detailed answers based on the content
of these documents. This tool is designed to help users quickly extract relevant 
information from large documents by asking specific questions.

1.2. Constraints:
> The system relies on the OpenAI API, which has a usage limit and cost associated with it.
> The quality of the answers depends on the context available in the documents and the 
efficiency of the text chunking and embedding processes.
> Users must upload valid PDF or Word documents, and the system's performance may vary 
based on document size and content complexity.

2. Work on Each Feature of the Dataset
2.1. Data Dictionary:
For this project, the dataset consists of text extracted from PDF and Word documents. 
While a traditional data dictionary is not applicable lets see an table.

3. Data Pre-processing
3.1. Data Cleaning, Feature Engineering, etc.:

Text Extraction: Text is extracted from PDF and Word documents.
Feature Engineering: Text chunks are created to ensure the context is maintained
and to handle large documents efficiently.

3.2. Outlier Treatment:
There’s no specific outlier treatment as the project deals with text data,
but text chunks are managed to maintain consistency and relevance.

4. Exploratory Data Analysis (EDA)
4.1. Summary:
The project involves extracting, chunking, and embedding text from documents for question-answering.
4.2. Univariate Analysis:
4.3. Bivariate Analysis:

5.	Model Building
The project involves creating a system that extracts text from PDF and Word documents, 
breaks it into manageable chunks, and converts these chunks into vector embeddings using
OpenAI's model. These embeddings are stored in a FAISS index, enabling efficient similarity
searches to retrieve relevant text based on user queries. A question-answering chain then
generates detailed answers using the retrieved text. Users interact with this system
through a Streamlit interface, allowing them to ask questions and receive precise answers
from the uploaded documents. The model's effectiveness hinges on the seamless integration 
of text processing, embedding, and retrieval components.

6. Benefits/Impact of the Solution
The business benefits from this solution by providing users with a powerful tool to 
extract relevant information from large and complex documents efficiently.
This saves time and enhances decision-making processes, especially in environments 
where quick access to specific information is crucial.