
from bank_data import bank

def create_account():

    print("\n========== CREATE BANK ACCOUNT ==========")

    accNo = int(input("Enter Account Number: "))

    if accNo in bank:
        print("Account Number already exists!")

    else:
        name = input("Enter Account Holder Name: ")
        age = int(input("Enter Account Holder Age: "))
        mobile = input("Enter Mobile Number: ")
        address = input("Enter Address: ")
        balance = float(input("Enter Initial Deposit Amount: "))

        if balance < 0:
            print("Initial deposit cannot be negative!")
            return

        bank[accNo] = {
            "accNo": accNo,
            "name": name,
            "age": age,
            "mobile": mobile,
            "address": address,
            "balance": balance
        }

        print("Bank Account Created Successfully!")
