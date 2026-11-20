from fastapi import FastAPI, HTTPException

app = FastAPI(title="User Service", version="1.0")

# Mock database for users
users_db = {
    1: {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob Jones", "email": "bob@example.com"},
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
  if user_id not in users_db:
    raise HTTPException(status_code=404, detail="User not found")
  return users_db[user_id]