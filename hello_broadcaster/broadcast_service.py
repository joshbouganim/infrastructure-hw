import asyncio
import random
from typing import List
import requests
from fastapi import FastAPI, Body
import datetime

app = FastAPI()

registered_receivers: List[str] = []

async def broadcast_message():
    while True:
        await asyncio.sleep(random.randint(1, 10))
        print(f"{datetime.datetime.now().time()} -- Sending broadcasts to {len(registered_receivers)} receivers")
        for receiver in registered_receivers:
            try:
                requests.post(f"{receiver}/receive", json={"message": "Hello world"})
            except Exception as e:
                print(f"Failed to send broadcast to {receiver}: {e}")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(broadcast_message())

@app.get("/")
async def root():
    return {"status": "Broadcasting", "subscribers": registered_receivers}

@app.post("/register")
async def register_receiver(receiver_url: str = Body(..., embed=True)):
    if receiver_url not in registered_receivers:
        registered_receivers.append(receiver_url)
        return {"status": "Registered", "receiver_url": receiver_url}
    return {"status": "Already registered", "receiver_url": receiver_url}
