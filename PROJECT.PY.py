def main_menu():
    print("\n*** Welcome to our Book Store ***")
    print("------Select Branch------")
    print("1 Dehradun Branch")
    print("2 Himachal Branch")
    print("3 Arunachal Branch")
    print("4 Kashmir Branch")
    print("5 Jaysingpur Branch")
    print("6 Exit")

def branch_menu(branch_name):
    book_charges = 0
    while True:
        print(f"\n** Welcome To OUR Book Store - {branch_name} **")
        print("1 Browse Books")
        print("2 View Bill")
        print("3 Exit to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            book_charges += books()
        elif choice == '2':
            bill(book_charges)
            break
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def books():
    menu = {
        '1': ('The Alchemist (Fiction)', 250),
        '2': ('Atomic Habits (Self-help)', 300),
        '3': ('Python Programming (Academic)', 450),
        '4': ('Mahabharata for Children (Comics)', 200),
        '5': ('Rich Dad Poor Dad (Finance)', 280),
        '6': ('Wings of Fire (Biography)', 350),
        '7': ('Ikigai (Philosophy)', 260),
        '8': ('Think and Grow Rich (Motivation)', 230),
    }
    total = 0
    while True:
        print("\n--- Available Books ---")
        for key, (title, price) in menu.items():
            print(f"{key}. {title} - Rs. {price}")
        print("0. Finish Order")
        choice = input("Enter book number: ")
        if choice == '0':
            break
        elif choice in menu:
            qty_input = input("Enter quantity: ")
            if qty_input.isdigit():
                qty = int(qty_input)
                total += menu[choice][1] * qty
            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Invalid choice.")
    if total > 0:
        print(f"Books selected. Charges: Rs.{total}")
    else:
        print("No books selected.")
    return total

def bill(book_charges):
    if book_charges > 0:
        print(f"\nTotal Bill: Rs. {book_charges}")
        payment(book_charges)
    else:
        print("No charges to pay.")

def payment(amount):
    print("\n--- Payment Options ---")
    print("1. Cash")
    print("2. Credit/Debit Card (10% discount)")
    print("3. UPI")
    choice = input("Select payment method: ")
    if choice == "1":
        print(f"Payment of Rs.{amount} received in CASH. Thank you!")
        exit()
    elif choice == "2":
        discount = amount * 0.10
        discounted_amount = amount - discount
        print(f"10% discount applied. You saved Rs.{discount:.2f}")
        print(f"Payment of Rs.{discounted_amount:.2f} received via CARD. Thank you!")
        exit()
    elif choice == "3":
        print(f"Payment of Rs.{amount} received via UPI. Thank you!")
        exit()
    else:
        print("Invalid payment method.")

def main():
    branches = {
        '1': 'Dehradun',
        '2': 'Himachal',
        '3': 'Arunachal',
        '4': 'Kashmir',
        '5': 'Jaysingpur'
    }
    while True:
        main_menu()
        choice = input("Select a branch: ")
        if choice in branches:
            branch_menu(branches[choice])
        elif choice == '6':
            print("Thank you for visiting our Book Store. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

main()
