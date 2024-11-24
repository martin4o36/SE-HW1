from shapes import *

def main():
    width = 2.5
    height = 10
    ppprint(f"Area of rectangle: {area_of_rectangle(width, height)}");

    radius = 7
    print(f"Area of circle: {area_of_circle(radius)}")

    base = 2.335
    triangle_height = 2
    print(f"Area of triangle: {area_of_triangle(base, triangle_height)}")

if __name__ == "__main__":
    main()