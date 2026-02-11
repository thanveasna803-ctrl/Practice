class BankAccount:
    def __init__(self,balance,name,secret):
        self.__balance=balance
        self.name=name
        self.__secret=secret

    def withdraw(self):
        print(f"{self.name} withdraw is money")
    def deposite(self):
        print(f"{self.name} deposite is money") 
    def check_balance(self,secret):
        if secret == self.__secret:
            print (f'{self.name} rewmaining balance is {self.__balance}' )
        else:
            print("i'm not")

dara=BankAccount(balance=2000,name="Dara",secret="0001")
# print(f"Balance  {dara.name} is: " ,dara.balance)
dara.withdraw()
veasna=BankAccount(balance=5000,name="Bora",secret="0002")
# print(f"Balance {veasna.name} is:" ,veasna.balance)
veasna.deposite()


dara.check_balance(secret="0001")
veasna.check_balance(secret="0002")
