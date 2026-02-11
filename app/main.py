from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.parent

app = FastAPI(title="PDF Recovery Web Framework")

# Serve frontend at root
app.mount("/", StaticFiles(directory=BASE_DIR / "frontend", html=True), name="frontend")

# Load profiles
PROFILES_FILE = BASE_DIR / "config" / "profiles.json"
with open(PROFILES_FILE) as f:
    profiles_data = json.load(f)

@app.get("/profiles")
def get_profiles():
    return profiles_data

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Just return filename & dummy hash for now
    content = await file.read()
    hash_preview = hash(content)  # Simple Python hash for demo
    return JSONResponse({"filename": file.filename, "hash_preview": str(hash_preview)})
