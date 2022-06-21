import csv

def validate_str(name):
    str_val = input(f"Enter {name}: ")
    if str_val.isalpha():
        return str_val
    print(f"{name} must be letters only!")
    return validate_str(name)

def validate_num(num: str):
    num_val = input(f"Enter your {num}: ")
    if num_val.isnumeric():
        return num_val
    print(f"{num} must be a number.")
    return validate_num(num)

def val_gender():
    gender = input("Enter your gender (M - Male, F - Female): ")
    if gender in ["M", "F"]:
        return gender
    print("ERROR: Enter either \"M\" or \"F\" as values")
    return val_gender()

def val_mar():
    gender = input("Enter your marital status (M - Married, S - Single): ")
    if gender in ["M", "S"]:
        return gender
    print("ERROR: Enter either \"M\" or \"S\" as values")
    return val_mar()

def val_email():
    email = input("Enter your email address: ")
    if "@" in email:
        return email
    print("Error: Not valid email addres")
    return val_email()

todo = input("What do you want to do: \"Save\" to save record or \"Search\" to search: ")
if todo == "Save":
    first_name = validate_str("first name")
    last_name = validate_str("last name")
    middle_name = validate_str("middle name")
    age = validate_num("age")
    occupation = input("Enter your occupation: ")
    dob = input("Enter your date of birth: ")
    gender = val_gender()
    marital_status = val_mar()
    email = val_email()
    
    headers = ["first_name", "last_name", "age", "occupation", "dob", "gender", "marital_status", "email"]
    data = {"first_name": first_name, "last_name": last_name, 
                        "age": age, "occupation": occupation, "dob": dob,
                        "gender": gender, "marital_status": marital_status, "email": email}

    with open("./Week_3_ATS/day_2/class_work.csv", 'a', newline='') as f:   
        handler = csv.DictWriter(f, fieldnames=headers)
        # handler.writeheader()
        handler.writerow(data)
        f.close()
elif todo == "Search":
    search_term = input("Enter search term: ").lower()
    
    # with open("./Week_3_ATS/day_2/class_work.csv", "r") as reader:
    #     for row in reader.readlines():
    with open("./Week_3_ATS/day_2/class_work.csv", 'r') as f:
        handler = csv.DictReader(f) 
        for row in handler:
            if search_term in row['first_name'].lower() or row['last_name'].lower() or row['email'].lower():
                print(row)
            else:
                print("Such record doesn't exist in our csv")   





