# Q:5 Average of Three Numbers

def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculating average
average = calculate_average(num1, num2, num3)

# Displaying the result
print("The average of the three numbers is:", average)
