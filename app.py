
import math
from calculator import power


while True:
    print("\n=== Scientific Calculator ===")
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
