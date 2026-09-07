# adicionar ou atualizar dicionário já existente com itens de uma lista

inventory = {'coal': 1, 'wood': 2}
item_list = ['wood', 'iron', 'coal', 'wood', 'iron', 'wood', 'coal', 'coal', 'coal']

def add_items(inventory, item_list):
    """"""

    for item in item_list:
        if item not in inventory:
            inventory[item] = 1

        else:
            inventory[item] += 1

    return inventory

add_items(inventory, item_list)
print(inventory)