correct_username = "admin"
correct_password = "password123"

def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        exit()
    elif username != correct_username and password == correct_password:
        print("Username must match!!!")
        login_system()
    elif username == correct_username and password != correct_password:
        print("Password must match!!!")
        login_system()
    else:
        print("Username and password must match!!!")
        login_system()
    
login_system()
