from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_messages():
    return FileResponse("static/index.html")