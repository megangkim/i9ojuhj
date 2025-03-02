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

# Prices for different ticket types
REGULAR_TICKET = 14.99
THREE_D_TICKET = 17.99
IMAX_TICKET = 19.99
CHILDREN_TICKET = 8.99
SENIOR_TICKET = 10.99

# Prices for concessions
SMALL_POPCORN = 6.99
MEDIUM_POPCORN = 8.99
LARGE_POPCORN = 10.99
SMALL_DRINK = 4.99
MEDIUM_DRINK = 5.99
LARGE_DRINK = 6.99
CANDY = 4.50
NACHOS = 7.99
HOT_DOG = 6.99

# Discount rates and additional fees
MEMBER_DISCOUNT = 0.15  # Membership discount
FAMILY_PACKAGE_DISCOUNT = 0.10  # Discount for 4 or more tickets
ONLINE_BOOKING_FEE = 1.50  # Flat fee for booking online
TAX_RATE = 0.13  # Tax percentage

# Storing ticket and concession prices in dictionaries for easier reference
TICKET_PRICES = {
    "regular": REGULAR_TICKET,
    "3d": THREE_D_TICKET,
    "imax": IMAX_TICKET,
    "children": CHILDREN_TICKET,
    "senior": SENIOR_TICKET
}

CONCESSION_PRICES = {
    "popcorn": {"small": SMALL_POPCORN, "medium": MEDIUM_POPCORN, "large": LARGE_POPCORN},
    "drinks": {"small": SMALL_DRINK, "medium": MEDIUM_DRINK, "large": LARGE_DRINK},
    "candy": CANDY,
    "nachos": NACHOS,
    "hot dog": HOT_DOG
}

# List of items that may be part of the daily special
DAILY_SPECIALS = ["candy", "nachos", "hot dog"]


def validate_input(category, type_value):
    """
    Checks if the user input is a valid ticket or concession option.
    :param category: 'movie tickets' or 'concessions'
    :param type_value: The specific ticket or item type entered by the user
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
    Determines the total cost of movie tickets.
    :param ticket_type: Type of movie ticket (e.g., regular, 3d, imax)
    :param quantity: Number of tickets being purchased
    :return: Total price of the tickets rounded to two decimal places
    """
    ticket_type = ticket_type.strip().lower()
    if ticket_type in TICKET_PRICES:
        return round(TICKET_PRICES[ticket_type] * quantity, 2)
    return -1


def calculate_concession_cost(concession_type, quantity, size=None):
    """
    Determines the total cost of concession items.
    :param concession_type: Type of concession (e.g., popcorn, drinks, candy)
    :param quantity: Number of items purchased
    :param size: Size of the item (small, medium, large) if applicable
    :return: Total cost of the concessions rounded to two decimal places
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
    Determines and applies the best discount available (membership or family discount).
    :param subtotal: Price before any discounts
    :param number_of_tickets: Total number of movie tickets purchased
    :return: Adjusted subtotal after applying the best discount
    """
    membership = input("Are you a member? (y/n): ").strip().lower()
    member_discount = MEMBER_DISCOUNT if membership == "y" else 0
    family_discount = FAMILY_PACKAGE_DISCOUNT if number_of_tickets >= 4 else 0
    best_discount = max(member_discount, family_discount)
    return round(subtotal * (1 - best_discount), 2)


def calculate_tax(subtotal):
    """
    Computes the tax amount based on the subtotal.
    :param subtotal: The total cost before tax
    :return: Tax amount rounded to two decimal places
    """
    return round(subtotal * TAX_RATE, 2)


def get_daily_special():
    """
    Selects a random item from the list of daily specials.
    :return: The name of the randomly chosen daily special item
    """
    return random.choice(DAILY_SPECIALS)


def ticket_option():
    """
    Handles user input for selecting a ticket type and quantity.
    :return: Tuple containing ticket type and quantity
    """
    while True:
        ticket_type = input("Select a ticket type (Regular, 3D, IMAX, Children, Senior): ").strip().lower()
        if validate_input("movie tickets", ticket_type):
            break
        print("Invalid choice. Please try again.")
    while True:
        try:
            quantity = int(input("Enter ticket quantity (must be greater than 0): "))
            if quantity > 0:
                return ticket_type, quantity
            print("Please enter a valid quantity.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def concessions_option():
    """
    Handles user input for selecting concessions, including size and quantity.
    :return: Tuple containing concession type, quantity, and size (if applicable)
    """
    while True:
        concession_type = input("Select concession (Popcorn, Drinks, Candy, Nachos, Hot Dog, Daily Special): ").strip().lower()
        if validate_input("concessions", concession_type):
            break
        print("Invalid selection. Try again.")
    size = None
    if concession_type in ["popcorn", "drinks"]:
        while True:
            size = input("Choose size (small, medium, large): ").strip().lower()
            if size in ["small", "medium", "large"]:
                break
            print("Invalid size. Please try again.")
    if concession_type == "daily special":
        concession_type = get_daily_special()
        print(f"Today's special is: {concession_type.capitalize()}")
    while True:
        try:
            quantity = int(input("Enter quantity (greater than 0): "))
            if quantity > 0:
                return concession_type, quantity, size
            print("Invalid quantity. Try again.")
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    main()

