# todo: A signup and sign-in program that takes info:

import csv
import pandas
# todo: login credentials. Add validation. Password must be a minimum of 8 characters
def validate_username():
    username = input(f"Enter username: ")
    # check if username exists in csv
    with open("./Week_3_ATS/day_2/user_db.csv", 'r') as f:
        handler = csv.DictReader(f) 
        for row in handler:
            if row['username'] == username:
                print("INVALID: User with username already exists in DB!")
                return validate_username()
    return username

def validate_str(name):
    str_val = input(f"Enter {name}: ")
    if str_val.isalnum():
        return str_val
    print(f"{name} must be letters only!")
    return validate_str(name)

def is_pass():
    password = input("Enter an 8-digit password: (Passwords must be alphanumeric!): ")
    if password.isalnum() and len(password) >= 8:
        return password
    print("ERROR: Incrrect format. Re-enter password again!")
    return is_pass()
    
def val_pass(password):
    newpassword = input("Confirm Password: ")
    if newpassword == password:
        return newpassword
    print("ERROR: password mismatch!")
    return val_pass()

def signup():
    # todo: On signup, username, first name, last name, password and confirm password and saves it in a file
    username = validate_username()
    first_name = validate_str("first name")
    last_name = validate_str("last name")
    password = is_pass()
    confirm_pass = val_pass(password)
    
    headers = ["username", "first name", "last name", "password", "password confirm"]
    data = {"username": username, "first name": first_name, "last name": last_name, "password": password, "password confirm": confirm_pass}

    with open("./Week_3_ATS/day_2/user_db.csv", 'a', newline='') as f:   
        handler = csv.DictWriter(f, fieldnames=headers)
        # handler.writeheader()
        
        handler.writerow(data)
        f.close()
    print("Signup Successful!")
    
# todo: on signin, it takes username and password  and return whether a message saying login successful or invalid    
def signin():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("./Week_3_ATS/day_2/user_db.csv", 'r') as f:
        handler = csv.DictReader(f) 
        for row in handler:
            if row['username'] == username and row['password'] == password:
                print(f"Login Successful!\nWelcome back {row['first name']}")
                return 
        print(f"User Account not found. Signup first")
        return    

def main():
    todo = input("Type  \"1\" to Signup or \"2\" to Signin: (Signin is set by default!): ")
    if todo == "1":
        signup() 
    else:
        signin()
        
        
if __name__ == '__main__':
    main()



    
    





