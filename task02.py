def deposit(balance, amount):
    balance += amount
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Yetarli mablag' mavjud emas.")
        return balance
    balance -= amount
    return balance

def check_balance(balance):
    print(f" balans: {balance}")
    return balance

balance = 100000  #  balans
amal = "deposit"
miqdor = 50000

if amal == "deposit":
    balance = deposit(balance, miqdor)
elif amal == "withdraw":
    balance = withdraw(balance, miqdor)
elif amal == "check":
    check_balance(balance)

print(f"✅ Yangi balans: {balance}")
