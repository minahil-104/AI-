#Questio:3 Compound Interest Calculator

def calculate_compound_interest(P, R, T):
    CI = P * (1 + R/100)**T - P
    return CI
# Taking input from user
principal = float(input("Enter the principal amount P:",))
rate = float(input("Enter the annual interest rate R in % :"))
time = float(input("Enter the time period in years T:"))
# Calculating compound interest
compound_interest = calculate_compound_interest(principal, rate, time)

# Displaying the result
print("The compound interest is:{compound_interest}")


