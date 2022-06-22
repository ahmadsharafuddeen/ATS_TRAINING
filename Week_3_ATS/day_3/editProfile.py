# todo: A signup and sign-in program that takes info:

import csv, sys
from fileinput import filename
from tempfile import NamedTemporaryFile
import shutil
# todo: login credentials. Add validation. Password must be a minimum of 8 characters

# global vars
headers = ["username", "first name", "last name", "password", "password confirm", "phone_num", "address", "dob", "gender"]
csv_filename = "./Week_3_ATS/day_3/updated_user_db.csv"
tempfile = NamedTemporaryFile(mode='w', delete=False)

def read_data():
     with open(csv_filename, 'r') as f:
        csv_data = csv.DictReader(f) 
        return list(csv_data)
    
def save_data(headers, data):
    with open(csv_filename, 'a', newline='') as f:   
        handler = csv.DictWriter(f, fieldnames=headers)
        handler.writeheader()
        handler.writerow(data)
    
def get_username():
    username = input(f"Enter username: ")
    # check if username exists in csv
    profiles = read_data()
    for row in profiles:
        if row['username'] == username:
            print("INVALID: User with username already exists in DB!")
            return get_username()
    return username

def get_str_input(name):
    str_val = input(f"Enter {name}: ")
    if str_val.isalnum():
        return str_val
    print(f"{name} must be letters only!")
    return get_str_input(name)

def get_gender():
    gender = input("Enter your gender (male/female): ")
    if gender in ["M", "F"]:
        return gender
    print("ERROR: Enter either \"male\" or \"female\" as values")
    return get_gender()

def get_password():
    password = input("Enter an 8-digit password: (Passwords must be alphanumeric!): ")
    if password.isalnum() and len(password) >= 8:
        return password
    print("ERROR: Incrrect format. Re-enter password again!")
    return get_password()
    
def get_validated_pw(password):
    newpassword = input("Confirm Password: ")
    if newpassword == password:
        return newpassword
    print("ERROR: password mismatch!")
    return get_validated_pw()

def signup():
    # todo: On signup, username, first name, last name, password and confirm password and saves it in a file
    username = get_username()
    first_name = get_str_input("first name")
    last_name = get_str_input("last name")
    password = get_password()
    confirm_pass = get_validated_pw(password)

    data = {"username": username, "first name": first_name, "last name": last_name, "password": password, "password confirm": confirm_pass}
    save_data(headers, data)
    
    print("Signup Successful, Sign In Please!")
    signin()
    
# todo: on signin, it takes username and password  and return whether a message saying login successful or invalid    
def signin():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for row in read_data():
        if row['username'] == username and row['password'] == password:
            print(f"Login Successful!\nWelcome back {row['first name']}")
            
            option = int(input("Enter 1- Edit Profile, 2- Change Password, 3- Logout: "))
            if option == 1:
                edit_profile(username, "profile")
            elif option == 2:
                edit_profile(username, "password", password=password)
            elif option == 3:
                print(f"Logging you out, {username}")
                sys.exit()
            
            return 
    print(f"User Account not found. Signup first")
    return    

def edit_profile(username: str, set, password = ''):
    if set == "profile": 
        phone_num = get_str_input("phone number")
        address = get_str_input("address") or ''
        dob = get_str_input("dob") or ''
        gender = get_gender()
    elif set == "password":
        old_password = input("Enter your old password: ")
        if old_password == password:
            new_password = get_password()
        else:
            print("Incorrect password")
    
    with open(csv_filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=headers)
        writer = csv.DictWriter(tempfile, fieldnames=headers)
        
        for row in reader:
            if row['username'] == username:
                if set == "profile":
                    row["phone_num"], row["address"], row["dob"], row["gender"] = phone_num, address, dob, gender
                elif set == "password":
                    row["password"], row["password confirm"] = new_password, new_password
            row = {"username": row["username"], "first name": row["first name"], "last name": row["last name"], 
                    "password": row["password"], "password confirm": row["password confirm"], "phone_num": row["phone_num"], 
                    "address": row["address"], "dob": row["dob"], "gender": row["gender"]}
            writer.writerow(row)
    shutil.move(tempfile.name, csv_filename)
    print(f"{username}'s profile editted successfully.")
    
    
def change_pw(row: dict):
    pass

def logout(profile):
    pass
    
def siginin_options(profile):
    pass

def main():
    todo = input("Type  \"1\" to Signup or \"2\" to Signin: (Signin is set by default!): ")
    if todo == "1":
        signup() 
    else:
        signin()
        
        
if __name__ == '__main__':
    main()