#Question:2 Area of Rectangle Calculator

def calculate_area(length, width):
    area = length * width
    return area

# Taking input from user
length = int (input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area
area = calculate_area(length, width)
print("The area of the rectangle is square units." , area)
