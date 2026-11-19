
from bank_data import bank

def update_account():

    print("\n========== UPDATE ACCOUNT DETAILS ==========")

    accNo = int(input("Enter Account Number: "))

    if accNo in bank:

        print("1. Update Name")
        print("2. Update Mobile Number")
        print("3. Update Address")

        choice = int(input("Enter Your Choice: "))

        match choice:

            case 1:
                name = input("Enter Updated Name: ")
                bank[accNo]["name"] = name
                print("Name Updated Successfully!")

            case 2:
                mobile = input("Enter Updated Mobile Number: ")
                bank[accNo]["mobile"] = mobile
                print("Mobile Number Updated Successfully!")

            case 3:
                address = input("Enter Updated Address: ")
                bank[accNo]["address"] = address
                print("Address Updated Successfully!")

            case _:
                print("Invalid Update Choice!")

    else:
        print("Account Not Found!")
