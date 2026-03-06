
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


import math
from calculator import power


while True:
    print("\nScientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Log")
    print("4. Power")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = float(input("Enter number: "))
        print("Result:", math.sqrt(x))

    elif choice == 2:
        x = int(input("Enter number: "))
        print("Result:", math.factorial(x))

    elif choice == 3:
        x = float(input("Enter number: "))
        print("Result:", math.log(x))

    elif choice == 4:
        x = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result:", power(x, b))

    elif choice == 5:
        break