# import pprint
# from datetime import date
# from turtle import back

# # Back-end Students RECORD

# backend_dict = [
#     {'first_name': 'Ahmad', 'last_name': 'Sharafudeen', 'day_month': '9-3', 'attendance': 11, 'height': 160,
#     'weight': 55, 'age': 25},
#     {'first_name': 'Awwal','last_name': 'Adeleke', 'day_month': '4-6', 'attendance': 11, 'height': 165,
#     'weight': 61, 'age': 21},
#     {'first_name': 'Abdulwali', 'last_name': 'Tajudeen', 'day_month': '10-12', 'attendance': 11,'height': 170,
#     'weight': 52, 'age': 24},
#     {'first_name': 'Abraham', 'last_name': 'Adekunle', 'day_month': '2-6', 'attendance': 11, 'height': 157,
#     'weight': 70, 'age': 28},
#     {'first_name': 'Yusuff', 'last_name': 'Oyedele', 'day_month': '22-7', 'attendance': 11,'height': 172,
#     'weight': 64, 'age': 26},
#     {'first_name': 'Adebusola', 'last_name': 'Adeyeye', 'day_month': '14-8', 'attendance': 11, 'height': 131,
#     'weight': 58, 'age': 24},
#     {'first_name': 'Basheer', 'last_name': 'Balogun', 'day_month': '19-11', 'attendance': 11, 'height': 141,
#     'weight': 48, 'age': 22},
#     {'first_name': 'Abdullahi', 'last_name': 'Salaam', 'day_month': '13-9', 'attendance': 11, 'height': 156,
#     'weight': 68, 'age': 19},
#     {'first_name': 'Faith', 'last_name': 'Adeosun', 'day_month': '17-4', 'attendance': 11, 'height': 141,
#     'weight': 56, 'age': 22},
#     {'first_name': 'Lukman', 'last_name': 'Abisoye', 'day_month': '15-2', 'attendance': 11, 'height': 169,
#     'weight': 59, 'age': 27},
#     {'first_name': 'Toluwanimi', 'last_name': 'Ogunbiyi', 'day_month': '12-7', 'attendance': 11, 'height': 181,
#     'weight': 53, 'age': 23},
# ]

# # print(backend_dict)
# def get_profile_index(first_name):
#     for index in range(len(backend_dict)):
#         if backend_dict[index]['first_name'] == first_name:
#             return index

# # A) function to increment attendance
# def increment_attendance(first_name):
#     index = get_profile_index(first_name)
#     backend_dict[index]['attendance'] += 1
#     return backend_dict[index]

# print(increment_attendance('Ahmad'))

# # B) function that update first and last name
# def update_names(old_first_name, new_first_name, new_last_name):
#     index = get_profile_index(old_first_name)
#     backend_dict[index]['first_name'] = new_first_name
#     backend_dict[index]['last_name'] = new_last_name
#     return backend_dict[index]

# print(update_names('Ahmad', 'Adeniyi', 'Sharaf'))

# # C) funtion that returns full names in title case
# def all_full_names(student_records):
#     full_names = []
#     for index in range(len(student_records)):
#         full_names.append(f"{student_records[index]['first_name']} {student_records[index]['last_name']}".title())
#     return full_names
        
# # print(all_full_names(backend_dict))

# # D) function that can add profile to class
# def add_new_stud(**kwargs):
#     backend_dict.append(kwargs)
#     return backend_dict
    
# # print(add_new_stud(first_name='Faatimah', last_name='Sharafudeen', day_month='8-21', attendance=13, height=151, weight=55, age=25))

# # E) function that return the total number of people in the class
# def count_students(student_records):
#     return len(student_records)

# # print(f"There are {count_students(backend_dict)} students in backend")

# # F) Remove profile from the class
# def remove_student(first_name):
#     index = get_profile_index(first_name)
#     del backend_dict[index]
#     return backend_dict

# # print(remove_student('Toluwanimi'))

# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
#           'November', 'December']

# # G) Function that returns name of birth month 
# def month_of_birth(first_name: str) -> str:
#     index = get_profile_index(first_name)
#     dob = backend_dict[index]['day_month']
#     mon_dig = int(dob.split('-')[1])
#     return months[mon_dig - 1]

# # print(month_of_birth("Awwal"))

