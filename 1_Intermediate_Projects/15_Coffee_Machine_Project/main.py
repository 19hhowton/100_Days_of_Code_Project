from coffee_data import MENU, resources

def process_coins():
    """Returns the sum of inserted coins."""
    print("Please insert coins.")
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")
    wallet = (int(quarters) * .25) + (int(dimes) * .10) + (int(nickles) * .25) + (int(pennies) * .01)
    return wallet

def check_money(wallet):
    """Return True when payment is accepted, False if money is insufficient."""
    if MENU[selection]['cost'] > wallet:
        print(f"“Sorry that's not enough money for {selection}. Money refunded.")
        return False
    if 'money' not in resources:
        resources['money'] = MENU[selection]['cost']
    else:
        resources['money'] += MENU[selection]['cost']
    change = wallet - MENU[selection]['cost']
    if change > 0:
        print("Here is ${:0.2f} dollars in change.".format(change))
    return True

# def check_resources(selection):
#     """A function to check that there are sufficient resources available. 
#     Returns True if there are sufficient resources."""
#     if resources['water'] < MENU[selection]['ingredients']['water']:
#         print("Sorry, there is not enough water in the machine.")
#         return False
#     if resources['coffee'] < MENU[selection]['ingredients']['coffee']:
#         print("Sorry, there is not enough coffee in the machine.")
#         return False
#     if 'milk' in MENU[selection]['ingredients']: 
#         if resources['milk'] < MENU[selection]['ingredients']['milk']:
#             print("Sorry, there is not enough milk in the machine.")
#             return False
#     return True

def check_resources(selection):
    """IMPROVED: Using a for loop instead of multiple if statements.
    Returns True if there are sufficient resources."""
    for items in MENU[selection]['ingredients']:
        if MENU[selection]['ingredients'][items] > resources[items]:
            print(f"Sorry, there is not enough {items} in the machine.")
            return False
    return True

# def make_coffee(selection):
#     """A function to 'make coffee' by subtract the resources"""
#     resources['water'] = resources['water'] - MENU[selection]['ingredients']['water']
#     resources['coffee'] = resources['coffee'] - MENU[selection]['ingredients']['coffee']
#     if 'milk' in MENU[selection]['ingredients']: 
#         resources['milk'] = resources['milk'] - MENU[selection]['ingredients']['milk']

def make_coffee(selection):
    """IMPROVED: Using a for loop instead of multiple if statements.
    Returns nothing. Subtracts reduction in resources"""
    for items in MENU[selection]['ingredients']:
        resources[items] = resources[items] - MENU[selection]['ingredients'][items]

def process_selection(selection):
    if selection == "report":
        print(resources)
    else:
        wallet = process_coins()
        if check_money(wallet) and check_resources(selection):
            make_coffee(selection)
            print(f"Enjoy your {selection}!")

machine_on = True
while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ") 
    if selection == 'off':
        machine_on = False
    else:
        process_selection(selection)

