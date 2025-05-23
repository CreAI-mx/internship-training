from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from src.routers.movie_router import movie_router
import datetime


app = FastAPI()


@app.get("/", tags=["Movies"])

def home():
    return PlainTextResponse(content ="Home", status_code=200)

app.include_router(prefix= "/movies", router=movie_router)

