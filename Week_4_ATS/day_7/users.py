import random
import csv
from decimal import Decimal
# from wallet import Wallet

# todo: Create a user class, wallet, transaction class
class User:
    ALL_USERS = []
    CSV_FILENAME = 'users.csv'
    USER_HEADERS = ['user_id', 'name', 'email', 'account balance', 'wallet_id']

    def __init__(self, name, email, acc_balance: float = 0.0) -> None:
        self.__name = name
        self.__email = email
        self.__acc_balance = acc_balance
        # self.user_id = self.generate_userid()
        # self.wallet_id = self.generate_walletid()
        self.data = {'name': self.__name, 'email': self.__email, 'account balance': acc_balance,
                     'user_id': self.user_id, 'wallet_id': self.wallet_id}

        User.ALL_USERS.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not (0 <= len(name) < 50) or not name.isalnum():
            raise ValueError(f'Name {name} may be too long or not alphanumeric')
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
        if acc_bal < Decimal('0.0'):
            raise ValueError('Balance must be >= 0')

    @classmethod
    def read_data(cls):
        with open(cls.CSV_FILENAME, 'r') as f:
            csv_data = csv.DictReader(f)
            return list(csv_data)

    def save_data(self, csv_filename, header, data):
        with open(csv_filename, 'a', newline='') as f:
            handler = csv.DictWriter(f, fieldnames=header)
            handler.writeheader()
            handler.writerow(data)

    @staticmethod
    def generate_userid():
        id = 'U'
        for _ in range(4):
            id += str(random.randint(0, 9))
        return id

    @staticmethod
    def generate_walletid():
        id = 'W'
        for _ in range(4):
            id += str(random.randint(0, 9))
        return id


    # todo: 1) creating a user
    def create_user(self):
        csv_users = self.read_data()
        for row in csv_users:
            if row['email'] == self.__email:
                print(f'User with email {self.__email} already registered!')
                return

        self.save_data(User.CSV_FILENAME, User.USER_HEADERS, self.data)

        User(
            name=self.__name,
            email=self.__email,
            acc_balance=self.__acc_balance
        )

    # todo: 2) deleting
    def del_user(self):
        pass


class Transaction(User):
    pass


# todo: 4) logging transactions

user = User('Ahmad', 'ahmadsharafudeen98@gmail.com', Decimal('3000.00'))
user.create_user()
print(user.user_id)
