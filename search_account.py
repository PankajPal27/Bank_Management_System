
from bank_data import bank

def search_account():

    print("\n========== SEARCH ACCOUNT ==========")

    accNo = int(input("Enter Account Number to Search: "))

    if accNo in bank:

        print("Account Found Successfully!")

        print("Account Number:", accNo)
        print("Account Holder:", bank[accNo]["name"])
        print("Age:", bank[accNo]["age"])
        print("Mobile:", bank[accNo]["mobile"])
        print("Address:", bank[accNo]["address"])
        print("Balance:", bank[accNo]["balance"])

    else:
        print("Account Not Found!")
