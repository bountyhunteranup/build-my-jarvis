age = int(input("Please enter your age: "))
has_id = input("Do you have an ID? (true/false): ").strip().lower()

if age >= 18 and has_id == "true":
    print("You are allowed to enter.")
elif age >= 18 and has_id == "false":
    print("You need an ID to enter.")
elif age < 18 and has_id == "true":
    print("You are not allowed to enter due to age restrictions.")  
else:
    print("You are not allowed to enter.")