unit_used = float(input("Enter the number of units consumed: "))

if unit_used <= 100:
    bill_amount = unit_used * 5
elif unit_used <= 200:
    bill_amount = (100 * 5) + ((unit_used - 100) * 7)
elif unit_used <= 300: 
    bill_amount = (100 * 5) + (100 * 7) + ((unit_used - 200) * 10)
else:
    bill_amount = (100 * 5) + (100 * 7) + (100 * 10) + ((unit_used - 300) * 15)
    
print(f"The total bill amount for {unit_used} units consumed is: ${bill_amount:.2f}")