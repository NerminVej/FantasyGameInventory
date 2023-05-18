inventory1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
def displayInventory(inventory):
    total = 0
    for item,number in inventory.items():
       print(item, number)
       total += number
    print("Total number of items: " + str(total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1



addToInventory(inv,dragonLoot)
displayInventory(inv)

