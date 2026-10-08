temp = float(input("Enter temperature: "))

option = input("Enter the conversion option (C to F or F to C): ")

if option.upper() == "C":
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp}°F")
elif option.upper() == "F":
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid option. Please enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius.")