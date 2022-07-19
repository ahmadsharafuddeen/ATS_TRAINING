from decimal import Decimal
from datetime import datetime
import pandas as pd
import users

class Wallet():
    
    def __init__(self, wallet_id):
        self.time = datetime.now().strftime('%H:%M:%S')
        self.wallet_id = wallet_id

    # todo: 3) funding the wallet
    def fund_wallet(self, amount):
        """Deposit money to the wallet."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        accounts = self.read_data()
        for account in accounts:
            if self.user_id == account['user_id']:
                account['account balance'] += amount

    def check_balance(self):
        accounts = self.read_data()
        balance = 0
        for account in accounts:
            if self.wallet_id == account['wallet_id']:
                balance = account['account balance']
        return Decimal(balance)

    def make_purchase(self):
        self.amount = int(input('Enter the amount of item you want to purchase: '))
        self.product = input('Enter the name of the product you wish to purchase: ')

        # check if balance is sufficient for transaction
        if self.check_balance() < self.amount:
            print('You do not have enough money in your wallet!')
            return
        all_accounts = self.read_data()
        for account in all_accounts:
            if account['wallet_id'] == self.wallet_id:
                bal = account.get('account balance')
                dec_bal = Decimal(bal)
                df = pd.read_csv(self.TRANS_FNAME, index_col='wallet_id')
                df.loc[self.wallet_id, 'account balance'] = dec_bal - self.amount
                df.to_csv(self.TRANS_FNAME)

        print(f'Payment successful. You now have #{self.check_balance()} left in your wallet')

        # save transaction history
        data = {'wallet_id': self.wallet_id, 'product': self.product, 'time': self.time, 'price': self.amount}
        self.save_data(Wallet.TRANS_FNAME, Wallet.TRANSACTION_HEADER, data)

user_wallet1 = Wallet('W4943')
user_wallet1.make_purchase()
