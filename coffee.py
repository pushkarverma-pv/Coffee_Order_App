class Coffee:
    # initialize coffee with name and price
    def __init__(self, name, price):

        self.name = name
        self.price = price


class Order:
    # initialize order with empty list
    def __init__(self):
        self.items = []

    # add coffee to order
    def add_item(self, coffee):

        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    # calculate total price
    def total(self):
        return sum(item.price for item in self.items)

    # show order summary
    def show_order(self):

        if not self.items:
            print("\nNothing ordered yet.\n")
            return

        print("\nYour Order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ₹{item.price}")
        print(f"Total: ₹{self.total()}\n")

    # checkout process
    def checkout(self):
        if not self.items:
            print("\nYour cart is empty.\n")
            return
        

        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()


        if confirm == 'yes':
            print("\nOrder confirmed! Arigato \n")
            self.items.clear()

        else:
            print("\nCheckout cancelled.\n")


def show_menu(menu):

    print("\n--- Coffee Menu ---")

    for i, coffee in enumerate(menu, 1):
        print(f"{i}. {coffee.name} - ₹{coffee.price}")
    print("5. View order")
    print("6. Checkout")
    print("7. Exit")


def main():

    menu = [
        Coffee("Espresso", 40),
        Coffee("Latte", 80),
        Coffee("Cappuccino", 70),
        Coffee("Americano", 60),
        Coffee("Filter Coffee", 50)
    ]

    order = Order()

    while True:
        show_menu(menu)

        choice = input("Choose an option: ")


        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) - 1])

        elif choice == '5':
            order.show_order()
            input("Press Enter to return to menu...")

        elif choice == '6':
            order.checkout()
            input("Press Enter to return to menu...")

        elif choice == '7':
            print("\nThanks for visiting. See you next time!\n")
            break

        else:
            print("\nInvalid choice. Try again.\n")


if __name__ == "__main__":
    main()


