"""
**********************************
CS 1026 - Assignment 2 – Movie Ticket Booking System
Code by: Megan Kim
Student ID: mkim945
File created: February 27, 2025
**********************************
This file is used to calculate monthly principal and interest amounts
for a given mortgage total. It must calculate these values over X
years using projected variations in interest rates. The final function
prints out all the results in a structured table.
"""

import random

# Constants - Prices of different items available for purchase
REGULAR_TICKET = 14.99
THREE_D_TICKET = 17.99
IMAX_TICKET = 19.99
CHILDREN_TICKET = 8.99
SENIOR_TICKET = 10.99

SMALL_POPCORN = 6.99
MEDIUM_POPCORN = 8.99
LARGE_POPCORN = 10.99
SMALL_DRINK = 4.99
MEDIUM_DRINK = 5.99
LARGE_DRINK = 6.99
CANDY = 4.50
NACHOS = 7.99
HOT_DOG = 6.99

MEMBER_DISCOUNT = 0.15  # 15% discount for members
FAMILY_PACKAGE_DISCOUNT = 0.10  # 10% discount if 4 or more tickets are purchased
ONLINE_BOOKING_FEE = 1.50  # Fixed online booking fee
TAX_RATE = 0.13  # Sales tax rate

# Dictionary storing ticket prices
TICKET_PRICES = {
    "regular": REGULAR_TICKET,
    "3d": THREE_D_TICKET,
    "imax": IMAX_TICKET,
    "children": CHILDREN_TICKET,
    "senior": SENIOR_TICKET
}

# Dictionary storing concession prices
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
    Validates user input for movie tickets and concessions.
    :param category: Type of category ('movie tickets' or 'concessions')
    :param type_value: Specific item to validate
    :return: True if valid, False otherwise
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
    Calculates the total cost of movie tickets.
    :param ticket_type: Type of ticket (regular, 3d, imax, etc.)
    :param quantity: Number of tickets purchased
    :return: Total ticket cost (rounded to 2 decimal places)
    """
    ticket_type = ticket_type.strip().lower()
    if ticket_type in TICKET_PRICES:
        return round(TICKET_PRICES[ticket_type] * quantity, 2)
    return -1  # Invalid input case


def calculate_concession_cost(concession_type, quantity, size=None):
    """
    Calculates the total cost of concessions.
    :param concession_type: Type of concession (popcorn, drinks, candy, etc.)
    :param quantity: Number of items purchased
    :param size: Size of the item (small, medium, large) if applicable
    :return: Total concession cost (rounded to 2 decimal places)
    """
    concession_type = concession_type.strip().lower()
    if concession_type in ["popcorn", "drinks"]:
        size = size.strip().lower()
        if size in CONCESSION_PRICES[concession_type]:
            return round(CONCESSION_PRICES[concession_type][size] * quantity, 2)
        return -1  # Invalid size case
    elif concession_type in CONCESSION_PRICES:
        return round(CONCESSION_PRICES[concession_type] * quantity, 2)
    return -1  # Invalid input case


def apply_discount(subtotal, number_of_tickets):
    """
    Applies discounts based on membership and number of tickets purchased.
    :param subtotal: Current subtotal before discount
    :param number_of_tickets: Number of tickets purchased
    :return: Discounted subtotal
    """
    membership = input("Are you a member? (y/n): ").strip().lower()
    member_discount = MEMBER_DISCOUNT if membership == "y" else 0
    family_discount = FAMILY_PACKAGE_DISCOUNT if number_of_tickets >= 4 else 0
    best_discount = max(member_discount, family_discount)
    return round(subtotal * (1 - best_discount), 2)


def calculate_tax(subtotal):
    """
    Calculates tax based on the subtotal.
    :param subtotal: Subtotal amount before tax
    :return: Tax amount (rounded to 2 decimal places)
    """
    return round(subtotal * TAX_RATE, 2)


def get_daily_special():
    """
    Randomly selects a daily special item.
    :return: Name of the daily special item
    """
    return random.choice(DAILY_SPECIALS)


def ticket_option():
    """
    Handles ticket selection and quantity input from the user.
    :return: Ticket type and quantity
    """
    while True:
        ticket_type = input("Select a ticket type (Regular, 3D, IMAX, Children, Senior): ").strip().lower()
        if validate_input("movie tickets", ticket_type):
            break
        print("Invalid Movie Ticket type. Please try again.")
    while True:
        try:
            quantity = int(input("Enter quantity (greater than 0): "))
            if quantity > 0:
                return ticket_type, quantity
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")


def concessions_option():
    """
    Handles concession selection, size (if applicable), and quantity input from the user.
    :return: Concession type, quantity, and size
    """
    while True:
        concession_type = input("Select concession type (Popcorn, Drinks, Candy, Nachos, Hot Dog, Daily Special): ").strip().lower()
        if validate_input("concessions", concession_type):
            break
        print("Invalid Concession type. Please try again.")
    size = None
    if concession_type in ["popcorn", "drinks"]:
        while True:
            size = input("Select size (small, medium, large): ").strip().lower()
            if size in ["small", "medium", "large"]:
                break
            print("Invalid size. Please select 'small', 'medium', or 'large'.")
    if concession_type == "daily special":
        concession_type = get_daily_special()
        print(f"You have selected the daily special: {concession_type.capitalize()}")
    while True:
        try:
            quantity = int(input("Enter quantity (greater than 0): "))
            if quantity > 0:
                return concession_type, quantity, size
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
