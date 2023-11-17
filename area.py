import math

def circle(radius):
    try:
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        return math.pi * radius ** 2
    except ValueError as e:
        return str(e)

def square(side):
    try:
        if side <= 0:
            raise ValueError("Side length must be a positive number")
        return side ** 2
    except ValueError as e:
        return str(e)

def rectangle(length, width):
    try:
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        return length * width
    except ValueError as e:
        return str(e)

def triangle(base, height):
    try:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        return 0.5 * base * height
    except ValueError as e:
        return str(e)
