
from bank_data import bank

def deposit_money():

    print("\n========== DEPOSIT MONEY ==========")

    accNo = int(input("Enter Account Number: "))

    if accNo in bank:

        amount = float(input("Enter Deposit Amount: "))

        if amount > 0:

            bank[accNo]["balance"] += amount

            print("Money Deposited Successfully!")
            print("Updated Balance:", bank[accNo]["balance"])

        else:
            print("Deposit Amount Must Be Greater Than Zero!")

    else:
        print("Account Not Found!")
