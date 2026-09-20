age = 20 
has_id = False

if age >= 18 and has_id:
    print("Access 1 granted")
else:
    print("Access 1 denied")

if age >= 18 or has_id:
    print("Access 2 granted")   
else:
    print("Access 2 denied")
    
is_banned = False

if not is_banned:
    print("Access 3 granted")