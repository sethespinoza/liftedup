from fastapi import FastAPI

# app instance
# all requests from the server are handled through this object
app = FastAPI()

# route
# maps URL to a function
@app.get("/")
def home():
    return {"message": "LiftedUp API is running!"}

# dynamic route with path parameter
# the {user_id} in the URL is a placeholder for a dynamic value
# the function get_user will receive the user_id as an argument
# when a request is made to /users/123, the get_user function will be called with user_id=123
# the function returns a JSON response with user details
# in a real application, you would fetch this data from a database instead of hardcoding it
# the response includes the user's id, username, and their personal records for flat bench and hack squat
#
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "username": "s3th",
        "flat_bench_pr": 170,
        "hack_squat_pr": 185
    }