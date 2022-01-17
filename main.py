from importlib.resources import contents
from fastapi.params import Body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True



@app.get("/")
def root():
    return {"message": "welcome to my api🔥"}

@app.get("/posts")
def  get_posts():
     return {"data:" "this is your post"}
        

# working with post methods

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

# PYDANTIC basemodel
# title str, content str
@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.published)
    return {"data": "new post"}


    