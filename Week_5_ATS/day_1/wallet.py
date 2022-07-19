from decimal import Decimal
from datetime import datetime

class Wallet():
    logs = []

    def __init__(self, init_bal, bank_acct):
        self.date_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.acc_balance = init_bal
        self.bank_acct = bank_acct

    # todo: 3) funding the wallet
    def fund_wallet(self):
        """Deposit money to the wallet."""
        amount = int(input('Enter amount to fund: '))
        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.acc_balance += amount
        Wallet.logs.append(f"Date: {self.date_time} Deposited: {amount}")

    def get_balance(self):
        print(f"You have #{self.acc_balance} in your wallet")

    def withdraw_to_bank(self):
        amount = int(input('Enter the amount to withdraw: '))

        # check if balance is sufficient for transaction
        if self.acc_balance < amount:
            print('You do not have enough money in your wallet!')
            return
        self.acc_balance -= amount
        print(f'Payment successful. You now have #{self.acc_balance} left in your wallet')

        Wallet.logs.append(f"Date: {self.date_time} Withdrawn: {amount} To: {self.bank_acct}")


