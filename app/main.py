from fastapi import FastAPI, Request
from pydantic import BaseModel
from gpt4all import GPT4All
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import urllib.parse
from app.grok_engine import grok_response


app = FastAPI()

# Mount static files for UI
app.mount("/static", StaticFiles(directory="app"), name="static")

# Load the local Grok model
model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

# Pydantic model for JSON body
class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Grok 4 DevOps is running"}

# Serve the chat UI
@app.get("/chat-ui")
async def get_chat_ui():
    return FileResponse("app/chat.html")

# API endpoint for HTML chat and Swagger
@app.post("/chat")
async def chat_with_grok(request: PromptRequest):
    return {"response": grok_response(request.prompt)}

# Optional: Raw GPT model (can also use grok_response here)
@app.post("/ask")
def ask_grok(request: PromptRequest):
    response = model.generate(prompt=request.prompt, max_tokens=200)
    return {"response": response}

# Slack-compatible webhook endpoint
@app.post("/slack/ask")
async def slack_ask(request: Request):
    form_data = await request.body()
    parsed = urllib.parse.parse_qs(form_data.decode())

    user_question = parsed.get("text", [""])[0]
    response = grok_response(user_question)

    return PlainTextResponse(response)
