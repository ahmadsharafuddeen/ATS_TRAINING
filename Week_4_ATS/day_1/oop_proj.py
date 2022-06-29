from datetime import date
import pprint
from turtle import back

backend_dict = {
    "ahmad@gmail.com": {'first_name': 'Ahmad', 'last_name': 'Sharafudeen', 'day_month': '9-3', 'attendance': 11, 'height': 160,
    'weight': 55, 'age': 25},
    "awwal@gmail.com": {'first_name': 'Awwal', 'last_name': 'Adeleke', 'day_month': '4-6', 'attendance': 11, 'height': 165,
    'weight': 61, 'age': 21},
    'Abdulwali@gmail.com': {'first_name': 'Abdulwali', 'last_name': 'Tajudeen', 'day_month': '10-12', 'attendance': 11,'height': 170,
    'weight': 52, 'age': 24},
    'abraham@gmail.com': {'first_name': 'Abraham','last_name': 'Adekunle', 'day_month': '2-6', 'attendance': 11, 'height': 157,
    'weight': 70, 'age': 28},
    'yusuff@gmail.com': {'first_name': 'Yusuf', 'last_name': 'Oyedele', 'day_month': '22-7', 'attendance': 11,'height': 172,
    'weight': 64, 'age': 26},
    'adebusola@gmail.com': {'first_name': 'Adebusola', 'last_name': 'Adeyeye', 'day_month': '14-8', 'attendance': 11, 'height': 131,
    'weight': 58, 'age': 24},
    'basheer@gmail.com': {'first_name': 'Basheer', 'last_name': 'Balogun', 'day_month': '19-11', 'attendance': 11, 'height': 141,
    'weight': 48, 'age': 22},
    'abdullahi@gmail.com': {'first_name': 'Abdullahi', 'last_name': 'Salaam', 'day_month': '13-9', 'attendance': 11, 'height': 156,
    'weight': 68, 'age': 19},
    'faith@gmail.com': {'first_name': 'Faith', 'last_name': 'Adeosun', 'day_month': '17-4', 'attendance': 11, 'height': 141,
    'weight': 56, 'age': 22},
    'lukman@gmail.com': {'first_name': 'Lukman', 'last_name': 'Abisoye', 'day_month': '15-2', 'attendance': 11, 'height': 169,
    'weight': 59, 'age': 27},
    'toluwanimi@gmail.com': {'first_name': 'Toluwanimi','last_name': 'Ogunbiyi', 'day_month': '12-7', 'attendance': 11, 'height': 181,
    'weight': 53, 'age': 23},
}

class Student:
    def __init__(self, email) -> None:
        self.first_name = backend_dict[email]['first_name']
        self.last_name = backend_dict[email]['last_name']
        self.day_month = backend_dict[email]['day_month']
        self.attendance = backend_dict[email]['attendance']
        self.height = backend_dict[email]['height']
        self.weight = backend_dict[email]['weight']
        self.age = backend_dict[email]['age']
        self.email = email
    
    
    # A) method that increments attendance
    def increment_attendance(self):
        self.attendance += 1
        
    # B) method that update first and last name
    def update_names(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        return f"Your new name is now {self.first_name} {self.last_name}"
        
    # C) method that returns full names in title case
    def title_fullname(self):
        return f'{self.first_name} {self.last_name}'.title()
    
    # D) method that returns name of birth month
    def det_birth_month(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']
        mon_dig = int(self.day_month.split('-')[1])
        return f"{self.first_name} was given birth to in the month of {months[mon_dig]}"
    
    # E) method that calculates profile BMI
    def calculate_bmi(self):
        # convert height from cm to m
        height = self.height / 100
        bmi = self.weight / pow(height, 2)
        return f"{self.first_name}'s BMI is {round(bmi, 2)}"
    
    # F) method that calculates birth year of profile
    def calc_birth_year(self):
        birth_year = date.today().year - self.age
        return f"{self.first_name} was born in the year {birth_year}"
    
    # G) A method that will return student's initials
    def stud_initials(self):
        return f"Your initials is {self.first_name[0]}.{self.last_name[0]}"
    
    # H) method that returns max age of the class
    def get_max_age(self):
        max_age = 0
        for profile in backend_dict.keys():
            current_age = backend_dict[profile]['age']
            if current_age > max_age:
                max_age = current_age
        print(f"The maximum age of the class is {max_age}")
        return max_age
    
    # I) method that returns min age of the class
    def get_min_age(self):
        min_age = self.get_max_age()
        for profile in backend_dict.keys():
            current_age = backend_dict[profile]['age']
            if current_age < min_age:
                min_age = current_age
        print(f"The minimum age of the class is {min_age}")
        return min_age
    
    # J) function that return the total number of people in the class
    def get_total_students(self):
        return f"There are {len(backend_dict)} students in class"
    
    # K) function that can add profile to class 
    def add_new_stud(self, email, first_name, last_name, day_month, attendance, height, weight, age):
        backend_dict[email] = {'first_name': first_name, 'last_name': last_name, 'day_month': day_month, 'attendance': attendance,
                               'height': height, 'weight': weight, 'age': age}
        print(f"{self.first_name} just added student '{first_name}'")
        return backend_dict
    
    # L) Remove profile from the class
    def remove_student(self):
        del backend_dict[self.email]
        return backend_dict
    
    # M) calculate the avg of ages
    def avg_age_stud(self):
        sum_ages = 0
        for profile in backend_dict.keys():
            sum_ages += backend_dict[profile]['age']
        return f"The average age of the students is {int(sum_ages/len(backend_dict))}"           
    
    # N) Function that will group profiles by birth month
    def group_stud_by_month(self):
        groups = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}}
        
        for profile in backend_dict.keys():
            profile_month = int(backend_dict[profile]['day_month'].split('-')[1])
            groups[profile_month][profile] = backend_dict[profile]     
        pprint.pprint(groups)
        
        
    
stud_01 = Student('ahmad@gmail.com')
stud_02 = Student('awwal@gmail.com')

print(stud_01.last_name)
print(stud_01.get_min_age())

stud_02.increment_attendance()
print(stud_01.update_names("Muhammad", "Raji"))
print(stud_01.stud_initials())
print(stud_01.calculate_bmi())
print(stud_02.attendance)
# print(stud_02.add_new_stud('yaasir@gmail.com', 'Yaasir', 'Adewale', '04-09', 3, 167, 62, 23))
print(stud_01.avg_age_stud())
stud_01.group_stud_by_month()


    
    
        
    
        
    
        
        
        