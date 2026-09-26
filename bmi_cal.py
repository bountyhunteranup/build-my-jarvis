weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: " ))

bmi = weight/(height ** 2)

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
elif bmi > 30:
    print("You are obese.")
else:
    print("Invalid input.")