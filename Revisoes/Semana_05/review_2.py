# Criar um dict a partir de valores e quantidades em uma lista

list = ["coal", "coal", "coal", "wood", "wood", "wood", "diamond", "diamond", "diamond"]

def create_inventory(list):

    inventory_dict = {}

    for item in list:
        inventory_dict[item] = inventory_dict.get(item, 0) + 1

    return inventory_dict

print(create_inventory(list))