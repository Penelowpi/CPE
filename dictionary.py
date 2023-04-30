items = {
    "apple": {
        "cost": 0.75,
        "quantity": 10
    },
    "banna": {
        "cost": 1.25,
        "quantity": 5
    },
    "orange": {
        "cost": 0.9,
        "quantity": 8
    }
}


def check_if_item_exist(item):
    if items.get(item) is None:
        return False
    else:
        return True


def add_item(item, cost, quantity):

    if items.get(item) is not None:  # Ignore if item does exist
        return

    # Add item if item does not exist
    items[item] = {"cost": cost, "quantity": quantity}


def print_item(item):
    print(f"{item} exists in the dictionary")
    cost = items[item]['cost']
    quantity = items[item]['quantity']
    print(f"Cost: {cost}, Quantity: {quantity}")


while True:

    print("Check if an item exists in the dictionary")
    item = input("Enter item you want to check: ")

    item_exist = check_if_item_exist(item) is True
    item_dont_exist = check_if_item_exist(item) is False

    if item_exist:
        print_item(item)
    elif item_dont_exist:
        print("\nAdd a new item to the dictionary")

        item = input("Enter new item you want to add: ")
        cost = input("Enter cost of new item: ")
        quantity = input("Enter quantity of new item: ")

        add_item(item, cost, quantity)

    print("\n")
