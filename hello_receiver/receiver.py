from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import requests
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

received_messages = []

BROADCASTER_URL = os.getenv("BROADCASTER_URL", "http://localhost:8000")

@app.post("/receive")
async def receive_message(request: Request):
    data = await request.json()
    received_messages.append(data["message"])
    return {"status": "Received"}

@app.get("/", response_class=HTMLResponse)
async def get_messages(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "messages": received_messages})

@app.post("/register", response_class=RedirectResponse)
async def register_endpoint(receiver_url: str = Form(...)):
    try:
        response = requests.post(f"{BROADCASTER_URL}/register", json={"receiver_url": receiver_url})
        print(response.json())
    except Exception as e:
        print(f"Failed to register with broadcaster: {e}")
    return RedirectResponse("/", status_code=303)
