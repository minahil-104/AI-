#Question:1 Celsius to Fahrenheit Converter

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Taking input from user
celsius_input = float(input("Enter temperature in Celsius: "))

# Converting and displaying result

fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print("°C is equal to °F" ,celsius_input,fahrenheit_output)
