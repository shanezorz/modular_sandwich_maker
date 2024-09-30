class SandwichMaker:
    def __init__(self, resources, recipes):
        self.machine_resources = resources
        self.recipes = recipes

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if ingredient != 'cost' and self.machine_resources.get(ingredient, 0) < amount:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            if ingredient != 'cost':
                self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

    def report(self):
        print("Current resources:")
        for ingredient, amount in self.machine_resources.items():
            print(f"{ingredient.capitalize()}: {amount}")