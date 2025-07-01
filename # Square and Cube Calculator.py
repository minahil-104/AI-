# Q:6 Square and Cube Calculator

def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Taking input from user
num = int(input("Enter a number: "))

# Calculating square and cube
square, cube = square_and_cube(num)

# Displaying results
print("The square of is:",num,square )
print("The square of is:", num, square)
print("The cube of is:",num, cube)
