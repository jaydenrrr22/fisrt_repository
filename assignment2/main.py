import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    machine = SandwichMaker(resources)
    cashier = Cashier()

    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")

        if choice == "off":
            break
        elif choice == "report":
            print(f"Bread: {machine.machine_resources['bread']} slice(s)")
            print(f"Ham: {machine.machine_resources['ham']} slice(s)")
            print(f"Cheese: {machine.machine_resources['cheese']} pound(s)")
        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]
            if machine.check_resources(ingredients):
                coins = cashier.process_coins()
                if cashier.transaction_result(coins, cost):
                    machine.make_sandwich(choice, ingredients)
        else:
            print("Invalid input. Please try again.")

if __name__=="__main__":
    main()
