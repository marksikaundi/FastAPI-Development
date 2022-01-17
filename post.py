from importlib.resources import contents
from typing import Optional
from fastapi.params import Body
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

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
        
# PYDANTIC basemodel
# title str, content str
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}


    