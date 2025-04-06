from fastapi import FastAPI
from pydantic import BaseModel
from langchain.llms import OpenAI

app = FastAPI(title="LangChain Chatbot")

llm = OpenAI(temperature=0.7)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = llm(request.prompt)
    return {"response": response}
