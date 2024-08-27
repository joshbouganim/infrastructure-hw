import asyncio
import random
from typing import List
import requests
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import datetime

app = FastAPI()

connected_clients: List[WebSocket] = []

async def broadcast_message():
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
    asyncio.create_task(broadcast_message())

@app.get("/")
async def root():
    client_ips = [client.client.host for client in connected_clients]
    return {"status": "Broadcasting", "subscribers": client_ips}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep the connection open
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
