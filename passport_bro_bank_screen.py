def passport_bros_bank_product():
    ronald_mcdonald = {'balance': 100000, 'authenticated': False}

    def opening_message_user_sees():
        print("\nHey! Welcome to Passport Bros Bank! ")
        print("1. Check Your Cash Balance")
        print("2. Deposit Cash Into Your Bank Account")
        print("3. Withdraw Cash From Your Bank Account")
        print("4. Terminate Your Current Bank Session")

    def check_your_cash_balance():
        print(f"\nYour current balance is: ${ronald_mcdonald['balance']}")

    def deposit_cash_into_your_bank_account():
        while True:
            try:
                amount = float(input("\nEnter amount to deposit your cash: $"))
                if amount > 0:
                    ronald_mcdonald['balance'] += amount
                    print(f"Deposit successful! Your new cash balance is ${ronald_mcdonald['balance']}")
                    break
                else:
                    print("Please enter a valid positive number. Numbers less than zero are invalid!")
            except ValueError:
                print("Invalid input. I don't you entered an actual number. Please enter a number Ronald.")

    def withdraw_cash_from_your_bank_account():
        while True:
            try:
                amount = float(input("\nEnter amount to withdraw cash: $"))
                if amount > 0:
                    if amount <= ronald_mcdonald['balance']:
                        ronald_mcdonald['balance'] -= amount
                        print(f"Withdrawal successful! Your new balance is ${ronald_mcdonald['balance']}")
                        break
                    else:
                        print("Request Declined! Ronald, You Have Insufficient funds.")
                else:
                    print("Please enter a valid positive number. Numbers less than zero are invalid!")
            except ValueError:
                print("Invalid input. I don't you entered an actual number. Please enter a number Ronald.")

    def authenticate_bank_user():
        while ronald_mcdonald['authenticated'] == False:
            password = input("Enter your bank password: ")
            if password == "freedom1": 
                print("Authentication successful!")
                ronald_mcdonald['authenticated'] = True
            else:
                print("Incorrect password. Try again.")

    authenticate_bank_user()
    while True:
        opening_message_user_sees()
        try:
            selection = int(input("\nHi Ronald! Please select an option from [1-4]: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if   selection == 1:
            check_your_cash_balance()
        elif selection == 2:
            deposit_cash_into_your_bank_account()
        elif selection == 3:
            withdraw_cash_from_your_bank_account()
        elif selection == 4:
            print("\nThank you for using Passport Bros bank. See you later and enjoy your next trip!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

passport_bros_bank_product()
