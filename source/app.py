from fastapi import FastAPI, HTTPException

from source.schema import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/', status_code=201, response_model=UserPublic)
def create_user1(user: UserSchema):
    return user


database = []  # provisório para estudo!


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user2(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def get_users():
    return {'users': database}


@app.put('/users/{user_id}')
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id
