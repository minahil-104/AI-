# Question:4 Perimeter of Rectangle

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# Taking input from user
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Calculating perimeter
perimeter = calculate_perimeter(length, width)

# Displaying result
print("The perimeter of the rectangle is:", perimeter)
