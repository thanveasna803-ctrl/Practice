class BankAccount:

    def __init__(self, name, balance, secret):
        self.name = name
        self.balance = balance
        self.secret = secret

    
    def __check_secret(self, secret):
        return self.secret == secret


    def deposit(self, amount, secret):

        if not self.__check_secret(secret):
            return "Wrong secret!"

        if amount <= 0:
            return "Invalid amount!"

        self.balance += amount
        return f"Deposit success. Balance: {self.balance}"

    
    def payment(self, service, amount, secret):

        if not self.__check_secret(secret):
            return "Wrong secret!"

        if amount > self.balance:
            return "Not enough balance!"

        self.balance -= amount
        return f"Paid {service}: {amount}. Balance: {self.balance}"

    
    def transfer(self, account, amount, secret):

        if not self.__check_secret(secret):
            return "Wrong secret!"

        if amount > self.balance:
            return "Not enough balance!"

        self.balance -= amount
        account.balance += amount

        return f"Transfer {amount} to {account.name} success"



Veasna = BankAccount("Veasna", 5000, "1234")
Chantha = BankAccount("Chantha", 3000, "4321")


print("-----------------------------------------------")
print(Veasna.transfer(Chantha, 1000, "1234"))

print("-----------------------------------------------")
print("Veasna Balance:", Veasna.balance)
print("-----------------------------------------------")
print("Chantha Balance:", Chantha.balance)

print("-----------------------------------------------")
print(Veasna.deposit(500, "1234"))

print("-----------------------------------------------")
print(Chantha.payment("Electricity bill", 300, "4321"))
