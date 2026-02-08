from fastapi import FastAPI, HTTPException, Form

app = FastAPI()

@app.post("/chat")
async def chat( 
    query:str = Form(...)
) : return {
    
    "answer":query
}