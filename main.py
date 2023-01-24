from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 
coffemaker = CoffeeMaker()
myMachine  = MoneyMachine()
menu = Menu()
# myMachine.report()
# coffemaker.report()

working = True

while working:
    options = menu.get_items()
    answer = input(f"What would you like? {options}: ")
    if answer == "off":
        working = False
    elif answer == "report":
        myMachine.report()
        coffemaker.report()
    else: 
        drink = menu.find_drink(answer)
        # print(drink)
        if coffemaker.is_resource_sufficient(drink):
            if myMachine.make_payment(drink.cost):
                coffemaker.make_coffee(drink)