from PyPDF2 import PdfReader
from docx import Document
import os 
from dotenv import load_dotenv


# Environment Variable to Acess OPENAI API KEY
# good practise not to hard code API keys
load_dotenv()
os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# creating a corpus form the pdf files
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    #print("this is get_pdf_text",end=" ")
    #print(type(text))

    return text

# creating a corpus form the word files
def get_docx_text(docx_docs):
    text = ""
    for doc in docx_docs:
        doc_reader = Document(doc)
        for paragraph in doc_reader.paragraphs:
            text += paragraph.text + "\n"
    return text

def context():
    pdf_paths = [
       "C:/Assignment/Training Data/India A Comprehensive Overview.pdf",
        "C:/Assignment/Training Data/India's Diverse States and Territories.pdf"
    ]
    docx_paths = [
       "C:/Assignment/Training Data/India's Education, Healthcare, and Social Development.docx",
        "C:/Assignment/Training Data/India's Natural Beauty and Wildlife.docx"
    ]
    
    raw_text = ""
    # for the pdf_paths and docx_paths we call the get_pdf_text and get_doc_text fuctions and store it
    # in raw_text , the raw text contains the corpus of the file text data
    if pdf_paths:
        raw_text += get_pdf_text(pdf_paths)
    if docx_paths:
        raw_text += get_docx_text(docx_paths)

    return raw_text