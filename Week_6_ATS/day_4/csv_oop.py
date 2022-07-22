import csv, shutil, sys
from tempfile import NamedTemporaryFile
import pyinputplus as pyip
from sqlalchemy import PrimaryKeyConstraint

class User:
    # class variables
    TEMPFILE = NamedTemporaryFile(mode='w', delete=False)
    CSV_FILENAME = "./Week_6_ATS/day_4/updated_user_db.csv"
    HEADERS = ["username", "first name", "last name", "password", "phone_num", "address", "dob", "gender"]
    ALL_PROFILES = []
    
    @classmethod
    def _read_data(cls):
        with open(cls.CSV_FILENAME, 'r') as f:
            csv_data = csv.DictReader(f)
            list_data = list(csv_data)   
            return list_data
        
    @classmethod
    def _return_profiles(cls):
        for profile in cls._read_data():
            new_profile = User(profile['username'], profile['first name'], profile['last name'], profile['password'], 
                                profile['phone_num'], profile['address'], profile['dob'], profile['gender'])
            User.ALL_PROFILES.append(repr(new_profile))
        return cls.ALL_PROFILES
            
     
    @classmethod   
    def _save_data(self, data):
        with open(self.CSV_FILENAME, 'a', newline='') as f:
            handler = csv.DictWriter(f, fieldnames=self.HEADERS)
            # handler.writeheader()
            handler.writerow(data)
    
    def __init__(self, username, first_name, last_name, password , phone_num='', address='', dob='', gender='') -> None:
        self._username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.phone_num = phone_num
        self._address = address
        self._dob = dob
        self.gender = gender
        self.data = {"username": self._username, "first name": self.first_name, "last name": self.last_name, "password": self.password, "phone_num": self.phone_num,
                      "address": self._address, "dob": self.dob, "gender": self.gender}
        
    def __repr__(self):
        return f"User('{self._username}', '{self.first_name}', '{self.last_name}', '{self.password}', '{self.phone_num}', '{self._address}', '{self._dob}', '{self.gender}')"
    
    
    def __str__(self) -> str:
        return "User class"
    @property
    def dob(self):
        return self._dob
        
    # @property
    # def first_name(self):
    #     return self._first_name
    
    # @first_name.setter
    # def first_name(self, value):
    #     if not value.isalnum():
    #         raise ValueError("First name can only contain letters and/or numbers!")
    #     self._first_name = value
    
    # @property
    # def last_name(self):
    #     return self._last_name
    
    # @last_name.setter
    # def last_name(self, value):
    #     if not value.isalnum():
    #         raise ValueError("Last name can only contain letters and/or numbers!")
    #     self._last_name = value
        
    # @property
    # def password(self):
    #     return self._password
    
    # @password.setter
    # def password(self, value):
    #     if len(value) < 7 or not value.isalnum():
    #         raise ValueError("Password must be at least 8 alpha-numeric characters!")
    #     self._password = value
        
    # @property
    # def phone_num(self):
    #     return self._phone_num
    
    # @phone_num.setter
    # def phone_num(self, value):
    #     if value != '' and not value.isalnum():
    #         raise ValueError("Your Phone Number must be a String!")
    #     self._phone_num = value
        
    # @property
    # def gender(self):
    #     return self._gender
    
    # @gender.setter
    # def gender(self, value):
    #     if value != '' and value.lower() not in ['male', 'female']:
    #         raise ValueError("Value can either be 'male' or 'female'")
    #     self._gender = value
        
    # signup method
    def signup(self, confirm_pass):
        profiles = self._read_data()
        for row in profiles:
            if row['username'] == self.__username:
                print("INVALID: User with username already exists in DB!")
                return  
        if confirm_pass != self.password:
            print("Password Mismtch: Confirm Password again!")
            return 
        self._save_data(self.data)
        print("Signup Successful, Sign In Please!")
        username = pyip.inputStr("Enter your username: ")
        password = pyip.inputPassword("Enter your password: ")
        self.signin(username, password)
        
    # signin method
    def signin(self, username, password):
        for row in self._read_data():
            if row['username'] == username and row['password'] == password:
                print(f"Login Successful!\nWelcome back {row['first name']}")
                
                option = pyip.inputInt(prompt="Enter: \n1- Edit User\n2- Change Password\n3- Logout\n", min=1, max=3)
                if option == 1:
                    self.edit_profile(set="profile")
                elif option == 2:
                    self.edit_profile(set="password")
                elif option == 3:
                    print(f"Logging you out, {username}")
                    sys.exit()
                return
        print(f"User Account not found. Signup first")
        return
     
    def edit_profile(self, set):
        if set == "profile":
            self.phone_num = pyip.inputStr("Enter Phone number: ")
            self._address = pyip.inputStr("Enter address: ")
            self._dob = pyip.inputStr("Enter dob: ")
            self.gender = pyip.inputStr("Enter gender: ")
        elif set == "password":
            old_pass = pyip.inputPassword("Enter old password: ")
            if old_pass == self.password:
                new_pass = pyip.inputPassword("Enter new password: ")
                confirm_pass = pyip.inputPassword("Confirm password: ")
                if new_pass != confirm_pass:
                    print("Error: Password mismatch!")
                    return  
            else:
                print("The password you entered is incorrect!")  
                return
        
        with open(self.CSV_FILENAME, 'r') as csvfile, self.TEMPFILE:
            reader = csv.DictReader(csvfile, fieldnames=self.HEADERS)
            writer = csv.DictWriter(self.TEMPFILE, fieldnames=self.HEADERS)
            for row in reader:
                if row['username'] == self.username:
                    if set == 'profile':
                        row['phone_num'], row['address'], row['dob'], row['gender'] = self.phone_num, self.address, self.dob, self.gender
                    if set == 'password':
                        row['password'] = new_pass
                
                row = {"username": row["username"], "first name": row["first name"], "last name": row["last name"], "password": row["password"],
                        "phone_num": row["phone_num"], "address": row["address"], "dob": row["dob"], "gender": row["gender"]}
                writer.writerow(row)
        shutil.move(self.TEMPFILE.name, self.CSV_FILENAME)
        print(f"{self.username}'s profile editted successfully.")

    
profile1 = User('ahmadsharaf', 'Ahmad', 'Sharafudeen', 'Ahmad2022')#, '07066402941', 'Akobo, Ibadan', '09/03', 'male')
# profile1.signin(input('Username: '), input('Password: '))
profile2 = User('awwalade', 'Awwal', 'Adeleke', 'AdElEke21')#, '07066402941', 'Akobo, Ibadan', '09/03', 'male')
# profile2.signin(input('Username: '), input('Password: '))

profile3 = User('toyin', 'Toyin', 'Sam', 'Toyin099')
# profile3.edit_profile('profile')


