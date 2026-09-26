weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: " ))

bmi = weight/(height ** 2)

print(f"Your BMI is: {bmi}")

if bmi < 19:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
