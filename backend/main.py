from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # lets fastapi talk to react



# APP project 
app = FastAPI()


from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)

from model import Todo

# Allow permission between origins Python/react

origins = ['https://localhost:3000'] # this list used below

app.add_middleware(
    CORSMiddleware,
    allow_origins     = origins,
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)



@app.get('/')
def read_root():
    return({"Hello":"Adam!"})


# ----------ROUTES

# Each root calls a DB function
# Each root uses the TODO class we defined as response model


# -------GET ALL TODOS

@app.get('/api/todo')
async def get_todo():
    response = await fetch_all_todos()
    return(response)

# -------GET BY ID

# response_model=Todo this is the Todo class

@app.get('/api/todo{title}', response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if(response):
        return(response)
    raise HTTPException(404, "There is no todo item with the Title: {}".format(title))

# -------POST

@app.post('/api/todo', response_model=Todo)
async def post_todo(todo:Todo): 
    response = await create_todo(todo.dict())
    if(response):
        return(response)
    raise HTTPException(400, "Something went wrong / Bad request")

# -------PUT

@app.put('/api/todo{title}/', response_model=Todo)
async def put_todo(title:str, desc:str):
    response = await update_todo(title,desc)
    if(response):
        return(response)
    raise HTTPException(404, "There is no todo item with the Title: {}".format(title))

# -------DELETE

@app.delete('/api/todo{title}')
async def delete_todo(title):
    response = await remove_todo(title)
    if(response):
        return('Successfully deleted todo item!')
    raise HTTPException("404 there is no todo item with this title {}".format(title))