# fastAPI converts data to JSON format for you.
from fastapi import Body, FastAPI
from pydantic import BaseModel  #schema stuff

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/") # decorator
async def root(): # functional, async for asynchronous task handling.
    return {"message": "Hello boink"}

@app.get("/posts")
def fuckoff():
    return {"oj":"nomnom"}

@app.post("/createpost")
def create_post(new_post: Post): # fastApi will validate data received from front-end has title and content
    print(new_post.title)
    return {"data": "new post"}
#title str, content str  