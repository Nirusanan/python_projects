from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root_route(req: Request):
    data = {
        'request': req,
        'title': 'My Page Title',
        'heading': 'My Page Heading',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return templates.TemplateResponse("renderPage.html", data)

if __name__ == "__main__":
    uvicorn.run("render:app")
