import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources, recipes)
cashier_instance = Cashier()


def main():
    machine = SandwichMaker(resources, recipes)

    while True:
        action = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if action == 'off':
            print("Machine turned off.")
            break

        elif action == 'report':
            machine.report()

        elif action in machine.recipes:
            order_ingredients = machine.recipes[action]["ingredients"]
            cost = machine.recipes[action]["cost"]

            # Check resources
            if machine.check_resources(order_ingredients):
                print("Please insert coins.")
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    machine.make_sandwich(action, order_ingredients)
                else:
                    print("Transaction failed. Returning to menu.")
            else:
                shortage = [ingredient for ingredient, amount in order_ingredients.items() if
                            ingredient != 'cost' and machine.machine_resources.get(ingredient, 0) < amount]
                print(f"Sorry there is not enough {', '.join(shortage)}.")

        else:
            print("Invalid selection. Please choose a valid option.")


if __name__ == "__main__":
    main()
