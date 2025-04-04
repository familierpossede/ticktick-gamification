from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# Enable CORS for ChatGPT plugin access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve ai-plugin.json from .well-known path
@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
async def serve_ai_plugin():
    return FileResponse(".well-known/ai-plugin.json")

# Serve OpenAPI schema
@app.get("/openapi.yaml", include_in_schema=False)
async def serve_openapi():
    return FileResponse("openapi.yaml")
