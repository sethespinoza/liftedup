from fastapi import FastAPI
from database import engine
from models import Base

# reads models and create tables in db
Base.metadata.create_all(bind=engine)


# app instance
# all requests from the server are handled through this object
app = FastAPI()

# route
# maps URL to a function
@app.get("/")
def home():
    return {"message": "LiftedUp API is running!"}

# dynamic route with path parameter

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "username": "s3th",
        "flat_bench_pr": 170,
        "hack_squat_pr": 185
    }