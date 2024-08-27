import asyncio
import datetime
import random
from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# Create the FastAPI instance
app = FastAPI()

connected_clients: List[WebSocket] = []


async def broadcast_message():
    """
    Asynchronously broadcasts a "Hello world" message to all connected WebSocket clients
    at random intervals between 1 and 10 seconds.

    The message includes the current time when it was sent.
    """
    while True:
        await asyncio.sleep(random.randint(1, 10))
        time_now = datetime.datetime.now().time()
        message = f"{time_now} Hello world"
        print(f"{time_now} -- Sending broadcasts to {len(connected_clients)} receivers")

        # Send the message to all connected WebSocket clients
        for client in connected_clients:
            try:
                await client.send_text(message)
            except Exception as e:
                print(f"Failed to send message to WebSocket client: {e}")


@app.on_event("startup")
async def startup_event():
    """
    Event handler for the FastAPI application startup event.

    This function creates a background task to continuously broadcast messages
    to connected WebSocket clients.
    """
    asyncio.create_task(broadcast_message())


@app.get("/")
async def root():
    """
    HTTP GET endpoint that returns the status of the broadcaster and the IP addresses
    of currently connected WebSocket clients.

    Returns:
        dict: A dictionary containing the status of the service and a list of connected client IP addresses.
    """
    client_ips = [client.client.host for client in connected_clients]
    return {"status": "Broadcasting", "subscribers": client_ips}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint that handles new connections, receives messages, and manages
    disconnections.

    Args:
        websocket (WebSocket): The WebSocket connection object.

    This function adds the WebSocket connection to the list of connected clients and
    keeps the connection open to receive messages. If the connection is closed, the
    WebSocket is removed from the list of connected clients.
    """
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep the connection open
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
