from importlib.resources import contents
from typing import Optional
from fastapi.params import Body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "contents of post 1", "id": 1}, {"title": 
"Favourites Programming language", "contents": "Python & Javascript", "id": 2}] #Array



@app.get("/")
def root():
    return {"message": "welcome to my api🔥"}

@app.get("/posts")
def  get_posts():
     return {"data": my_posts}
        

# working with post methods

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

# PYDANTIC basemodel
# title str, content str
@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print("post.dict()")
    return {"data": post}


    