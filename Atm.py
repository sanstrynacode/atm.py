class ATM():
    def __init__(self):
        self.balance = 0

    def deposit(self, user):
        self.balance += user.amount
        print(f"Deposit Successful.✅ New Balance: {self.balance}💰")
    
    def withdraw(self, user):
        if self.balance < user.amount:
            print(f"🤨 Don't tryna con me brokie. Your balance is {self.balance} 🚨")
            return False
        else:
            self.balance -= user.amount
            print(f"Withdraw Successful.✅ Your new balance is {self.balance}💸")
            
    def checkbalance(self):
        print(f"Your current balance is ﹩{self.balance}.")

class Customers():
    def __init__(self, name, pin, amount):
        self.name = name
        self.pin = pin
        self.amount = amount

def save(user, account):
    with open(f"{user.name}.txt", "w") as f:
        f.write(f"{user.name}," f"{user.pin}," f"{account.balance}")
    print("Customer Information Updated.🧍‍♂️")

account = ATM()
choice = int(input("1.Create Account🆕  |2.Load Account💾"))
if choice == 2:
    try:
        temp_name = input("Enter your account name: ")
        open(f"{temp_name}.txt", "r")
        if open: 
            temp_pin = int(input("👀 Enter your pin"))
            with open(f"{temp_name}.txt", "r") as f:
                data = f.read().split(",")
                user = Customers(data)
                user.name = data[0]
                user.pin = int(data[1])
                account.balance = float(data[2])
                if temp_pin == user.pin:
                    print("Verification Successful...🕵")
                    choice
                else: 
                    print("Incorrect Pin‼️")
        else:
            print("🏦... We couldn't find your account. Creating a new one...🏦")
            choice = 1
    except FileNotFoundError:
        print("🏦... We couldn't find your account. Creating a new one...🏦")
        choice = 1

if choice == 1:
    name = input("Enter your name: ")
    pin = int(input("👀 Enter your pin: "))
    amount = int(input("💵 Enter your amount: "))
    user = Customers(name, pin, amount)

account.checkbalance()

    


