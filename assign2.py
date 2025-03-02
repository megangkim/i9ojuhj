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


def main():
    """
    Main function that runs the movie ticket booking system.
    Handles user input, calculates totals, applies discounts, and displays final cost.
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
    
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Online Booking Fee: ${ONLINE_BOOKING_FEE:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()

