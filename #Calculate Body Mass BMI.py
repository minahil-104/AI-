#Q:16 Calculate Body Mass BMI
# Input weight and height from the user
weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))

# Check the height
if height != 0:
    BMI = weight / (height ** 2)
    print("Your BMI is:", round(BMI))
else:
    print("Height cannot be zero.")
