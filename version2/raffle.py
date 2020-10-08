"""Randomly pick customer and print customer info"""

from random import choice
import customers

def pick_winner(customer_file_path):
    customers_list = customers.get_customer_from_file(customer_file_path)

    chosen_customer = choice(customers_list)

    print(f"Tell {chosen_customer.name} at {chosen_customer.email} that they've won")
