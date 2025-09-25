# 🏦 Simple ATM Simulation (Python)

Author : M.S.MEYSINTHA

A beginner-friendly Python program that simulates the basic operations of an ATM machine.
It allows the user to check balance, deposit money, withdraw money, and exit the system.

# 📌 Features

✅ Check Balance – view your current account balance
✅ Deposit – add money to your balance
✅ Withdraw – withdraw money with balance validation
✅ Exit – quit the ATM system safely
✅ Looped Menu – keeps running until the user exits

# 📜 Code Example
def atm():
    balance = 1000  # initial balance
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

# ▶️ Example Run
ATM Menu
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter choice: 1
Balance: 1000

ATM Menu
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter choice: 2
Enter amount to deposit: 500
Deposited. New balance: 1500

# ⚡ How to Run

Clone this repository:

git clone https://github.com/meysiii/SIMPLE-ATM-SIMULATION
cd simple-atm-simulation


# Run the program:

python atm.py

# output

<img width="1920" height="1030" alt="Image" src="https://github.com/user-attachments/assets/a2e1810a-44c5-49bb-ae89-55423d59c30c" />

# 🚀 Future Improvements

Add PIN verification for security

Save transaction history in a file (mini passbook)

Add daily withdrawal limit

Create a GUI version using Tkinter or Streamlit
