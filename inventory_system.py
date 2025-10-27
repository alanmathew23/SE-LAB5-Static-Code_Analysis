"""
Inventory management system module.


This module provides functions to manage product inventory including
adding/removing items, saving/loading data, and checking stock levels.
"""
import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item (str): The item name to add
        qty (int): The quantity to add
        logs (list): Optional log list to record operations

    Returns:
        None
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove an item from the inventory.

    Args:
        item (str): The item name to remove
        qty (int): The quantity to remove

    Returns:
        None
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Item '{item}' not found in inventory")
    except TypeError as e:
        print(f"Error: Invalid type for quantity - {e}")


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item (str): The item name to query

    Returns:
        int: The quantity of the item
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): The filename to load from

    Returns:
        None
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(
            f"Warning: File '{file}' not found, "
            f"starting with empty inventory"
        )
        stock_data = {}


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file (str): The filename to save to

    Returns:
        None
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=2)


def print_data():
    """
    Print the current inventory report.

    Returns:
        None
    """
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """
    Check for items below a quantity threshold.

    Args:
        threshold (int): The minimum quantity threshold

    Returns:
        list: List of items below the threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to demonstrate inventory system usage.

    Returns:
        None
    """
    add_item("apple", 10)
    add_item("banana", 3)
    remove_item("apple", 3)
    remove_item("orange", 1)  # Will trigger warning for missing item
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
