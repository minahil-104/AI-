#Question:17 Convert Minutes to Hours and Minutes

# Input total minutes from the user
total_minutes = int(input("Enter total minutes: "))

# Calculate hours and remaining minutes
hours = total_minutes // 60
minutes = total_minutes % 60

# Display result
print("minutes = hour and minute", total_minutes , hours , minutes)
