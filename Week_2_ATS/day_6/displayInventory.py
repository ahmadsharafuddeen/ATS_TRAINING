import pprint

inventory =  {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory_dict):
    sum  = 0
    for k,v in inventory_dict.items():
        sum += v
        print(pprint.pformat(f"{v} {k}"))
    print(f"Total number of items: {sum}")
# displayInventory(inventory)

def addToInventory(inventory, addedItems):
    print("")
    # your code goes here
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
            
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)