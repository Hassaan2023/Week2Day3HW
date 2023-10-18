# Area of a house

def Sqft(length, width):
    area = length * width
    return area

def user_input():
    length = float(input("Enter the length of the house in feet: "))
    width = float(input("Enter the width of the house in feet: "))
    return length, width

def main():
    print("Welcome to the Area of a House Calculator!")
    length, width = user_input()
    square_footage = Sqft(length, width)
    print(f"The square footage of the house is {square_footage} square feet.")

if __name__ == "__main__":
    main()

# circumference of a circle 

import math

def calCir(radius):
    circumference = 2 * math.pi * radius
    return circumference

def calCir(diameter):
    radius = diameter / 2
    circumference = 2 * math.pi * radius
    return circumference

# Get user input for radius or diameter
choice = input("Calculate circumference by (R)adius or (D)iameter: ").strip().lower()

if choice == 'r':
    radius = float(input("Enter the radius of the circle: "))
    circumference = calCir(radius)
    print(f"The circumference of the circle is approximately {circumference:.2f} units.")
elif choice == 'd':
    diameter = float(input("Enter the diameter of the circle: "))
    circumference = calCir(diameter)
    print(f"The circumference of the circle is approximately {circumference:.2f} units.")
else:
    print("Invalid choice. Please select 'R' for radius or 'D' for diameter.")