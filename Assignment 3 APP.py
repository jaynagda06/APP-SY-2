class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Payment:
    def __init__(self, method):
        self.method = method

    def pay(self, amount):
        self.method.pay(amount)

choice = input("Enter payment method (card/upi): ")
amount = int(input("Enter amount: "))

if choice == "card":
    p = Payment(CreditCard())
else:
    p = Payment(UPI())

p.pay(amount)
