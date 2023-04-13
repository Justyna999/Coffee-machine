MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough{item}.")
            return False
    return True


def printer_makes_brr(drink_cost, total):
    print(f"Payed so far: {total}$")
    if drink_cost - total <0:
        debt = 0
    else:
        debt = drink_cost - total
    print(f"Remaining debt: {debt}$")


def process_coins(drink_cost, drink_type):
    print(f"cost of {drink_type} : {drink_cost} $. Please insert coins.")
    total = int(input("How many quarters (0.25$)?: ")) * 0.25
    printer_makes_brr(drink_cost, total)
    total += int(input("How many dimes (0.1$)?: ")) * 0.1
    printer_makes_brr(drink_cost, total)
    total += int(input("How many nickles (0.05$)?: ")) * 0.05
    printer_makes_brr(drink_cost, total)
    total += int(input("How many pennies (0.01$)?: ")) * 0.01
    return total


def is_transactional_successful(money_received, drink_cost):

    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}. Enjoy!")


is_on = True
choices = ["espresso", "latte", "cappuccino"]
while is_on:
    choice = input("What would you like? (espresso press 1 / latte press 2 / cappuccino press 3): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice.isdigit() and int(choice) in range(1, 4):
        choice_int = int(choice)
        choice_new = choices[choice_int-1]
        drink = MENU[choice_new]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins(drink["cost"], choice_new)
            if is_transactional_successful(payment, drink["cost"]):
                make_coffee(choice_new, drink["ingredients"])
