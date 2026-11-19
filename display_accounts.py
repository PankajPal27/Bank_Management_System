
from bank_data import bank

def display_accounts():

    print("\n========== DISPLAY ALL ACCOUNTS ==========")

    if len(bank) == 0:
        print("No Bank Accounts Available")

    else:
        for accNo, accDetails in bank.items():

            print("Account Number:", accNo)
            print("Account Holder:", accDetails["name"])
            print("Age:", accDetails["age"])
            print("Mobile:", accDetails["mobile"])
            print("Address:", accDetails["address"])
            print("Balance:", accDetails["balance"])
            print("=" * 40)
