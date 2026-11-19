from create_account import create_account
from display_accounts import display_accounts
from search_account import search_account
from deposit_money import deposit_money
from withdraw_money import withdraw_money
from check_balance import check_balance
from update_account import update_account
from delete_account import delete_account


# ================= MAIN MENU =================

while True:

    print("\n==============================================")
    print("           BANK MANAGEMENT SYSTEM")
    print("==============================================")

    print("1. Create Bank Account")
    print("2. Display All Accounts")
    print("3. Search Bank Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Check Account Balance")
    print("7. Update Account Details")
    print("8. Delete Bank Account")
    print("9. Exit")

    try:
        choice = int(input("\nEnter Your Choice: "))

        match choice:

            case 1:
                create_account()

            case 2:
                display_accounts()

            case 3:
                search_account()

            case 4:
                deposit_money()

            case 5:
                withdraw_money()

            case 6:
                check_balance()

            case 7:
                update_account()

            case 8:
                delete_account()

            case 9:
                print("\nThank You for Using Bank Management System!")
                break

            case _:
                print("Invalid Choice! Please Select 1 to 9.")

    except ValueError:
        print("Invalid Input! Please Enter a Valid Number.")
