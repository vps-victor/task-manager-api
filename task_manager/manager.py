from fastapi import FastAPI

TASKS = []

app = FastAPI()

@app.get("/task")
def listar():
    return TASKS