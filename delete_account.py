
from bank_data import bank

def delete_account():

    print("\n========== DELETE BANK ACCOUNT ==========")

    accNo = int(input("Enter Account Number to Delete: "))

    if accNo in bank:

        confirm = input(
            "Are you sure you want to delete this account? (yes/no): "
        )

        if confirm.lower() == "yes":

            del bank[accNo]

            print("Bank Account Deleted Successfully!")

        else:
            print("Account Deletion Cancelled!")

    else:
        print("Account Not Found!")
