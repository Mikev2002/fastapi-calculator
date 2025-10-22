from fastapi import FastAPI, HTTPException
from operations import add, subtract, multiply, divide
import logging

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator"}

@app.get("/add")
def calculate_add(a: float, b: float):
    result = add(a, b)
    logging.info(f"Add: {a} + {b} = {result}")
    return {"result": result}

@app.get("/subtract")
def calculate_subtract(a: float, b: float):
    result = subtract(a, b)
    logging.info(f"Subtract: {a} - {b} = {result}")
    return {"result": result}

@app.get("/multiply")
def calculate_multiply(a: float, b: float):
    result = multiply(a, b)
    logging.info(f"Multiply: {a} * {b} = {result}")
    return {"result": result}

@app.get("/divide")
def calculate_divide(a: float, b: float):
    try:
        result = divide(a, b)
        logging.info(f"Divide: {a} / {b} = {result}")
        return {"result": result}
    except ValueError as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
