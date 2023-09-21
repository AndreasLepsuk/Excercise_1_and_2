import json

def load_menu_from_file():
    try:
        with open("cafemenu.json", 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_menu_to_file(cafemenu, menu):
    with open(cafemenu, 'w', encoding='utf-8') as file:
        json.dump(menu, file, indent=4)

def add_menu(menu, name, price):
    menu[name] = price
    return menu

def update_menu(menu, name, new_price):
    if name in menu:
        menu[name] = new_price
        return menu
    else:
        return None

def delete_menu(menu, name):
    if name in menu:
        del menu[name]
        return menu
    else:
        return None

def display_menu(menu, sort_alphabetically=True):
    sorted_menu = sorted(menu.items(), key=lambda item: item[0].lower() if sort_alphabetically else item[1], reverse=not sort_alphabetically)
    for name, price in sorted_menu:
        print(f"{name}: €{price}")

def search_by_name(menu, search_term):
    found_item = {}
    for name, price in menu.items():
        if search_term.lower() in name.lower():
            found_item[name] = price
    return found_item

def search_by_price(menu, price):
    closest_price = min(menu.values(), key=lambda x: abs(x - price))
    found_item = {name: price for name, price in menu.items() if price == closest_price}
    return found_item

def purchase(products):
    total = sum(products.values())
    tax_percent = 20
    tax = total * tax_percent / 100
    total_with_tax = total + tax
    return total_with_tax

def main():
    data_file = "cafemenu.json"
    data = load_menu_from_file()

    while True:
        print("\n--- Menu ---")
        print("1. Add an item to the menu")
        print("2. Update menu")
        print("3. Delete an item from the menu")
        print("4. Display menu (alphabetically)")
        print("5. Display menu (by highest price)")
        print("6. Search item by name")
        print("7. Search item by price")
        print("8. Buy")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            data = add_menu(data, name, price)
            save_menu_to_file(data_file, data)
            print(f"{name} has been added to the data.")

        elif choice == "2":
            name = input("Enter the product name to update: ")
            if name in data:
                new_price = float(input("Enter the new price: "))
                data = update_menu(data, name, new_price)
                save_menu_to_file(data_file, data)
                print(f"{name} price has been updated.")
            else:
                print(f"{name} is not in the data.")

        elif choice == "3":
            name = input("Enter the product name to delete: ")
            if name in data:
                data = delete_menu(data, name)
                save_menu_to_file(data_file, data)
                print(f"{name} has been deleted from the data.")
            else:
                print(f"{name} is not in the data.")

        elif choice == "4":
            print("Data sorted alphabetically:")
            display_menu(data, sort_alphabetically=True)

        elif choice == "5":
            print("Data sorted by highest price:")
            display_menu(data, sort_alphabetically=False)

        elif choice == "6":
            search_term = input("Enter the search term: ")
            found_data = search_by_name(data, search_term)
            print("Search results:")
            display_menu(found_data, sort_alphabetically=True)

        elif choice == "7":
            price = float(input("Enter the price to search: "))
            found_data = search_by_price(data, price)
            print("Search results:")
            display_menu(found_data, sort_alphabetically=True)

        elif choice == "8":
            cart = {}
            while True:
                name = input("Enter the product name (or 'buy' to finish): ").capitalize()
                if name.lower() == "buy":
                    break
                elif name in data:
                    if name in cart:
                        cart[name] += data[name]
                    else:
                        cart[name] = data[name]
                    print(f"{name} has been added to the cart.")
                else:
                    print(f"{name} is not in the menu.")

            total_with_tax = purchase(cart)
            print("Cart content:")
            display_menu(cart, sort_alphabetically=True)
            print(f"Total amount with tax: €{total_with_tax:.2f}")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
