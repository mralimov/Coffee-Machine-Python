from data import MENU, resources

balance = 0

off_button = False


def order_coffee(order):
    """Returns True if ingredients are sufficient otherwise returns False"""
    for el in order:
        if order[el] >= resources[el]:
            print(f"Sorry there is not enough {el}")
            return False
        else:
            return True


def calc_money_inserted(money_inserted, cost):
    """Returns True if there coins inserted enough to buy"""
    if money_inserted >= cost:
        change = round(money_inserted - cost, 2)
        print(f"Here is your ${change} in change")
        global balance
        balance += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def calc_money():
    """ Returns total coins inserted """
    print("Please insert coins.")
    quarters = int(input("how many quarters?:  ")) * 0.25
    dimes = int(input("how many dimes?:  ")) * 0.1
    nickles = int(input("how many nickles?:  ")) * 0.05
    pennies = int(input("how many pennies?:  ")) * 0.01
    total_coins_inserted = quarters + dimes + nickles + pennies
    return total_coins_inserted


def make_coffee(drink_name, drink_ordered):
    for item in drink_ordered:
        resources[item] -= drink_ordered[item]
    print(f"Here is your {drink_name} Enjoy!")


while not off_button:
    ask_customer = input(
        "What would you like?  (espresso/latte/cappuccino):").lower()

    if ask_customer == "off":
        off_button = True
        print("Coffee machione turning off.....")
    elif ask_customer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${round(balance, 2)}")
    elif ask_customer == "espresso" or ask_customer == "latte" or ask_customer == "cappuccino":

        drink = MENU[ask_customer]
        total_inserted = calc_money()

        if order_coffee(drink["ingredients"]):
            if calc_money_inserted(total_inserted, drink["cost"]):
                make_coffee(ask_customer, drink["ingredients"])
                print(
                    f"Here is the total balance in account {round(balance, 2)}")

    else:
        print("Sorry, please type in correct name of the drink. Thank you!")

while not off_button:
    ask_customer = input(
        "What would you like?  (espresso/latte/cappuccino):").lower()

    if ask_customer == "off":
        off_button = True
        print("Coffee machione turning off.....")
    elif ask_customer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${round(balance, 2)}")
    elif ask_customer == "espresso" or ask_customer == "latte" or ask_customer == "cappuccino":

        drink = MENU[ask_customer]
        total_inserted = calc_money()

        if order_coffee(drink["ingredients"]):
            if calc_money_inserted(total_inserted, drink["cost"]):
                make_coffee(ask_customer, drink["ingredients"])
                print(
                    f"Here is the total balance in account {round(balance, 2)}")

    else:
        print("Sorry, please type in correct name of the drink. Thank you!")
