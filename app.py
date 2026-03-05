import logging
from flask import Flask, request
import math

logging.basicConfig(filename="calculator.log",level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def home():
    return "Scientific Calculator API Running"

@app.route("/add")
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a + b
    logging.info(f"Addition performed: {a} + {b} = {result}")
    return {"result": result}
    #return {"result": a + b}

@app.route("/sub")
def sub():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a - b
    logging.info(f"Subtraction performed: {a} - {b} = {result}")
    return {"result": result}

@app.route("/mul")
def mul():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a * b
    logging.info(f"Multiplication performed: {a} * {b} = {result}")
    return {"result": result}

@app.route("/div")
def div():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    if b == 0:
        logging.warning(f"Division by zero attempted: {a} / {b}")
        return {"error": "Division by zero is not allowed"}, 400
    result = a / b
    logging.info(f"Division performed: {a} / {b} = {result}")
    return {"result": result}
    #return {"result": a / b}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)