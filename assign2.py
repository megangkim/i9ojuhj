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

# Constants for ticket prices
REGULAR_TICKET = 14.99
THREE_D_TICKET = 17.99
IMAX_TICKET = 19.99
CHILDREN_TICKET = 8.99
SENIOR_TICKET = 10.99

# constants for concession prices
SMALL_POPCORN = 6.99
MEDIUM_POPCORN = 8.99
LARGE_POPCORN = 10.99
SMALL_DRINK = 4.99
MEDIUM_DRINK = 5.99
LARGE_DRINK = 6.99
CANDY = 4.50
NACHOS = 7.99
HOT_DOG = 6.99

# these are the discounts and fees
MEMBER_DISCOUNT = 0.15
FAMILY_PACKAGE_DISCOUNT = 0.10
ONLINE_BOOKING_FEE = 1.50
TAX_RATE = 0.13

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

DAILY_SPECIALS = ["candy", "nachos", "hot dog"]

# this validates if the given category and type_value are vaid choices
def validate_input(category, type_value):
    category = category.strip().lower()
    type_value = type_value.strip().lower()
    if category == "movie tickets" and type_value in TICKET_PRICES:
        return True
    if category == "concessions" and (type_value in CONCESSION_PRICES or type_value == "daily special"):
        return True
    return False

# this calculates the total ticket cost which is based off of the type and quantity.
def calculate_ticket_cost(ticket_type, quantity):
    ticket_type = ticket_type.strip().lower()
    if ticket_type in TICKET_PRICES:
        return round(TICKET_PRICES[ticket_type] * quantity, 2)
    return -1

# this calculates the cost of the concession items, and considers size if applicable
def calculate_concession_cost(concession_type, quantity, size=None):
    concession_type = concession_type.strip().lower()
    if concession_type in ["popcorn", "drinks"]:
        size = size.strip().lower()
        if size in CONCESSION_PRICES[concession_type]:
            return round(CONCESSION_PRICES[concession_type][size] * quantity, 2)
        return -1
    elif concession_type in CONCESSION_PRICES:
        return round(CONCESSION_PRICES[concession_type] * quantity, 2)
    return -1

# this applies the best available discout (membership vs family packagge)
def apply_discount(subtotal, number_of_tickets):
    membership = input("Are you a member? (y/n): ").strip().lower()
    member_discount = MEMBER_DISCOUNT if membership == "y" else 0
    family_discount = FAMILY_PACKAGE_DISCOUNT if number_of_tickets >= 4 else 0
    best_discount = max(member_discount, family_discount)
    return round(subtotal * (1 - best_discount), 2)

# calculates and returns the tax amount based off of the subtotal
def calculate_tax(subtotal):
    return round(subtotal * TAX_RATE, 2)

# this randomly selects and returns a daily special item
def get_daily_special():
    return random.choice(DAILY_SPECIALS)

# handles ticket selection and returns the type and quantity 
def ticket_option():
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

# main function to process user selections and calculate total cost
def main():
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
