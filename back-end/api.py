from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def index():
    return {"message": "This is a home route"}