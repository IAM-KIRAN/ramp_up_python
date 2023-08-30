class ATM:
    def __init__(self):
        self.notes = {500: 0, 200: 0, 50: 0}

    def start(self):
        self.notes = {500: 0, 200: 0, 50: 0}  # Reset notes data
        amount = int(input("Enter the amount to withdraw: "))
        self.withdraw(amount)

    def withdraw(self, amount):
        if amount % 50 != 0 or amount < 50:
            print("Invalid amount. Amount should be a multiple of 50 and at least 50.")
            self.start()  # Ask for input again
            #return

        remaining_amount = amount

        for note in [500, 200, 50]:
            if remaining_amount >= note:                        #1250
                self.notes[note] = remaining_amount // note     #1250//500 =2.5 ==2
                remaining_amount %= note                        #1250%500 = 250

        self.display_notes()
        self.ask_continue_cancel()

    def display_notes(self):
        print("Notes distribution:")
        for note, count in self.notes.items():
            if count > 0:
                print(f"{note} notes : {count}")

    def ask_continue_cancel(self):
        choice = input("Do you want to continue (C) or cancel (X)? ").upper()
        if choice == "C":
            self.start()
        elif choice == "X":
            print("Transaction cancelled.")
        else:
            print("Invalid choice. Please enter 'C' to continue or 'X' to cancel.")
            self.ask_continue_cancel()


atm = ATM()
atm.start()
