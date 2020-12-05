"""RESTful API for our calculators.

This is using FastAPI.
"""
from calculon import calculator
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Body(BaseModel):
    # expression to be computed
    expression: str

    @property
    def notation(self):
        # small clean up to prevent error if whitespace on each end
        return self.expression.strip()


@app.post("/calculate_prefix/")
def calculate_prefix(expression: Body):
    result = calculator.calculate_prefix(expression.notation)
    return {'result': result}


@app.post("/calculate_infix")
def calculate_infix(expression: Body):
    result = calculator.calculate_infix(expression.notation)
    return {'result': result}
