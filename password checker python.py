# Take password input from user
password = input("Enter password: ")

# Check if entered password is correct
if password == "danish123":
    print("Access Granted")   # If correct password
else:
    print("Access Denied")    # If wrong password

#modified code
# User sets their own password
user_password = input("Create your password: ")

# User tries to login
login_password = input("Enter your password: ")

if login_password == user_password:
    print("Access Granted")
else:
    print("Wrong Password - Access Denied")


