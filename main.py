from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# Temporary array for testing
my_posts = [{"title": "post title 1", "content": "content of post 1", "id": 1}, {"title":
"post title 2", "content": "content of post 2", "id": 2}]

# Function to retrieve post (temporary)
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"message": "Hello World"}

# FastAPI serializes automatically!
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

'''
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"post": f"title {payload['title']} content: {payload['content']}"}
'''

'''
@app.post("/createposts")
def create_posts(post: Post):
    print(post.rating)
    return {"data": "new post"}
'''



# convert pydantic model to dict
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

'''
@app.post("/createposts")
def create_posts(post: Post):
    print(post.rating)
    return {"data": "new post"}
'''

# embed url with path parameter - {id}
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}