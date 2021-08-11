MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def print_report(resource_available, money):
    print(f"""Water: {resource_available[0]}ml
Milk: {resource_available[1]}ml
Coffee: {resource_available[2]}g
Money: ${money}""")


def check_resources(beverage_selected, resource_available):
    """Return True when order can be made, False if ingredients are not sufficient."""
    enough_resources = True

    if MENU[beverage_selected]["ingredients"]["water"] > resource_available[0]:
        print("Sorry there is not enough water.")
        enough_resources = False
    elif MENU[beverage_selected]["ingredients"]["milk"] > resource_available[1]:
        print("Sorry there is not enough milk.")
        enough_resources = False
    elif MENU[beverage_selected]["ingredients"]["coffee"] > resource_available[2]:
        print("Sorry there is not enough coffee.")
        enough_resources = False
    return enough_resources


def process_coins(quarters, dimes, nickles, pennies):
    """Return the sum of the coins inserted by the user"""
    sum_coins = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return sum_coins


def check_transaction(sum_coin_inserted, beverage_selected):
    """Check if the user inserted enough money for the selected beverage. Return the change"""
    if sum_coin_inserted < MENU[beverage_selected]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return
    changes = sum_coin_inserted - MENU[beverage_selected]["cost"]
    return round(changes, 2)


def start():
    """Start of the program"""
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    money = 0.0
    shut_down = False

    while not shut_down:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        machine_functions = ["off", "report", "espresso", "latte", "cappuccino"]

        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        resources_available = [water, milk, coffee]

        # Check for user input
        if user_input == "off":
            shut_down = True
        elif user_input == "report":
            print_report(resources_available, money)
        elif not user_input in machine_functions:
            print("Invalid input")
        else:
            for function_selected in machine_functions:  # Check what beverage the user would like
                if user_input == function_selected:
                    if check_resources(function_selected, resources_available):  # Check if there is enough resources
                        print("Please insert coins.")
                        quarters = int(input("how many quarters?: "))
                        dimes = int(input("how many dimes?: "))
                        nickles = int(input("how many nickles?: "))
                        pennies = int(input("how many pennies?: "))
                        coins_sum = process_coins(quarters, dimes, nickles, pennies)
                        changes = check_transaction(coins_sum, user_input)  # Check if enough money inserted
                        if changes:  # Update the amount of money in the machine and the resources dictionaries
                            money += MENU[user_input]["cost"]
                            resources["water"] -= MENU[user_input]["ingredients"]["water"]
                            resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
                            resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
                            print(f"Here is ${changes} dollars in change.")
                            print(f"Here is your {user_input} ☕. Enjoy!")


start()

"""
    if user_input == "off":
        shut_down = True
    elif user_input == "report":
        print_report(resources_available)
    elif user_input == "espresso":
        check_resources("espresso", resources_available)
    elif user_input == "latte":
        check_resources("latte", resources_available)
    elif user_input == "cappuccino":
        check_resources("cappuccino", resources_available)
    else:
        print("Invalid input")
"""

"""
    for list_ingredient in resource_list:
        for resources_available in resources:
            print(resources_available)
            if resources_available < MENU[beverage_selected]["ingredients"][list_ingredient]:
                resource_is_enough = False
                print(f"Resource verifie: {list_ingredient}")
                print(f"Resource disponible {resources_available}")
                print(f'Resource nécessaire {MENU[beverage_selected]["ingredients"][list_ingredient]}')"""

"""
    resources_need = MENU[beverage_selected]["ingredients"]
    resources_needed_list = []
    enough_resources = True

    for x in resources_need:
        resources_needed_list.append(MENU[beverage_selected]["ingredients"][x])

    for y in range(0, 2):
        if resources_needed_list[y] > resource_available[y]:
            enough_resources = False

    print(f"Resource needed list: {resources_needed_list}")
    print(f"Resource available: {resource_available}")
    print(f"Assez de resource: {enough_resources}")
    return enough_resources"""
