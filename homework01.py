class BankAccount:
    def __init__(self, name, balance, secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    def withdraw(self, amount, secret):
        if secret == self.__secret:
            if self.__balance < amount:
                print("You don't have enough money")
                return False
            else:
                self.__balance -= amount
                print("Withdraw successfully.")
                print(f"Your remain balance is: {self.__balance}")
                return True
        else:
            print("Invalid input")
            return False

    def check_balance(self, secret):
        if secret == self.__secret:
            print(f"{self.name} Balance: {self.__balance}")
            return self.__balance
        else:
            print("Who are you?")
            return None

    def deposit(self, amount, secret):
        if secret == self.__secret:
            if amount > 0:
                self.__balance += amount
                print(f"{self.name} Deposit successfully.")
                print(f"Your remain balance is: {self.__balance}")
                return True
            else:
                print("Deposit amount must be positive")
                return False
        else:
            print("Who are you?")
            return False

    def payment(self, service, amount, secret):
        if secret == self.__secret:
            if amount > self.__balance:
                print("You don't have enough money")
                return False
            else:
                self.__balance -= amount
                print(f"{self.name} Payment for {service} successfully.")
                print(f"Your remain balance is: {self.__balance}")
                return True
        else:
            print("You are not allowed.")
            return False

    def transfer(self, receiver_account, amount, secret):
        if secret == self.__secret:
            if amount > self.__balance:
                print("You don't have enough money")
                return False
            else:
                self.__balance -= amount
                receiver_account._BankAccount__balance += amount
                print(f"{self.name} transferred Reil{amount} to {receiver_account.name} successfully.")
                print(f"{self.name} remain balance is: {self.__balance}")
                print(f"{receiver_account.name} balance is: {receiver_account._BankAccount__balance}")
                return True
        else:
            print("You are not allowed.")
            return False

    def _add_balance(self, amount):
        self.__balance += amount


class SavingAccount(BankAccount):
    def calculate_interest(self):
        self._add_balance(10)
        print(f"Added 10 to {self.name} saving account")
        print(f"Your new balance is: {self._BankAccount__balance}")


class StudentBankAccount(BankAccount):
    MAX_WITHDRAWAL = 500

    def withdraw(self, amount, secret):
        if secret == self._BankAccount__secret:
            if amount <= 0:
                print("✗ Withdrawal amount must be positive")
            elif amount > self.MAX_WITHDRAWAL:
                print(f"✗ You can't withdraw the money over ${self.MAX_WITHDRAWAL}")
            elif amount > self._BankAccount__balance:
                print("✗ Insufficient funds")
            else:
                self._BankAccount__balance -= amount
                print(f"✓ {self.name} Withdraw {amount} successfully.")
                print(f"✓ {self.name} balance remains: ${self._BankAccount__balance}")
        else:
            print("Invalid input")


class PremiumSaving(SavingAccount):
    BONUS_RATE = 0.02

    def deposit(self, amount, secret):
        if secret == self._BankAccount__secret:
            if amount > 0:
                bonus = amount * self.BONUS_RATE
                total = amount + bonus
                self._BankAccount__balance += total
                print(f"✓ {self.name} Deposited ${amount}")
                print(f"✓ Your Bonus (2%): ${bonus:.1f}")
                print(f"✓ {self.name} Total added: ${total:.1f}")
                print(f"✓ Now {self.name} balance is: ${self._BankAccount__balance:.2f}")
            else:
                print("✗ Deposit amount must be positive")
        else:
            print("Invalid input")


class BusinessAccount(BankAccount):
    def __init__(self, name, balance, secret):
        super().__init__(name, balance, secret)
        self.loan_amount = 0

    def take_loan(self, amount, secret, loaner_account):
        if secret == self._BankAccount__secret:
            if amount <= 0:
                print("✗ Loan amount must be positive")
            else:
                self.loan_amount += amount
                self._BankAccount__balance += amount
                loaner_account._BankAccount__balance -= amount
                print(f"✓ {self.name} approved for loan of ${amount}")
                print(f"  Total borrowed: ${self.loan_amount}")
                print(f"  {self.name} received ${amount} from {loaner_account.name}")
                print(f"  {self.name} balance is: ${self._BankAccount__balance}")
                print(f"  {loaner_account.name} balance remains: ${loaner_account._BankAccount__balance}")
        else:
            print("Invalid input")



savingAccounts = {
    "dara": SavingAccount("Dara", 30000, 123),
    "visual": SavingAccount("Visual", 40000, 456),
    "chanthy": SavingAccount("Chanthy", 150000, 789),
}
student_Accounts = {
    "student1": StudentBankAccount("Student1", 50000, 456),
    "student2": StudentBankAccount("Student2", 60000, 654),
    "student3": StudentBankAccount("Student3", 90000, 999),
}
premiumAccounts = {
    "premium1": PremiumSaving("Premium1", 60000, 111),
    "premium2": PremiumSaving("Premium2", 70000,777),
}
business_accounts = {
    "loantaker1": BusinessAccount("Loantaker1", 30000, 444),
    "loantaker2": BusinessAccount("Loantaker2", 40000, 555),
}


while True:
    print("\n----Bank Menu----")
    print("1. Withdraw")
    print("2. Check balance")
    print("3. Deposit")
    print("4. Payment")
    print("5. Transfer")
    print("6. Saving Account ")
    print("7. StudentBankAccount")
    print("8. Premium Saving Account")
    print("9. Business Account")
    print("10. Exit")
    choice = input("Enter your choice: ")

    if choice == "10":
        break

    all_keys = list(savingAccounts.keys()) + list(student_Accounts.keys()) + list(premiumAccounts.keys())+ list(business_accounts.keys())
    print("Available accounts:", ", ".join(all_keys))
    account_name = input("Enter account name: ").lower()

    if account_name not in savingAccounts and account_name not in student_Accounts and account_name not in premiumAccounts and account_name not in business_accounts:
        print("Invalid account")
        continue

    if account_name in savingAccounts:
        selected = savingAccounts[account_name]
    elif account_name in student_Accounts:
        selected = student_Accounts[account_name]
    elif account_name in premiumAccounts:
        selected = premiumAccounts[account_name]
    else:
        selected = business_accounts[account_name]

    if choice == "1":
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.withdraw(amount, secret)
    elif choice == "2":
        secret = int(input("Enter secret: "))
        selected.check_balance(secret)
    elif choice == "3":
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.deposit(amount, secret)
    elif choice == "4":
        service = input("Enter service: ")
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.payment(service, amount, secret)
    elif choice == "5":
        to_name = input("Enter recipient account (dara/visual/chanthy): ").lower()
        if to_name not in savingAccounts:
            print("Invalid recipient account")
            continue
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.transfer(savingAccounts[to_name], amount, secret)
    elif choice == "6":
        secret = int(input("Enter secret: "))
        if secret == selected._BankAccount__secret:
            selected.calculate_interest()
        else:
            print("Invalid secret")
    elif choice == "7":
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.withdraw(amount, secret)

    elif choice == "8":
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.deposit(amount, secret)


    elif choice == "9":

        if not isinstance(selected, BusinessAccount):
            print("✗ Only Business Accounts can take loans")
            continue
        loaner_name = input("Enter loaner account name (who will lend the money): ").lower()
        loaner = None

        if loaner_name in savingAccounts:

            loaner = savingAccounts[loaner_name]

        elif loaner_name in student_Accounts:

            loaner = student_Accounts[loaner_name]

        elif loaner_name in premiumAccounts:

            loaner = premiumAccounts[loaner_name]

        elif loaner_name in business_accounts:

            loaner = business_accounts[loaner_name]

        if loaner is None:
            print("Invalid loaner account")

            continue
        amount = float(input("Enter loan amount: "))
        secret = int(input("Enter secret loan account: "))

        selected.take_loan(amount, secret, loaner)
    else:
        print("Invalid choice")