# # F) Function that will group profiles by birth month
# def group_by_month():
#     backend_dict.sort(key=lambda profile: profile['day_month'].split('-')[1:][0])
#     return backend_dict

# pprint.pprint(group_by_month())

# # G) A function that will return list of initials
# def stud_initials(stud_list):
#     initials = []
#     for name in stud_list:
#         initials.append(f"{name[:1]}.{stud_list[name]['last_name'][:1]}")
#     return initials
   
# # print(stud_initials(backend_dict))

# # H) function that calculates profile BMI
# def calc_bmi(profile_name, profiles):
#     s_weight = profiles[profile_name]['weight']
#     s_height = profiles[profile_name]['height'] / 100
     
#     bmi = s_weight / pow(s_height, 2)
#     return f"{profile_name}'s BMI is {round(bmi, 2)}"

# # print(calc_bmi("Ahmad", backend_dict))

# # I) function that calculates the avg of ages
# def average_age(profiles):
#     ages = []
#     for profile in profiles:
#         ages.append(profiles[profile]['age'])
#     print(ages)
#     average = sum(ages) / len(ages)
#     return f"Average age of students is {round(average)}"

# # print(average_age(backend_dict))

# # J) function that return max age of the class
# def max_age_stud(profiles):
#     max = 0
#     for profile in profiles:
#         stud_age = profiles[profile]['age']
#         if stud_age > max:
#             max = stud_age
#     return f"The maximum age of the class is {max}"

# # print(max_age_stud(backend_dict))

# # K) function that return min age of the class
# def min_age_stud(profiles):
#     min = 50
#     for profile in profiles:
#         stud_age = profiles[profile]['age']
#         if stud_age < min:
#             min = stud_age
#     return f"The minimum age of the class is {min}"

# # print(min_age_stud(backend_dict))

# # L) function that calculates birth year of a profile
# def calc_birth_year(profile_name, profiles):
#     age = profiles[profile_name]['age']
#     birth_year = date.today().year - age
#     return f"The birth year of {profile_name} is {birth_year}"

# # print(calc_birth_year("Ahmad", backend_dict))
    
    
# def add_5_nums(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     average = sum / len(nums)
#     return average

# print(add_5_nums(1,2,3,4,5))   

# # positional args
# def positional_addition(n1, n2, n3, n4, n5):
#     sum = n1 + n2 + n3 + n4 + n5
#     return sum / 5


# # func takes 5 args and prints types of each
# # create 5 vars, assign 5 datatypes into it
# def det_datatypes(a=1, b='', c=[], d={}, e=()):
#     print(type(a)) 
    
# det_datatypes()



class Profile:
    students = [
        {'first_name': 'Abdulwali', 'last_name': 'Tajudeen', 'day_month': '10-12', 'attendance': 11,'height': 170,
        'weight': 52, 'age': 24},
        {'first_name': 'Abraham', 'last_name': 'Adekunle', 'day_month': '2-6', 'attendance': 11, 'height': 157,
        'weight': 70, 'age': 28},
        {'first_name': 'Yusuff', 'last_name': 'Oyedele', 'day_month': '22-7', 'attendance': 11,'height': 172,
        'weight': 64, 'age': 26},
    ]
    
    
    def __init__(self, **kwargs) -> None:
        pass
    
        
    def initialize_student(self, first_name):
        for i in range(len(self.students)):
            if self.students[i]['first_name'] == first_name:
                profile = self.students[i]
                self.first_name = profile['first_name']
                self.last_name = profile['last_name']
                self.dob = profile['day_month']
                self.age = profile['age']
                self.height = profile['height']
                self.weight =profile['weight']
                self.attendance = profile['attendance']
                return self
            return f"Profile with first name '{first_name}' not found!"
                
    @classmethod
    def get_all_students(cls):
        all_names = []
        for i in range(len(cls.students)):
            all_names.append(f"{cls.students[i]['first_name']} {cls.students[i]['last_name']}")
        return all_names        
        
    def increment_attendance(self):
        self.attendance += 1
        
        
    def __str__(self) -> str:
        return f"Full Name: {self.first_name} {self.last_name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}, Attendance: {self.attendance}"
                
        
        
profile = Profile()

# get all students
print(Profile.get_all_students())

print(profile.initialize_student('Abdulwali'))
profile.increment_attendance()
print(profile.attendance)


    
    