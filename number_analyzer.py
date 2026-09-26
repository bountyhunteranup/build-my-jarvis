num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.") 
else:
    print(f"{num} is zero.")

if num % 2 == 0:
    print(f"{num} is an even number.")
elif num % 2 != 0:
    print(f"{num} is an odd number.")
else:
    print("Invalid input.")