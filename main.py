from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

comments_list = [
    {'Name':'Alex','Comment':'你好', 'id':1},
    {'Name':'Ben','Comment':'你好不好', 'id':2},
    {'Name':'Claire','Comment':'肯定非常好', 'id':3}
]

# @app.get('/home')
# def home():
#     return HTMLResponse(content="<h1>Hello World!<h1>", status_code=200)

@app.get("/comments")
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request, 'comments_list': comments_list})

@app.get("/comments/{id}")
def home(request: Request, id:int):
    comment_dict = list(filter(lambda item: item['id'] == id, comments_list))[0]
    return templates.TemplateResponse("show.html",{"request": request, 'comment_dict': comment_dict})

if __name__ == '__main__':
    port = 8080
    uvicorn.run(app, port=port, host='0.0.0.0')