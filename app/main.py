"""RESTful API for our calculators.

This is using FastAPI.
"""
from calculon import calculator
from fastapi import FastAPI

app = FastAPI()


@app.get("/calculate_prefix/{expression}")
def calculate_prefix(expression: str):
    # strip spaces on each end
    expression = expression.strip()
    result = calculator.calculate_prefix(expression)
    return {'result': result}


@app.get("/calculate_infix/{expression}")
def calculate_infix(expression: str):
    # strip spaces on each end
    expression = expression.strip()
    result = calculator.calculate_infix(expression)
    return {'result': result}
