while True:
    print("\n===== CALCULATOR =====\n")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Reminder\n6. Power\n7. Floor Division\n8. Exit")
    print("\n======================\n")    
    print("Enter your choice (1-8): ")
    choice = input()
    match choice:
        case "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print(f"Result: {result}")
        case "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print(f"Result: {result}")
        case "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print(f"Result: {result}")
        case "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {result}")
        case "5":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 % num2
            print(f"Result: {result}")
        case "6":
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter exponent number: "))
            result = num1 ** num2
            print(f"Result: {result}")
        case "7":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 // num2
            print(f"Result: {result}")
        case "8":
            print("Exiting the calculator. Goodbye!")
            break