import random
import csv
import sys
from decimal import Decimal
from wallet import Wallet

# todo: Create a user class, wallet, transaction class
class User(Wallet):

    def __init__(self, name, email, bank_acct, init_bal: float = 0.0) -> None:
        self.__name = name
        self.__email = email
        self.__init_bal = init_bal
        self.bank_acct = bank_acct
        self.user_id = self.generate_userid()
        self.wallet = Wallet(init_bal= self.__init_bal, bank_acct=self.bank_acct)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print('setting')
        if len(name) > 5:
            
            raise ValueError("Incorrect!")
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not '@' in email:
            raise ValueError(f'{email} format not correct!')
        self.__email = email

    @property
    def acc_balance(self):
        return self.__acc_balance

    @acc_balance.setter
    def acc_balance(self, acc_bal):
        if acc_bal < 0:
            raise ValueError('Balance must be >= 0')

    @staticmethod
    def generate_userid():
        id = 'U'
        for _ in range(4):
            id += str(random.randint(0, 9))
        return id


    # todo: 1) creating a user
    @classmethod
    def create_user(cls, name, email, bank_acct, init_bal):
        return cls(name, email, bank_acct, init_bal)

    # todo: 2) deleting
    # def del_user(self):
    #     pass

newuser = User('Ahmad Sharaf', 'ahmad@gmail.com', '0923', 900)
# print('Welcome!, \nRegister your details first')
# name = input('Name: ')
# email = input('Email: ')
# bank_acc = input('Account Number: ')
# init_bal = Decimal(input('Amount to open account with: '))

# user = User.create_user(name=name, email=email, bank_acct=bank_acc, init_bal=init_bal)
# while True:
#     option = input("""
#         Select an action to perform:
#         1. Fund Wallet
#         2. Get Balance
#         3. Withdraw to Bank
#         4. Get all transaction logs
#         5. Exit
#     """)
#     if option == '1':
#         user.wallet.fund_wallet()
#     elif option == '2':
#         user.wallet.get_balance()
#     elif option == '3':
#         user.wallet.withdraw_to_bank()
#     elif option == '4':
#         [print(x) for x in user.wallet.logs]
#     elif option == '5':
#         sys.exit()


