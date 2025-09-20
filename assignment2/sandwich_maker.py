
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, required in ingredients.items():
            if self.machine_resources.get(item, 0) < required:
                print(f"We do not have {item}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
        for item, amount in sandwich_size.items():
            self.machine_resources[item] -= amount
        print(f"Here is your {sandwich_size} sandwich.")