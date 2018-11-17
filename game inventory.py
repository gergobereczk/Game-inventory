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

def print_table(inventory):
    # find the len of longest string:
    longest_list = []
    for i in range(len(inventory)):
        longest_list.append(len(list(inventory.keys())[i]))
    longest_string = (max(longest_list))
    # make the desc and asc type:

    dictToList = []

    for number in range(len(inventory.items())):
        dictToList.append([list(inventory.values())[number], list(inventory.keys())[number]])

    desc = (sorted(dictToList, reverse=True))
    asc = (sorted(dictToList, reverse=False))  
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
        stringConvert = str(desc[number2][0])
        stringConvert2 = str(desc[number2][1])
        print(stringConvert.rjust(6), stringConvert2.rjust(longest_string + 2))
        TotalNumberOfItems += desc[number2][0]
    # print the table (downside)
    print("-"*(longest_string+9))
    print("Total number of items:", TotalNumberOfItems)

 






    # table_line = 20
    # print(
    # "Inventory:\n",
    # "count   item name\n",
    # "-"*table_line,
    # )
    # sumInvValues = 0        #iterate total inventory vale to 0 for sum
    # for key, value in inventory.items(): 
    #     sumInvValues += value
    #     print(value, key)       # collect and after print the elements of the "inv" dictionary.
    # print("-"*table_line)
    # print("Total number of items:", (sumInvValues))      # print total inventory values
    # #print('{:_<40}'.format('test'))


# display_inventory(inv)
print_table(inv)
# print right justified test
# test_right = 11
# test_lyrics = "test lyrics"
# len_testlyrics = (len(test_lyrics))*2
# print ("test lyrics")
# print ("test lyrics".rjust(len_testlyrics))