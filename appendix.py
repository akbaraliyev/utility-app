# Dictionary with stock added
vending_items = {
    "A1": {"name": "Cola", "category": "Drink", "price": 1.50, "stock": 3},
    "A2": {"name": "Pepsi", "category": "Drink", "price": 1.40, "stock": 2},
    "B1": {"name": "Chips", "category": "Snack", "price": 1.00, "stock": 5},
    "B2": {"name": "Chocolate Bar", "category": "Snack", "price": 1.20, "stock": 0},  # Out of stock example
    "C1": {"name": "Water", "category": "Drink", "price": 1.00, "stock": 4},
}

# Display the menu of available items
def display_menu():
    print("\n=== VENDING MACHINE MENU ===")
    for code, item in vending_items.items():
        status = "OUT OF STOCK" if item["stock"] == 0 else f"${item['price']:.2f}"
        print(f"{code}: {item['name']} ({item['category']}) - {status}")

# Get user selection and validate code and stock
def get_user_selection():
    code = input("\nEnter the item code of your selection: ").upper()
    if code in vending_items:
        if vending_items[code]["stock"] > 0:
            return code
        else:
            print("Sorry, that item is out of stock.")
            return get_user_selection()
    else:
        print("Invalid code. Please try again.")
        return get_user_selection()

# Handle user payment and return change if needed
def process_payment(price):
    print(f"\nPlease insert ${price:.2f}")
    inserted = 0.0
    while inserted < price:
        try:
            amount = float(input(f"Inserted so far: ${inserted:.2f}. Insert money: $"))
            if amount <= 0:
                print("Please insert a positive amount.")
            else:
                inserted += amount
        except ValueError:
            print("Invalid input. Please enter a number.")
    return inserted - price

# Dispense item, handle stock, show change and confirmation
def dispense_item(code):
    item = vending_items[code]
    print(f"\nYou selected: {item['name']} - ${item['price']:.2f}")
    change = process_payment(item['price'])

    if change > 0:
        print(f"Change returned: ${change:.2f}")
    else:
        print("No change to return.")

    # Reduce item stock
    vending_items[code]["stock"] -= 1

    print(f"{item['name']} has been successfully dispensed.")
    print("Thank you for your purchase!")

# Main program loop
def main():
    while True:
        display_menu()
        code = get_user_selection()
        dispense_item(code)
        again = input("\nWould you like to make another purchase? (yes/no): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
