class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class DebitCard:
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


print("Select Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    method = CreditCard()
elif choice == 2:
    method = DebitCard()
elif choice == 3:
    method = UPI()
else:
    print("Invalid choice")
    exit()

payment = Payment(method)
payment.process_payment(amount)
