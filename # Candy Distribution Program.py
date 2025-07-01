#Q:7 Candy Distribution Program

def distribute_candies(n, k):
    each_student = n // k
    remaining = n % k
    return each_student, remaining

# Taking input from user
n = int(input("Enter total number of candies: "))
k = int(input("Enter number of students: "))

# Avoid division by zero
if k == 0:
    print("Number of students cannot be zero.")
else:
    per_student, leftover = distribute_candies(n, k)
    print("Each student gets candies.",per_student)
    print("Candies left:" ,leftover)
