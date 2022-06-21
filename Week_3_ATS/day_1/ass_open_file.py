# A program that asks for your username, firstname,
# lastname, password, password confirmation and saves it in text file
# with name as username

username = input("Enter your username: ")
first_name = input("Enter your firstname: ")
last_name = input("Enter your last name: ")
password = input("Enter your password: ")
if input("confirm password: ") == password:
    confirm_password = password
    
    with open(f"./Week_3_ATS/day_1/{username}.txt", 'w') as f:
        f.write(f'''    Username: {username}
        Name: {first_name}First
        Last Name: {last_name}
        Password: {password}
        Password Confirm: {confirm_password}''')    
else:
    print("Error: Password Mismatch")
    

    # f.write(f"First Name: {first_name}\n")
    # f.write(f"Last Name: {last_name}\n")
    # f.write(f"Password: {password}\n")
    # f.write(f"Password Confirm: {confirm_password}\n")