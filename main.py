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
