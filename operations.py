
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed!")
        return a / b
    except Exception as e:
        return str(e)

def power(a, b):
    return a ** b

def modulus(a, b):
    try:
        if b == 0:
            raise ValueError("Error: Modulus by zero is not allowed!")
        return a % b
    except Exception as e:
        return str(e) 

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Error: Square root of a negative number is undefined!")
        return a ** 0.5
    except Exception as e:
        return str(e)