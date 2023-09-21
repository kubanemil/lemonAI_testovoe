from fastapi import FastAPI
from main import FuncOptimizer
from typing import List, Tuple
from pydantic import BaseModel
import numpy as np


app = FastAPI(docs_url='/')


class DataInput(BaseModel):
    data: List[Tuple[float, float]]


@app.post("/abc/")
async def optimize_params(data_input: DataInput):
    """
    Введите массив А для того чтобы получить оптимальные значения для a, b, c
    Примерный вводный массив:
    {
        "data": [
         [0, 8],
         [1, 8],
         [2, 8],
         [3, 8],
         [4, 8],
         [5, -2],
         [6, -2],
         [7, -2],
         [8, -2],
         [9, -2]
         ]
    }
    """
    try:
        data = np.array(data_input.data)
        print(data)
        print("!!")
        opt = FuncOptimizer(data)
        a, b, c = opt.a, opt.b, opt.c
        return {"a": a, "b": b, "c": c}
    except Exception as e:
        return {'error': str(e)}
