from fastapi import FastAPI

app = FastAPI(
    title="Mail Sending and Management API",
    description="API for sending emails and managing clients.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"status": "ok"}
