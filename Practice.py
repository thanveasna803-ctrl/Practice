class BankAccount:

    def init(self, name, balance, secret):
        self.name = name
        self.balance = balance
        self.secret = secret


    def __check_secret(self, secret):
        return self.secret == secret


    def deposit(self, amount, secret):

        if not self.__check_secret(secret):
            return "❌ Wrong secret!"

        if amount <= 0:
            return "❌ Invalid amount!"

        self.balance += amount
        return f"✅ Deposit success. Balance: {self.balance}"


    def payment(self, service, amount, secret):

        if not self.__check_secret(secret):
            return "❌ Wrong secret!"

        if amount > self.balance:
            return "❌ Not enough balance!"

        self.balance -= amount
        return f"✅ Paid {service}: {amount}. Balance: {self.balance}"


    def transfer(self, account, amount, secret):

        if not self.__check_secret(secret):
            return "❌ Wrong secret!"

        if amount > self.balance:
            return "❌ Not enough balance!"

        self.balance -= amount
        account.balance += amount

        return f"✅ Transfer {amount} to {account.name} success"



# ==========================
# Create Accounts
# ==========================

accounts = {}

accounts["Veasna"] = BankAccount("Veasna", 5000, "1234")
accounts["Chantha"] = BankAccount("Chantha", 3000, "4321")


# ==========================
# Login System
# ==========================

print("===== BANK LOGIN =====")

name = input("Enter name: ")
secret = input("Enter secret: ")

if name not in accounts:
    print("❌ Account not found!")
    exit()

user = accounts[name]

if secret != user.secret:
    print("❌ Wrong password!")
    exit()

print("✅ Login Success!")


# ==========================
# Menu System
# ==========================

while True:

    print("\n===== MENU =====")
    print("1. Deposit")
    print("2. Payment")
    print("3. Transfer")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose (1-5): ")


    # Deposit
    if choice == "1":

        amount = float(input("Enter amount: "))
        password = input("Enter secret: ")

        print(user.deposit(amount, password))


    # Payment
    elif choice == "2":

        service = input("Service name: ")
        amount = float(input("Enter amount: "))
        password = input("Enter secret: ")

        print(user.payment(service, amount, password))


    # Transfer
    elif choice == "3":

        to_name = input("Transfer to: ")

        if to_name not in accounts:
            print("❌ Account not found!")
            continue

        amount = float(input("Enter amount: "))
        password = input("Enter secret: ")

        receiver = accounts[to_name]

        print(user.transfer(receiver, amount, password))


    # Check Balance
    elif choice == "4":

        print(f"💰 Balance = {user.balance}")


    # Exit
    elif choice == "5":

        print("👋 Goodbye!")
        break


    else:
        print("❌ Invalid choice!")