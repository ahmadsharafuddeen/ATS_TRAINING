from csv_oop import User
import csv
import csv, shutil

class Profile(User):
    def __init__(self, username='', first_name='', last_name='', password='', phone_num='', address='', dob='', gender='') -> None:
        super().__init__(username, first_name, last_name, password, phone_num, address, dob, gender)
        
    def get_user(self, username):
        all_profiles = User._read_data()
        
        for profile in all_profiles:
            if profile['username'] == username:
                self._username = profile['username']
                self.first_name = profile['first name']
                self.last_name = profile['last name']
                self.password = profile['password']
                self.phone_num = profile['phone_num']
                self._address = profile['address']
                self._dob = profile['dob']
                self.gender = profile['gender']
                break
        return repr(self)
    
    def edit(self, **kwargs):
        self.first_name = kwargs.get('first_name', self.first_name)
        self.last_name = kwargs.get('last_name', self.last_name)
        self.password = kwargs.get('password', self.password)
        self.phone_num = kwargs.get('phone_num', self.phone_num)
        self._address = kwargs.get('address', self._address)
        self._dob = kwargs.get('dob', self._dob)
        self.gender = kwargs.get('gender', self.gender)
        
        with open(self.CSV_FILENAME, 'r') as csvfile, self.TEMPFILE:
            reader = csv.DictReader(csvfile, fieldnames=self.HEADERS)
            writer = csv.DictWriter(self.TEMPFILE, fieldnames=self.HEADERS)
            
            for row in reader:
                if row['username'] == self._username:
                    row = {"username": self._username, "first name": self.first_name, "last name": self.last_name, "password": self.password,
                        "phone_num": self.phone_num, "address": self._address, "dob": self._dob, "gender": self.gender}
                writer.writerow(row)
        shutil.move(self.TEMPFILE.name, self.CSV_FILENAME)
        print(f"{self._username}'s profile editted successfully.")
        print(self.get_user(self._username))
            
        
        
profile = Profile()
print(profile.get_user('awwalade'))
profile.edit(phone_num='09023245464', address='Aja, Lagos', dob='09/02', gender='female')


        


    