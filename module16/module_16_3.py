from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
        age: Annotated[int, Path(ge=14, le=120, description='Enter age')]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {users[current_index]} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, description='Enter user ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=14, le=120, description='Enter age')]):
    for k in users:
        if user_id == int(k):
            users[user_id] = f'Имя: {username}, возраст: {age}'
            return f'The user {user_id} is updated'
    raise HTTPException(status_code=404, detail="Не удалость обновить значение")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description='Enter user ID')]) -> str:
    for k in users:
        if user_id == int(k):
            users.pop(str(user_id))
            return f'User {user_id} has been deleted'
    raise HTTPException(status_code=404, detail="Не удалось удалить объект")
