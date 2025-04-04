from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
import httpx

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve ChatGPT plugin manifest + OpenAPI spec
@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
async def serve_ai_plugin():
    return FileResponse(".well-known/ai-plugin.json")

@app.get("/openapi.yaml", include_in_schema=False)
async def serve_openapi():
    return FileResponse("openapi.yaml")

# ✅ Proxy TickTick OAuth
@app.get("/oauth/authorize")
async def proxy_authorize(request: Request):
    ticktick_url = "https://ticktick.com/oauth/authorize"
    params = str(request.query_params)
    return RedirectResponse(f"{ticktick_url}?{params}")

@app.post("/oauth/token")
async def proxy_token(request: Request):
    async with httpx.AsyncClient() as client:
        body = await request.body()
        headers = dict(request.headers)
        response = await client.post("https://ticktick.com/oauth/token", headers=headers, content=body)
        return response.json()
