class BankAccount :
    def __int__(self,balance,name,secret):
        self.balance=balance
        self.name=name
        self.secret=secret
    def withdraw(self):
        print(f"{self.name} withdraw is money"):
data =BankAccount(balance=2000, name='data','ggg22')
