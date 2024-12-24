from fastapi import FastAPI, Path, HTTPException, status, Body
from typing import Annotated
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()


class User(BaseModel):
    id: int = Field(ge=1, le=100, description='Enter user ID')
    username: str = Field(min_length=5, max_length=20, description='Enter username')
    age: int = Field(ge=18, le=120, description='Enter age from 18 to 120')


users: List[User] = []


@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age from 18 to 120')]) -> User:
    new_id = len(users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter user ID')],
                      user: User) -> User:
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = user.username
            edit_user.age = user.age
            return edit_user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter user ID')]) -> User:
    try:
        del_user = users.pop(user_id - 1)
        return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
