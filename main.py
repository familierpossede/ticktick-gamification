
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TICKTICK_API = "https://api.ticktick.com/open/v1/task"
TICKTICK_TOKEN_URL = "https://ticktick.com/oauth/token"
CLIENT_ID = os.getenv("TICKTICK_CLIENT_ID")
CLIENT_SECRET = os.getenv("TICKTICK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("TICKTICK_REDIRECT_URI")

@app.get("/tasks/today")
async def get_today_tasks(request: Request):
    token = request.headers.get("Authorization")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TICKTICK_API}", headers={"Authorization": token})
        tasks = response.json()
    today_tasks = [t for t in tasks if t.get("dueDate") and not t.get("status") == 2]
    return JSONResponse(content=today_tasks)

@app.get("/tasks/habits")
async def get_habit_tasks(request: Request):
    token = request.headers.get("Authorization")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TICKTICK_API}", headers={"Authorization": token})
        tasks = response.json()
    recurring_tasks = [t for t in tasks if t.get("repeatFlag") and not t.get("status") == 2]
    return JSONResponse(content=recurring_tasks)

@app.post("/oauth/callback")
async def oauth_callback(request: Request):
    body = await request.json()
    code = body.get("code")
    async with httpx.AsyncClient() as client:
        response = await client.post(TICKTICK_TOKEN_URL, data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI
        })
    return JSONResponse(content=response.json())
