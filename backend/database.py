from model import Todo
# mongodb driver 
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.TodoList
collection = database.todo



# functions 

# ---------fetcha todo by id

# title from model, model set from get
async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return(document)


# ---------fetcha all todos

async def fetch_all_todos():
    todos =[]
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    
    return(todos)

# ---------create todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    
    return(document)

# ---------update todos

async def update_todo(title, desc):
    await collection.update_one({"title":title},{"$set":{"description":desc}} )
    document = await collection.find_one({"title":title})
    return(document)


# -----------remove todo

async def remove_todo(title):
    await collection.delete_one({'title':title})
    return True