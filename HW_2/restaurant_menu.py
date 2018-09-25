menu = {}

while True:
    dish_name = input("What's on the menu today: ")
    dish_price = input("What's the price of " + dish_name + "? ")
    menu[dish_name] = dish_price
    print(dish_name + " has been added to the menu")

    another_item = input("Add another item to the menu? (y/n) ")

    if another_item.lower() == "n":
        print("Menu is ready")
        break

with open('restaurant_menu.txt', 'w+') as file:
    for food in menu:
        file.write("%s, %s \n" % (food, menu[food]))
