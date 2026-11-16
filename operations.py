"""
operations.py - Mathematical operations module for the calculator app.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers with division-by-zero error handling."""
    try:
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed!")
        return a / b
    except Exception as e:
        return str(e)  