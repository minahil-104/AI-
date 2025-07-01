#Question:15 Speed, Distance, and Time

# Input distance and time from the user
distance = float(input("Enter distance (in kilometers): "))
time = float(input("Enter time (in hours): "))

# Check the time
if time != 0:
    speed = distance / time
    print("Speed is:", speed, "km/h")
else:
    print("Time cannot be zero.")
