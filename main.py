from fastapi import FastAPI

app = FastAPI(title="Bale Multi Userbot Backend")


@app.get("/")
def root():
    return {"status": "ok", "message": "backend is running"}


@app.get("/status")
def status():
    return {
        "online_accounts": [],
        "version": "0.1"
    }
