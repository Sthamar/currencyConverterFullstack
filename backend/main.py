from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet_user():
    return {"message":"Hello amar"}