from fastapi import FastAPI, HTTPException, Form

from llm_ollama import call_llm

app = FastAPI()

@app.post("/chat")
async def chat( 
    query:str = Form(...)
) : return {

    "answer":call_llm(query)
}