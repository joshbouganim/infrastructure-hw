import os

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

# Create the FastAPI instance
app = FastAPI()

# Define the base directory dynamically
# BASE_DIR refers to the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the index.html file in the static directory
index_file_path = os.path.join(BASE_DIR, "static/index.html")


@app.get("/")
async def get_messages():
    """
    HTTP GET endpoint that allows the user to register to a broadcaster.

    Returns:
        FileResponse: The HTML file that will be rendered in the browser.
    """
    return FileResponse(index_file_path)
