from fastapi import FastAPI

app = FastAPI(title="ARPI v3.1")

@app.get("/")
def root():
    return {"status": "ARPI running"}
