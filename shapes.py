import math

def area_of_rectangle(width, height):
    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return width * height

def area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

def area_of_triangle(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height


# Failng test on purpose
def test_area_of_circle_invalid_radius():
    assert area_of_circle(-3) == 28.274333882308138