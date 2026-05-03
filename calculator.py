# Square root feature added

import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return a / b

    def square_root(self, x):
        return math.sqrt(x)


if __name__ == "__main__":
    c = Calculator()
    print("Add:", c.add(10, 5))
    print("Subtract:", c.subtract(10, 5))
    print("Multiply:", c.multiply(10, 5))
    print("Divide:", c.divide(10, 5))
    print("Square Root:", c.square_root(25))


