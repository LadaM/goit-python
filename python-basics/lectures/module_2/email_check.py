name = input("Enter your name ")
email = input("Enter email ")
password = input("Please enter your password now ")

# email validation logic
if email.isspace():
    print("Email address cannot be empty")
else:
    if '@' not in email:
        print("Invalid email address")
    else:
        if password.isspace() or len(password) < 8:
            print("Password must be not empty and contain at least 8 characters")
        else:
            print("Login successful!")