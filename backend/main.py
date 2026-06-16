from fastapi import FastAPI
from .auth import router as auth_router

app = FastAPI()

# Include authentication routes
app.include_router(auth_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to ORIVION API"}

@app.get("/health")
async def health():
    return {"status": "ok"}

# Additional endpoints and agent orchestration logic will be implemented here.
