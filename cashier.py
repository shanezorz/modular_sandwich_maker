class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        try:
            dollars = int(input("How many dollars?: ")) * 1.00
            halfDollars = int(input("How many half dollars?: ")) * 0.50
            quarters = int(input("How many quarters?: ")) * 0.25
            nickels = int(input("How many nickels?: ")) * 0.05
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return 0

        total = dollars + halfDollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
