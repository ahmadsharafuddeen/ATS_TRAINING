username = "adeniyi"
password = "pass1234"

in_user = input("Enter your username: ")
in_pass = input("Enter your password: ")

while in_user != username or in_pass != password:
    print("Incorrect Username and/or Password. Try again!")
    in_user = input("Enter your username: ")
    in_pass = input("Enter your password: ")

print("login Successful!")
