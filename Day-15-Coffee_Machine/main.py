
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}ml")
    print(f"Money: ${profit}")


def process_coins(quarters, dimes, nickles, pennies):
    total = 0.25 * float(quarters) + 0.10 * float(dimes) + 0.05 * float(nickles) + 0.01 * float(pennies)
    return total


def is_ingredient_sufficient(order_item):
    if order_item["ingredients"]["water"] > resources["water"]:
        print("sorry not enough water")
        return False
    elif order_item["ingredients"]["milk"] > resources["milk"]:
        print("sorry not enough milk")
        return False
    elif order_item["ingredients"]["coffee"] > resources["coffee"]:
        print("sorry not enough coffee")
        return False
    return True


def process_order(order_item):
    global profit

    # don't know why I functioned this, but ok:
    is_sufficient = is_ingredient_sufficient(order_item)
    if not is_sufficient:
        return

    order_name = ""
    if order_item["cost"] == 1.5:
        order_name = "espresso"
    elif order_item["cost"] == 2.5:
        order_name = "latte"
    else:
        order_name = "cappuccino"

    print("Insert coins-")
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")

    total_cost = process_coins(quarters, dimes, nickles, pennies)
    if total_cost < order_item["cost"]:
        print("Sorry, not enough money")
    else:
        resources["water"] -= order_item["ingredients"]["water"]
        resources["milk"] -= order_item["ingredients"]["milk"]
        resources["coffee"] -= order_item["ingredients"]["coffee"]
        change = total_cost - order_item["cost"]
        profit += order_item["cost"]
        print(f"Here is your {order_name}!, Enjoy!")
        print(f"Here is ${change} dollars in change.")


is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        is_on = False
    elif order == "report":
        print_report()
    else:
        process_order(MENU[order])

print("Thank you for coming!")