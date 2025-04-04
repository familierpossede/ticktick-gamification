from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
