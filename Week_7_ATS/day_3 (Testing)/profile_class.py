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
        if hasattr(self, 'attendance'):
            self.attendance += 1
        else:
            print('Profile not initialized yet!')
        
        
    def __str__(self) -> str:
        return f"Full Name: {self.first_name} {self.last_name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}, Attendance: {self.attendance}"
                
        
        
profile = Profile()
# profile.get_all_students()
# get all students
print(Profile.get_all_students())

print(profile.initialize_student('Ahmad'))
profile.increment_attendance()

print(profile.attendance if hasattr(profile, 'attendance') else 'No such attribute yet!')