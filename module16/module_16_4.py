from fastapi import FastAPI, Path, HTTPException, status, Body
from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def add_user(user: User) -> str:
    user.id = len(users) + 1
    users.append(user)
    return f"User {users[-1]} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, description='Enter user ID')],
                      user=Body()):
    try:
        edit_user = users[user_id - 1]
        edit_user.username = user['username']
        edit_user.age = user['age']
        return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description='Enter user ID')]) -> str:
    try:
        users.pop(user_id-1)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")