from random import randint
from typing import NamedTuple
from 

UserData = NamedTuple('UserData', [('username', str), ('balance', float), ('previous_balance', float)])

class User(object):

    def __init__(self, username: str, password: str) -> None:
        self.is_authenticated: bool = False
        self.account_name: str = username
        self.account_number: str = str(randint(1111111111, 9999999999))
        self.password: str = password
        self.previous_balance: float = float()
        self.account_balance: float = float()

    def __str__(self) -> str:
        return f'Account Owner: {self.account_name}\nBalance: {self.account_balance}'
    
    def getReceipt(self, type: str, amount: float) -> str:
        return \
            f'{type.title()} of {amount} Processed & Confirmed!\n' \
            f'Previous Balance: ${self.previous_balance}\n' \
            f'Current Balance: ${self.account_balance}\n'
        
    def deposit(self, amount: float = float(), root_access = None) -> None:
        if root_access is None:
            if input('Enter Password to Confirm Deposit: ') == self.password:
                self.authenticate()
                self.previous_balance = self.account_balance
                self.account_balance += amount
                print(self.getReceipt(type='deposit', amount=amount))
                self.is_authenticated = False
        if root_access == 'Bank':
            self.previous_balance = self.account_balance
            self.account_balance += amount

    def withdraw(self, amount: float = float(), root_access = None) -> None:
        if root_access is None:
            if input('Enter Password to Confirm Withdrawal: ') == self.password:
                self.authenticate()
                self.previous_balance = self.account_balance
                self.account_balance -= amount
                print(self.getReceipt(type='withdraw', amount=amount))
                self.is_authenticated = False
        if root_access == 'Bank':
            self.previous_balance = self.account_balance
            self.account_balance -= amount

    def getData(self) -> UserData:
        return UserData(self.account_name, self.account_balance, self.previous_balance)
    
    def getAuthMode(self) -> bool:
        return self.is_authenticated
    
    def authenticate(self) -> None:
        self.is_authenticated = True
