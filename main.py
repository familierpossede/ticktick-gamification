from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import httpx

app = FastAPI()

# Allow CORS (required for ChatGPT plugins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
async def serve_ai_plugin():
    return FileResponse(".well-known/ai-plugin.json")

@app.get("/openapi.yaml", include_in_schema=False)
async def serve_openapi():
    return FileResponse("openapi.yaml")

@app.get("/oauth/authorize")
async def proxy_authorize(request: Request):
    params = request.query_params
    async with httpx.AsyncClient() as client:
        response = await client.get("https://ticktick.com/oauth/authorize", params=params)
    return Response(content=response.content, status_code=response.status_code, media_type=response.headers.get("content-type"))

@app.post("/oauth/token")
async def proxy_token(request: Request):
    data = await request.body()
    headers = {"Content-Type": request.headers.get("content-type")}
    async with httpx.AsyncClient() as client:
        response = await client.post("https://ticktick.com/oauth/token", content=data, headers=headers)
    return Response(content=response.content, status_code=response.status_code, media_type=response.headers.get("content-type"))
