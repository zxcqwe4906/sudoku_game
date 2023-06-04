from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.generate_sudoku import parse_sudoku
from utils.solve import board_str_to_board, solve_sudoku


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

@app.get('/solve')
def solve(request: Request, board_str: str):
    # board_str
    new_board = board_str_to_board(board_str)
    solved_board = solve_sudoku(new_board)
    return templates.TemplateResponse(
        "sudoku.html",
        {
            "request": request,
            "board": solved_board
        },
    )