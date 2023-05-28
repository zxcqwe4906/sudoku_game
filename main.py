from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.generate_sudoku import parse_sudoku


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
def main(request: Request, generate: Optional[bool] = False):
    board = parse_sudoku() if generate else []
    return templates.TemplateResponse(
        "sudoku.html",
        {
            "request": request,
            "board": board
        },
    )