inventory = {"coal": 1}
items = ["wood", "iron", "coal", "wood"]
# {"coal":2, "wood":2, "iron":1}

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    for item in items:

        if item not in inventory:
            inventory[item] = 1

        else: 
            inventory[item] += 1


    return inventory

print(add_items(inventory, items))