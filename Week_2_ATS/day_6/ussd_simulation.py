# program that simulates a bank USSD application.

import random
import sys
 
recharge_card_bal = 0
data_bal = 0
account_bal = 5000

acct_details = {"12345": 600, "67890": 900}
phone_numbers = {"09034": [200, 12], "08123": [50, 10], "09155": [100, 15]}

# TO-DOs
# set PIN
def set_pin():
    pin = input("Set your 4-digit Pin: ")
    if len(pin) != 4:
        print(f"ERROR: Pin must be 4-digits")
        return set_pin()
    if not pin.isdecimal():
        print("PIN can be only be numbers")
        return set_pin()
    print("Your PIN has been successfully set")
    return pin

PIN = set_pin()

# 1) check balance
def check_bal():
    return f"Your account balance is: #{account_bal}"
    
# 2) transfer cash
def transfer_cash():
    global account_bal
    transfer_amount = int(input("Enter the amount you want to transfer: "))
    pin = input("Enter your Pin: ")
    if pin == PIN:
        if transfer_amount > account_bal:
            return f"You do not have enough money in your account to complete the transfer"
        account_bal -= transfer_amount
        receiver_acct = input("Enter the receiver's account number: ")
        if acct_details.get(receiver_acct) != None: 
            acct_details[receiver_acct] += transfer_amount
            print(acct_details[receiver_acct])
            return f"""#{transfer_amount} has been transferred to {receiver_acct}
                    Your remaining balance is #{account_bal}"""
        return "Account Number not found"
    return "The PIN you entered is incorrect. You can reset your PIN"
    
# 3) load airtime
def load_airtime():
    global account_bal, recharge_card_bal
    confirm_owner = input("Type \"1\" to load for self or \"2\" to load for others: ")
    amount = int(input("Please enter amount: "))
    gen_otp = generate_otp()
    print(gen_otp)
    user_otp = input("Please enter the OTP sent to your device: ")
    if user_otp != gen_otp:
        return f"The OTP you entered is incorrect. Try again later"
    if account_bal > amount:
        if confirm_owner == "1":
            recharge_card_bal += amount
            return f"You recharge was successful. Recharge card balance is: {recharge_card_bal}"
        elif confirm_owner == "2":
            receiver = input("Please enter 3rd party mobile number: ")
            if phone_numbers.get(receiver) != None: 
                account_bal -= amount
                phone_numbers[receiver][0] += amount
                print(phone_numbers[receiver])
                return f"#{amount} recharge card has been successfully transferred to {receiver}"
            return f"Phone number not yet registered"
    return f"Your account balance is too low to complete your transaction"
            
# 4) load data
def load_data():
    global data_bal, account_bal
    confirm_owner = input("Type \"1\" to purchase data for Self or \"2\" to load for 3rd party: ")
    data_dict = {"1": [100, 100], "2": [350, 300], "3": [750,500], "4": [1000, 300], "5": [1500, 1000]}
    print("Select MTN bundle")
    print("1) 100MB 1day N100")
    print("2) 350MB 7days N300")
    print("3) 750MB 14days N500")
    print("4) 1GB 1day N300")
    print("5) 1.5GB 30dayS N1000")
    selected = input("Enter number here: ")
    data_mb = data_dict[selected][0]
    data_cost = data_dict[selected][1]
    if data_cost < account_bal:
        if confirm_owner == "1":
            account_bal -= data_cost
            data_bal += data_mb
            return f"""Your data subscription was successful. New data balance is: {data_bal}MB.
                        #{data_cost} has been deducted from your account balance.
                    """
        elif confirm_owner == "2":
            phone_num = input("Please enter 3rd party mobile number: ")
            account_bal -= data_cost
            if phone_numbers.get(phone_num) != None: 
                phone_numbers[phone_num][1] += data_mb
                print(phone_numbers[phone_num])
                return f"""{data_mb}MB has been successfully transferred to {phone_num}
                        Your new account balance is {account_bal}
                        """
            return "Phone number not yet registered"
    return f"Your account balance is too low to complete your transaction"

# 5) generate a four-digit OTP
def generate_otp():
    otp = ""
    for _ in range(0, 4):
        otp += str(random.randint(0,9))
    return otp

while True:
    print("\nBank USSD Simulation Program.")
    print("1) Check Balance")
    print("2) Transfer Cash")
    print("3) Load Airtime")
    print("4) Load Data")
    print("5) Quit\n")
    
    action = int(input("Enter number for the action to perform: "))
    ussd_dict = {1: check_bal, 2: transfer_cash, 3: load_airtime, 4: load_data, 5: sys.exit}
    print(ussd_dict[action]())