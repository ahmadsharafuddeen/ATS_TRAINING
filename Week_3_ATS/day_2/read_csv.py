# from cgitb import handler
from cgitb import handler
import csv

# with open("./Week_3_ATS/day_2/username.csv", 'r') as f:
#     handler = csv.reader(f)
#     for row in handler:
#         print(row)
        
# with open("./Week_3_ATS/day_2/new.csv") as f:
#     handler = csv.writer(f)
#     handler.writerow(["username","school","department"])
    
# with open("./Week_3_ATS/day_2/email.csv", 'r') as f:
#     handler = csv.DictReader(f)
    
#     for row in handler:
#         print(row['Login email;Identifier;First name;Last name'])
        # print(row['school'])
        # print(row['department'])
        # print(row)
        
with open("./Week_3_ATS/day_2/username.csv", 'w') as f:
    headers = ["firstname", "lastname", "department"]
    handler = csv.DictWriter(f, fieldnames=headers)
    handler.writeheader()
    handler.writerow({"firstname": "Ahmad", "lastname": "Sharaf", "department": "CSE"})
    handler.writerow({"firstname": "Yasir", "lastname": "Alao", "department": "MEE"})
    handler.writerow({"firstname": "Ade", "lastname": "Kabiru", "department": "EEE"})
        

