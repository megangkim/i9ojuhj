"""
*******************************
CS 1026 - Assignment 2 – Movie Ticket Booking System
Code by: Megan Kim
Student ID: mkim945
File created: February 25, 2025
*******************************
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

# Constants for concession prices
SMALL_POPCORN = 6.99
MEDIUM_POPCORN = 8.99
LARGE_POPCORN = 10.99
SMALL_DRINK = 4.99
MEDIUM_DRINK = 5.99
LARGE_DRINK = 6.99
CANDY = 4.50
NACHOS = 7.99
HOT_DOG = 6.99

# Discounts and Fees
MEMBER_DISCOUNT = 0.15
FAMILY_PACKAGE_DISCOUNT = 0.10
ONLINE_BOOKING_FEE = 1.50
TAX_RATE = 0.13

def validate_input(category, type_value):
    """Validates if the given category and type_value are valid choices."""
    category = category.strip().lower()
    type_value = type_value.strip().lower()
    
    valid_tickets = {"regular", "3d", "imax", "children", "senior"}
    valid_concessions = {"popcorn", "drinks", "candy", "nachos", "hot dog", "daily special"}
    
    if category == "movie tickets" and type_value in valid_tickets:
        return True
    elif category == "concessions" and type_value in valid_concessions:
        return True
    return False

def calculate_ticket_cost(ticket_type, quantity):
    """Calculates the total ticket cost based on type and quantity."""
    prices = {"regular": REGULAR_TICKET, "3d": THREE_D_TICKET, "imax": IMAX_TICKET, 
              "children": CHILDREN_TICKET, "senior": SENIOR_TICKET}
    ticket_type = ticket_type.strip().lower()
    
    if ticket_type in prices:
        return round(prices[ticket_type] * quantity, 2)
    return -1

def calculate_concession_cost(concession_type, quantity, size=None):
    """Calculates the cost of a concession item, considering size if applicable."""
    prices = {"candy": CANDY, "nachos": NACHOS, "hot dog": HOT_DOG}
    size_prices = {"small": SMALL_POPCORN, "medium": MEDIUM_POPCORN, "large": LARGE_POPCORN,
                   "small drink": SMALL_DRINK, "medium drink": MEDIUM_DRINK, "large drink": LARGE_DRINK}
    
    concession_type = concession_type.strip().lower()
    if concession_type in {"popcorn", "drinks"}:
        size = size.strip().lower() if size else ""
        if size in {"small", "medium", "large"}:
            return round(size_prices[f"{size} {concession_type}"] * quantity, 2)
        return -1
    elif concession_type in prices:
        return round(prices[concession_type] * quantity, 2)
    return -1

def apply_discount(subtotal, number_of_tickets):
    """Applies the best discount available (Membership or Family package)."""
    membership = input("Are you a member? (y/n): ").strip().lower()
    
    member_discount = subtotal * MEMBER_DISCOUNT if membership == "y" else 0
    family_discount = subtotal * FAMILY_PACKAGE_DISCOUNT if number_of_tickets >= 4 else 0
    
    return round(subtotal - max(member_discount, family_discount), 2)

def calculate_tax(subtotal):
    """Calculates and returns the tax amount based on subtotal."""
    return round(subtotal * TAX_RATE, 2)

def get_daily_special():
    """Randomly selects and returns a daily special item."""
    return random.choice(["candy", "nachos", "hot dog"])

def ticket_option():
    """Handles ticket selection and returns the type and quantity."""
    while True:
        ticket_type = input("Select a ticket type (Regular, 3D, IMAX, Children, Senior): ")
        if validate_input("movie tickets", ticket_type):
            break
        print("Invalid Movie Ticket type. Please try again.")
    
    while True:
        try:
            quantity = int(input("Enter quantity (greater than 0): "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")
    
    return ticket_type.strip().lower(), quantity

def concessions_option():
    """Handles concession selection and returns the type, quantity, and size."""
    while True:
        concession_type = input("Select concession type (Popcorn, Drinks, Candy, Nachos, Hot Dog, Daily Special): ")
        if validate_input("concessions", concession_type):
            break
        print("Invalid Concession type. Please try again.")
    
    if concession_type.lower() == "daily special":
        concession_type = get_daily_special()
        print(f"You have selected the daily special: {concession_type}")
    
    size = None
    if concession_type.lower() in {"popcorn", "drinks"}:
        while True:
            size = input("Select size (small, medium, large): ").strip().lower()
            if size in {"small", "medium", "large"}:
                break
            print("Invalid size. Please select 'small', 'medium', or 'large'.")
    
    while True:
        try:
            quantity = int(input("Enter quantity (greater than 0): "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")
    
    return concession_type.strip().lower(), quantity, size

def main():
    """Main function to process user selections and calculate total cost."""
    subtotal = 0
    total_tickets = 0
    
    while True:
        choice = input("Would you like to order Movie Tickets, Concessions, or type done to finish?: ").strip().lower()
        if choice == "done":
            break
        elif choice == "movie tickets":
            ticket_type, quantity = ticket_option()
            subtotal += calculate_ticket_cost(ticket_type, quantity)
            total_tickets += quantity
        elif choice == "concessions":
            concession_type, quantity, size = concessions_option()
            subtotal += calculate_concession_cost(concession_type, quantity, size)
        else:
            print("Invalid category type. Please try again.")
    
    if subtotal == 0:
        print("You don't seem to have ordered anything.")
        return
    
    subtotal = apply_discount(subtotal, total_tickets)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax + ONLINE_BOOKING_FEE, 2)
    
    print(f"Subtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nBooking Fee: ${ONLINE_BOOKING_FEE:.2f}\nTotal: ${total:.2f}")

if __name__ == "__main__":
    main()
