def age_cal():
    age = input("Please enter your age: ")
    if age == "" :
        print("Please enter a valid age. Age cannot be negative or zero, you can run the program again.")
        age_cal()
    else :
        age1 = int(age)
        print("\n===== AGE CALCULATOR =====\n")
        print(f"Current Age: {age1}")
        print(f"Age after 1 year: {age1 + 1}")
        print(f"Age after 5 years: {age1 + 5}")
        print(f"Age after 10 years: {age1 + 10}")
        print("\n=============================\n")
        exit()
age_cal()