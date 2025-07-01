#Quearion:10 Salary Sheet
def calculate_salary(basic_salary):
    hra = 0.20 * basic_salary
    da = 0.15 * basic_salary
    total_salary = basic_salary + hra + da
    return hra, da, total_salary

# Input from user
basic = float(input("Enter Basic Salary: "))

# Calculation
hra, da, total = calculate_salary(basic)

# Output
print("\nBasic Salary:",basic)
print("HRA (20%):",hra)
print("DA (15%):",da)
print("Total Salary:",total)

