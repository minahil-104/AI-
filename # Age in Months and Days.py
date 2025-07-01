#Q:11 Age in Months and Days

def calculate_age(age_years):
    months = age_years * 12
    days = age_years * 365  
    return months, days

# Input from user
age_years = int(input("Enter your age in years: "))

# Calculation
months, days = calculate_age(age_years)

# Output
print("\nYour age in months:",months)
print("Your age in days:" ,days)
