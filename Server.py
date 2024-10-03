from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain.llms import OpenAI
import uvicorn
import os
from dotenv import load_dotenv
from main import get_pdf_text , get_docx_text , context

load_dotenv()

os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

model = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY")) 
context_value = context()
#print(context)

prompt1 = ChatPromptTemplate.from_template(""" Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context_value:\n {context_value}?\n
    Question: \n{question}\n
    Answer:""")

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

add_routes(
    app,
    prompt1|model,
    path="/QA"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)


















