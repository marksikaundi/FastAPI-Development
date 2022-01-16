from fastapi.params import Body
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to my api🔥"}

@app.get("/posts")
def  get_posts():
     return {"data:" "this is your post"}
        
# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"feed:" "post sent well"}

# working with post methods

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": f"title: {payload['title']} content: {payload['content']}"}


    