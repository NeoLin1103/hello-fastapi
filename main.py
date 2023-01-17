from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# @app.get('/home')
# def home():
#     return HTMLResponse(content="<h1>Hello World!<h1>", status_code=200)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

if __name__ == '__main__':
    port = 8080
    uvicorn.run(app, port=port, host='0.0.0.0')