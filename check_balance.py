
from bank_data import bank

def check_balance():

    print("\n========== CHECK ACCOUNT BALANCE ==========")

    accNo = int(input("Enter Account Number: "))

    if accNo in bank:

        print("Account Holder:", bank[accNo]["name"])
        print("Available Balance:", bank[accNo]["balance"])

    else:
        print("Account Not Found!")
