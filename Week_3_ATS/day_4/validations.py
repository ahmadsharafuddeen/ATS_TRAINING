# todo: A signup and sign-in program that takes info:

import csv
import sys
import shutil
from tempfile import NamedTemporaryFile
import pyinputplus as pyip

# todo: login credentials. Add validation. Password must be a minimum of 8 characters

# global vars
headers = ["username", "first name", "last name", "password", "password confirm", "phone_num", "address", "dob",
           "gender"]
csv_filename = "./Week_3_ATS/day_4/updated_user_db.csv"
tempfile = NamedTemporaryFile(mode='w', delete=False)


def read_data():
    with open(csv_filename, 'r') as f:
        csv_data = csv.DictReader(f)
        return list(csv_data)


def save_data(headers, data):
    with open(csv_filename, 'a', newline='') as f:
        handler = csv.DictWriter(f, fieldnames=headers)
        # handler.writeheader()
        handler.writerow(data)

def check_username(username):
     profiles = read_data()
     for row in profiles:
        if row['username'] == username:
            raise Exception("INVALID: User with username already exists in DB!")
        return username

def get_username():
    return pyip.inputCustom(check_username, prompt="Enter username: ")


def get_str_input(name):
    return pyip.inputStr(f"Enter {name}: ")


def get_optional(name):
    return pyip.inputStr(f"Enter {name}: ", blank=True)


def get_gender():
    return pyip.inputMenu(['male', 'female'], prompt="Gender: ")


def get_phone_num():
    return pyip.inputStr(prompt="Enter your phone number: ")


def get_date_of_birth():
    return pyip.inputDate(prompt="Enter your dob e.g.: 03/10/99", formats=["%m/%d/%y"], blank=True)


def check_password(password):
    if not password.isalnum() and len(password) < 8:
        raise Exception("ERROR: Incorrect format. Re-enter password again!")
    return password

def get_password():
    return pyip.inputCustom(check_password, prompt="Enter an 8-digit password: (Passwords must be alphanumeric!): ")


def get_validated_pw(password):
    newpassword = pyip.inputPassword("Confirm Password: ")
    if newpassword == password:
        return newpassword
    print("ERROR: password mismatch!")
    return get_validated_pw(password)


def signup():
    # todo: On signup, username, first name, last name, password and confirm password and saves it in a file
    username = get_username()
    first_name = get_str_input("first name")
    last_name = get_str_input("last name")
    password = get_password()
    confirm_pass = get_validated_pw(password)

    data = {"username": username, "first name": first_name, "last name": last_name, "password": password,
            "password confirm": confirm_pass}
    save_data(headers, data)

    print("Signup Successful, Sign In Please!")
    signin()


# todo: on signin, it takes username and password  and return whether a message saying login successful or invalid
def signin():
    username = pyip.inputStr("Enter your username: ")
    password = pyip.inputPassword("Enter your password: ")

    for row in read_data():
        if row['username'] == username and row['password'] == password:
            print(f"Login Successful!\nWelcome back {row['first name']}")

            option = pyip.inputInt(prompt="Enter: \n1- Edit Profile\n2- Change Password\n3- Logout\n", min=1, max=3)
            if option == 1:
                edit_profile(username, set="profile")
            elif option == 2:
                edit_profile(username, set="password", password=password)
            elif option == 3:
                print(f"Logging you out, {username}")
                sys.exit()
            return
    print(f"User Account not found. Signup first")
    return


def edit_profile(username: str, set, password=''):
    if set == "profile":
        phone_num = get_phone_num()
        address = get_optional("address")
        dob = get_date_of_birth()
        gender = get_gender()
    elif set == "password":
        old_password = pyip.inputPassword(prompt="Enter your old password: ")
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
                    if address != '':
                        row["address"] = address
                    if dob != '':
                        row["dob"] = dob
                    row["gender"], row["phone_num"] = gender, phone_num
                elif set == "password":
                    row["password"], row["password confirm"] = new_password, new_password
            row = {"username": row["username"], "first name": row["first name"], "last name": row["last name"],
                   "password": row["password"], "password confirm": row["password confirm"],
                   "phone_num": row["phone_num"],
                   "address": row["address"], "dob": row["dob"], "gender": row["gender"]}
            writer.writerow(row)
    shutil.move(tempfile.name, csv_filename)
    print(f"{username}'s profile editted successfully.")


def main():
    todo = pyip.inputInt("Type  \"1\" to Signup or \"2\" to Signin: (Signin is set by default!): ", allowRegexes=['\d'])
    if todo == 1:
        signup()
    else:
        signin()


if __name__ == '__main__':
    main()
