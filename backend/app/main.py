from fastapi import FastAPI

app = FastAPI(
    title="Smart Weather Assistant API",
    version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Weather Assistant API",
        "status": "running"
    }