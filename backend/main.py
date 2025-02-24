from fastapi import FastAPI
# from chatbot import get_response
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chatbot import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Titanic Chatbot Backend is Running"}

@app.get("/query/")
def query(question: str):
    response = get_response(question)
    return {"answer": response}
