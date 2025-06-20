# utils.py
import re

def calculator(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == 'x': return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operator")

def validate_password(pwd):
    return (len(pwd) >= 8 and
            re.search(r"[A-Z]", pwd) and
            re.search(r"[a-z]", pwd) and
            re.search(r"[0-9]", pwd) and
            re.search(r"[!@#$%^&*()]", pwd))
