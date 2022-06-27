import pyinputplus as pyip 
import random

def det_username():
    first_name = pyip.inputStr("Enter your first name: ").lower()
    middle_name = pyip.inputStr("Enter your second name: ").lower()
    last_name = pyip.inputStr("Enter your second name: ").lower()
    
    rand_digits = random.randrange(0, 9)

    username = first_name[:3] + middle_name[0] + last_name[:4] + (str(rand_digits) * 2)
    return username

print(det_username())