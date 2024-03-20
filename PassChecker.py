user = str(input("Enter your preferred username: "))
password = ""
while len(password) < 8:
    password = str(input("Please enter your password: "))
    if len(password) < 8:
        print("Password criteria not met, please enter a password longer than 8 characters.")
    else:
        print("Account has been created.")