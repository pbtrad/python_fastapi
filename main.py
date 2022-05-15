from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

'''
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"post": f"title {payload['title']} content: {payload['content']}"}
'''

@app.post("/createposts")
def create_posts(post: Post):
    print(post.rating)
    return {"data": "new post"}


'''
# convert pydantic model to dict
@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": "post"}
'''