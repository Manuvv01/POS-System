"""
Does the calculations of the project
"""

def calculate_total(total, item):
    total["value"] += item.price

def calculate_change(money, total):
    return money - total["value"]

