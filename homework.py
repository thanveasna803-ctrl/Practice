class BankAccount:

    def __init__(self, name, balance, secret):
        self.name = name
        self.balance = balance
        self.secret = secret

    def __check_secret(self, secret):
        return self.secret == secret

    def show_balance(self):
        return f"Balance: {self.balance}$"

    def deposit(self, amount, secret):

        if not self.__check_secret(secret):
            return "Wrong secret!"

        if amount <= 0:
            return "Invalid amount!"

        self.balance += amount
        return f"Deposit success. Balance: {self.balance}$"

    def withdraw(self, amount, secret):

        if not self.__check_secret(secret):
            return "Wrong secret!"

        if amount <= 0:
            return "Invalid amount!"

        if amount > self.balance:
            return "Not enough balance!"

        self.balance -= amount
        return f"Withdraw success. Balance: {self.balance}$"

    def payment(self, service, amount, secret):

        if not self.__check_secret(secret):
            return "Wrong secret!"

        if amount <= 0:
            return "Invalid amount!"

        if amount > self.balance:
            return "Not enough balance!"

        self.balance -= amount
        return f"Paid {service}: {amount}$ | Balance: {self.balance}$"

    def transfer(self, account, amount, secret):

        if not self.__check_secret(secret):
            return "Wrong secret!"

        if amount <= 0:
            return "Invalid amount!"

        if amount > self.balance:
            return "Not enough balance!"

        self.balance -= amount
        account.balance += amount

        return f"Transfer {amount}$ to {account.name} success!"


# ================= Student Account =================

class StudentBankAccount(BankAccount):

    def withdraw(self, amount, secret):

        if amount > 500:
            return "Student can withdraw max 500$ only!"

        return super().withdraw(amount, secret)


# ================= Saving Account =================

class SavingBankAccount(BankAccount):
    pass


class PremiumSaving(SavingBankAccount):

    def deposit(self, amount, secret):

        if amount <= 0:
            return "Invalid amount!"

        bonus = amount * 0.02
        total = amount + bonus

        self.balance += total

        return f"Deposit {amount}$ + Bonus {bonus}$ = {total}$ | Balance: {self.balance}$"


# ================= Business Account =================

class BusinessAccount(BankAccount):

    def take_loan(self, amount):

        if amount <= 0:
            return "Invalid loan amount!"

        self.balance += amount

        return f"Loan received {amount}$ | Balance: {self.balance}$"


# ================= TEST =================

accounts = {}

accounts["dara"] = StudentBankAccount("dara", 5000, "1234")
accounts["viva"] = PremiumSaving("viva", 3000, "4321")
accounts["boss"] = BusinessAccount("boss", 10000, "9999")


print("===== BANK LOGIN =====")

name = input("Enter name: ")
secret = input("Enter secret: ")

if name not in accounts:
    print("Account not found!")
    exit()

user = accounts[name]

if secret != user.secret:
    print("Wrong password!")
    exit()

print("Login Success!")

while True:

    print("\n===== MENU =====")
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Payment")
    print("5. Transfer")
    print("6. Take Loan (Business Only)")
    print("7. Exit")

    choice = input("Choose (1-7): ")

    if choice == "1":
        print(user.show_balance())

    elif choice == "2":
        amount = float(input("Enter amount: "))
        password = input("Enter secret: ")
        print(user.withdraw(amount, password))

    elif choice == "3":
        amount = float(input("Enter amount: "))
        password = input("Enter secret: ")
        print(user.deposit(amount, password))

    elif choice == "4":
        service = input("Service name: ")
        amount = float(input("Enter amount: "))
        password = input("Enter secret: ")
        print(user.payment(service, amount, password))

    elif choice == "5":

        to_name = input("Transfer to: ")

        if to_name not in accounts:
            print("Account not found!")
            continue

        amount = float(input("Enter amount: "))
        password = input("Enter secret: ")

        receiver = accounts[to_name]

        print(user.transfer(receiver, amount, password))

    elif choice == "6":

        if isinstance(user, BusinessAccount):

            amount = float(input("Loan amount: "))
            print(user.take_loan(amount))

        else:
            print("This feature is for Business Account only!")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")