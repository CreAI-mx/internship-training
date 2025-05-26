from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import HTMLResponse, Response, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from fastapi.requests import Request
from pydantic import BaseModel, Field
from typing import Optional, List
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 

import os


app = FastAPI()

app.add_middleware(HTTPErrorHandler)

static_path = os.path.join(os.path.dirname(__file__), "static")
templates_path = os.path.join(os.path.dirname(__file__), "templates")


app.mount("/static", StaticFiles(directory=static_path), name="static")

templates = Jinja2Templates(directory=templates_path)


@app.middleware("http")
async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
    print("Middleware is running!")
    return await call_next(request)


@app.get("/", tags=["Movies"])

def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome"})

app.include_router(prefix= "/movies", router=movie_router)

#def common_params(start_date: str, end_date: str):
    #return{"start_date": start_date, "end_date": end_date}

#CommonDep = Annotated[dict, Depends(common_params)]

class CommonDep:
    def __init__(self, start_date: str, end_date:str) -> None:
        self.star_date = start_date
        self.end_date = end_date

        
    
@app.get("/users")
def get_users(commons: CommonDep):
    return f"Users created between{commons["start_date"]} and {commons["end_date"]}"

@app.get("/coustomers")
def get_users(commons: CommonDep):
    return f"Coustomers created between{commons["start_date"]} and {commons["end_date"]}"

