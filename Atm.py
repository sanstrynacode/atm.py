class ATM():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Successful.✅ New Balance: {self.balance}💰")
    
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"🤨 Don't tryna con me brokie. Your balance is {self.balance} 🚨")
        else:
            self.balance -= amount
            print(f"Withdraw Successful.✅ Your new balance is {self.balance}💸")

    def checkbalance(self):
        print(f"Your current balance is ﹩{self.balance}.")

class Customers():
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        

def save(user, account):
    with open(f"{user.name}.txt", "w") as f:
        f.write(f"{user.name}," f"{user.pin}," f"{account.balance}")
    print("Customer Information Updated.🧍‍♂️")

verification = False
account = ATM()
choice = int(input("1.Create Account🆕  |2.Load Account💾"))
if choice == 2:
    try:
        temp_name = input("Enter your account name: ")
        open(f"{temp_name}.txt", "r")
        print(f"Welcome back {temp_name}")
        with open(f"{temp_name}.txt", "r") as f:
            data = f.read().split(",")
            if len(data) < 3:
                print("⚠️ Error: Save file is corrupted or empty.")
                exit()
            name = data[0]
            pin = int(data[1])
            account.balance = float(data[2])
            user = Customers(name, pin)
            attempts = 1
            while attempts <= 3: 
                temp_pin = int(input("👀 Enter your pin: "))
                if temp_pin == user.pin:
                    print("Verification Successful...🕵")  
                    verification = True
                    break
                else: 
                    print(f"❌Incorrect Pin‼️. You have {3 - attempts} remining attempts.")
                    verification = False
                    attempts += 1
                    if not verification:
                        print("Too many incorrect tries. U better get outta here now.🚔")   
                        exit()

    except FileNotFoundError:
        print("🏦... We couldn't find your account. Run again to create a new one...🏦")
        exit()
        

if choice == 1:
    name = input("Enter your name: ").strip().lower()
    pin = int(input("👀 Enter your pin: "))
    user = Customers(name, pin)
    save(user, account)
    verification = True
if verification: 
    print("-------🏧 Welcome 🏧-------")
    transaction = True
    while transaction:
        num = int(input("1.Withdraw Money💰  |2.Deposit Money💸  |3.Check Balance💵  |4.Exit🚪"))
        try:
            if num == 4:
                print("Exiting......")
                save(user, account)
                game = False
                break
            elif num == 1:
                amount = int(input("Enter your amount:"))
                account.withdraw(amount)
            elif num == 2:
                amount = int(input("Enter your amount:"))
                account.deposit(amount)
            elif num == 3:
                account.checkbalance()
        except ValueError:
            print("Invalid Choice❌")
        game = input("Do you wanna continue?(y/n)")
        try:
            if game == 'y':
                transaction = True
            elif game == 'n':
                print ("Exiting.....")
                transaction = False
                save(user, account)
                
        except ValueError:
            print("Invalid Choice❌")


