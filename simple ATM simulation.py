def atm():
    balance = 1000
    while True:
        print("\nATM Menu")
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Balance:", balance)
        elif choice == 2:
            amt = float(input("Enter amount to deposit: "))
            balance += amt
            print("Deposited. New balance:", balance)
        elif choice == 3:
            amt = float(input("Enter amount to withdraw: "))
            if amt <= balance:
                balance -= amt
                print("Withdrawn. New balance:", balance)
            else:
                print("Insufficient funds")
        elif choice == 4:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")

atm()
