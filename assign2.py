"""
**********************************
CS 1026 - Assignment 2 – Movie Ticket Booking System
Code by: Megan Kim
Student ID: mkim945
File created: February 27, 2025
**********************************
This file implements a Movie Ticket Booking System that allows users to purchase tickets and concessions,
applies discounts based on membership and family packages, calculates applicable taxes, and outputs
the final total amount payable.
"""

import random  # Importing the random module to select daily specials

# Constants - Ticket prices
REGULAR_TICKET = 14.99
THREE_D_TICKET = 17.99
IMAX_TICKET = 19.99
CHILDREN_TICKET = 8.99
SENIOR_TICKET = 10.99

# Constants - Concession prices
SMALL_POPCORN = 6.99
MEDIUM_POPCORN = 8.99
LARGE_POPCORN = 10.99
SMALL_DRINK = 4.99
MEDIUM_DRINK = 5.99
LARGE_DRINK = 6.99
CANDY = 4.50
NACHOS = 7.99
HOT_DOG = 6.99

# Discount and tax rates
MEMBER_DISCOUNT = 0.15  # 15% discount for members
FAMILY_PACKAGE_DISCOUNT = 0.10  # 10% discount for purchases of 4 or more tickets
ONLINE_BOOKING_FEE = 1.50  # Fixed online booking fee
TAX_RATE = 0.13  # 13% tax rate

# Dictionary mappings for ticket prices
TICKET_PRICES = {
    "regular": REGULAR_TICKET,
    "3d": THREE_D_TICKET,
    "imax": IMAX_TICKET,
    "children": CHILDREN_TICKET,
    "senior": SENIOR_TICKET
}

# Dictionary mappings for concession prices
CONCESSION_PRICES = {
    "popcorn": {"small": SMALL_POPCORN, "medium": MEDIUM_POPCORN, "large": LARGE_POPCORN},
    "drinks": {"small": SMALL_DRINK, "medium": MEDIUM_DRINK, "large": LARGE_DRINK},
    "candy": CANDY,
    "nachos": NACHOS,
    "hot dog": HOT_DOG
}

# List of daily special items
DAILY_SPECIALS = ["candy", "nachos", "hot dog"]

def validate_input(category, type_value):
    """
    Validates user input for movie ticket and concession categories.
    :param category: (str) The category type - 'movie tickets' or 'concessions'.
    :param type_value: (str) The specific type of ticket or concession item.
    :return: (bool) True if the input is valid, False otherwise.
    """
    category = category.strip().lower()
    type_value = type_value.strip().lower()
    if category == "movie tickets" and type_value in TICKET_PRICES:
        return True
    if category == "concessions" and (type_value in CONCESSION_PRICES or type_value == "daily special"):
        return True
    return False

def calculate_ticket_cost(ticket_type, quantity):
    """
    Calculates the total cost for a given number of tickets.
    :param ticket_type: (str) The type of movie ticket.
    :param quantity: (int) Number of tickets.
    :return: (float) Total cost or -1 if ticket type is invalid.
    """
    ticket_type = ticket_type.strip().lower()
    if ticket_type in TICKET_PRICES:
        return round(TICKET_PRICES[ticket_type] * quantity, 2)
    return -1

def calculate_concession_cost(concession_type, quantity, size=None):
    """
    Calculates the total cost of concession items based on type, quantity, and size if applicable.
    :param concession_type: (str) Type of concession item.
    :param quantity: (int) Number of concession items.
    :param size: (str, optional) Size of item (small, medium, large).
    :return: (float) Total cost or -1 if invalid input.
    """
    concession_type = concession_type.strip().lower()
    if concession_type in ["popcorn", "drinks"]:
        size = size.strip().lower()
        if size in CONCESSION_PRICES[concession_type]:
            return round(CONCESSION_PRICES[concession_type][size] * quantity, 2)
        return -1
    elif concession_type in CONCESSION_PRICES:
        return round(CONCESSION_PRICES[concession_type] * quantity, 2)
    return -1

def apply_discount(subtotal, number_of_tickets):
    """
    Applies the best discount available based on membership or family package.
    :param subtotal: (float) The current subtotal before tax.
    :param number_of_tickets: (int) Number of tickets purchased.
    :return: (float) The discounted subtotal.
    """
    membership = input("Are you a member? (y/n): ").strip().lower()
    member_discount = MEMBER_DISCOUNT if membership == "y" else 0
    family_discount = FAMILY_PACKAGE_DISCOUNT if number_of_tickets >= 4 else 0
    best_discount = max(member_discount, family_discount)
    return round(subtotal * (1 - best_discount), 2)

def calculate_tax(subtotal):
    """
    Calculates the tax on the given subtotal.
    :param subtotal: (float) The subtotal before tax.
    :return: (float) The tax amount.
    """
    return round(subtotal * TAX_RATE, 2)

def get_daily_special():
    """
    Selects a random daily special from the list.
    :return: (str) The selected daily special item.
    """
    return random.choice(DAILY_SPECIALS)

def main():
    """
    Main function that handles user input, calculates totals, applies discounts and prints the final amount.
    """
    subtotal = 0
    ticket_count = 0
    while True:
        choice = input("Would you like to order Movie Tickets, Concessions, or type done to finish?: ").strip().lower()
        if choice == "done":
            break
        if choice == "movie tickets":
            ticket_type, quantity = ticket_option()
            subtotal += calculate_ticket_cost(ticket_type, quantity)
            ticket_count += quantity
        elif choice == "concessions":
            concession_type, quantity, size = concessions_option()
            subtotal += calculate_concession_cost(concession_type, quantity, size)
        else:
            print("Invalid category type. Please try again.")
    
    if subtotal == 0:
        print("You don't seem to have ordered anything.")
        return
    
    subtotal = apply_discount(subtotal, ticket_count)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax + ONLINE_BOOKING_FEE, 2)
    
    print(f"Subtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nOnline Booking Fee: ${ONLINE_BOOKING_FEE:.2f}\nTotal: ${total:.2f}")

if __name__ == "__main__":
    main()
