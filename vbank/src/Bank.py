from User import (User, UserData)

class Bank(object):

    def __init__(self, bank_name: str) -> None:
        self.bank_name: str = bank_name
        self.users: list[User] = list()
        
    def connect(self, user: User) -> None:
        if isinstance(user, User) and user.getAuthMode():
            self.users.append(user)

    def getUsers(self) -> None:
        for id, user in enumerate(self.users):
            user_data: UserData = user.getData()
            print(f'{id}. Username: {user_data[0]}\tBalance: {user_data[1]}')

    def disconnect(self, user: User) -> None:
        if isinstance(user, User):
            self.users.remove(user)

    def getReceipt(self, amount: float, sender: User, receiver: User) -> None:
        sender_data: UserData = sender.getData()
        receiver_data: UserData = receiver.getData()
        print('Processing Bank Transfer Request')
        print(f'Withdrawal of ${amount} from {sender_data[0]} Validated')
        print('\t' + sender.getReceipt(type='withdraw', amount=amount))
        print(f'Deposit of ${amount} to {receiver_data[0]} Validated!')
        print('\t' + receiver.getReceipt(type='deposit', amount=amount))
            

    def transfer(self, sender: User, receiver: User, amount: float) -> None:
        sender.withdraw(amount=amount, root_access='Bank')
        receiver.deposit(amount=amount, root_access='Bank')
        self.getReceipt(amount=amount, sender=sender, receiver=receiver)
        
