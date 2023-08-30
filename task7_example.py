class ATM:
    def __init__(self):
        self.denominations = [500, 200, 50]

    def calculate_notes(self, amount):
        notes_count = {}

        if amount < min(self.denominations):
            print("Error: Please enter an amount greater than or equal to the smallest denomination.")
            return

        for denomination in self.denominations:
            notes_count[denomination] = amount // denomination
            amount %= denomination

        print("Output:")
        for denomination, count in notes_count.items():
            print(f"{denomination} notes: {count}")

atm = ATM()

while True:
    withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
    atm.calculate_notes(withdrawal_amount)

    choice = input("Do you want to continue (y/n)? ").lower()
    if choice != 'y':
        break
