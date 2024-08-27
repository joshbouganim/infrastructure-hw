import os
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

# Define the base directory dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

index_file_path = os.path.join(BASE_DIR, "static/index.html")

@app.get("/", response_class=HTMLResponse)
async def get_messages():
    return FileResponse(index_file_path)