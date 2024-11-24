from shapes import *

def main():
    while True:
        try:
            shape = input("Enter shape (rectangle, circle, triangle): ").lower()

            if shape == 'rectangle':
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                print(f"Area of rectangle: {area_of_rectangle(width, height)}")
                
            elif shape == 'circle':
                radius = float(input("Enter radius: "))
                print(f"Area of circle: {area_of_circle(radius)}")
                
            elif shape == 'triangle':
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print(f"Area of triangle: {area_of_triangle(base, height)}")
                
            else:
                print("Unknown shape")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()