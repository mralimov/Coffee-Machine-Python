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
