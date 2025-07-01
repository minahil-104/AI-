#Q:13 Sum of First N Natural Numbers

def calculate_sum(n):
    return n * (n + 1) // 2 

# Taking input from user
n = int(input("Enter a positive integer (n): "))

# input
if n > 0:
    total = calculate_sum(n)
    print("The sum of the first natural numbers is:", n ,total)
else:
    print("Please enter a number greater than 0.")
