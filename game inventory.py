import csv, os
# iterate the things what we will work in the program

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# print all inventory

def display_inventory(inv):  
    sumInvValues = 0        # iterate total inventory vale to 0 for sum
    print("  Inventory:")

    for key, value in inv.items(): 
        sumInvValues += value
        print(key, value)       # collect and after print the elements of the "inv" dictionary.
    print("Total number of items:", (sumInvValues))      # print total inventory values

def add_to_inventory(inventory, added_items):
    # inventory = inv
    # added_items = dragon_loot
    for i in added_items:       
        if i in inventory:
            inventory[i] += 1
        if i not in inventory:
            inventory[i] = 1

inv == add_to_inventory(inv, dragon_loot)

desc = True
asc = False
def print_table(inventory, order):
    # find the len of longest string:
    longest_list = []
    for i in range(len(inventory)):
        longest_list.append(len(list(inventory.keys())[i]))
    longest_string = (max(longest_list))
    # make the desc and asc type:

    dictToList = []

    for number in range(len(inventory.items())):
        dictToList.append([list(inventory.values())[number], list(inventory.keys())[number]])

    desc_asc = (sorted(dictToList, reverse= order))
    # print the table (upside)
    item = "item"
    print(
    " Inventory:\n","\n",
    "count",item.rjust(longest_string + 2),"\n","\n",
    "-"*(longest_string+8),
    )
    TotalNumberOfItems = 0
    # print the table (center)
    for number2 in range(len(inventory)):
        stringConvert = str(desc_asc[number2][0])
        stringConvert2 = str(desc_asc[number2][1])
        print(stringConvert.rjust(6), stringConvert2.rjust(longest_string + 2))
        TotalNumberOfItems += desc_asc[number2][0]
    # print the table (downside)
    print("-"*(longest_string+9))
    print("Total number of items:", TotalNumberOfItems)

#print_table(inv,asc)
def import_inventory(inventory, filename):
    o = open(filename)
    csv_o = csv.reader(o)
    iDontKnow = 0
    for csvItem in csv_o:
        iDontKnow += 1
    add_to_inventory(inv, csvItem)
    print_table(inv, desc)

#import_inventory(inv,"/home/gergo/Desktop/kész python/game_inventory/importinventory.csv")

def export_inventory(inventory, filename):
    exportlist = []
    for i in range(len(inv.items())):
                exportlist.append(list(inv.keys())[i])
                exportlist.append(list(inv.values())[i])

    with open(filename,"w", newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(exportlist)

#export_inventory(inv,"/home/gergo/Desktop/kész python/game_inventory/exportinventory.csv")