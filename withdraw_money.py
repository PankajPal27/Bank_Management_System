
from bank_data import bank

def withdraw_money():

    print("\n========== WITHDRAW MONEY ==========")

    accNo = int(input("Enter Account Number: "))

    if accNo in bank:

        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            print("Withdrawal Amount Must Be Greater Than Zero!")

        elif amount <= bank[accNo]["balance"]:

            bank[accNo]["balance"] -= amount

            print("Money Withdrawn Successfully!")
            print("Remaining Balance:", bank[accNo]["balance"])

        else:
            print("Insufficient Balance!")

    else:
        print("Account Not Found!")
