from __future__ import print_function
from time import sleep
inventory = []
mprstorage = []
def mpr():
    print('''You walk into the vast MPR. It's a bit chilly. There's a lot of open space around
You should be able to leave things here to come back for them later.''')
    sleep(3)
    mprStorageCall()
    sleep(2)
    inventoryCall()
    sleep(2)
    leave = raw_input("Do you want to leave anything in the MPR? (Y/N)")
    if leave.lower()=="y":
        leaveInMPR()
    take = raw_input("Do you want to take anything from the MPR? (Y/N)")
    if take.lower()=="y":
        takeFromMPR()
    print("You exit into the hall.")
            
            
def leaveInMPR():
    cont=True
    if len(inventory)>0:
        item = raw_input("What do you want to leave in the MPR?")
        while cont:
            inInventory = False
            for stuff in inventory:
                if stuff.lower() == item.lower():
                    inInventory = True
                    break
            if not inInventory:
                item = raw_input("You search yourself for it but you can't find it. Try another item.")
            else:
                print("You leave",item,"in the MPR.")
                inventory.remove(item)
                mprstorage.append(item)
                inventoryCall()
                mprStorageCall()
                cont=False
    else:
        print("You don't have any items to leave in the MPR.")    
    
def takeFromMPR():
    cont=True
    if len(mprstorage)>0:
        item = raw_input("What do you want to take frpm the MPR?")
        while cont:
            inStorage = False
            for stuff in mprstorage:
                if stuff.lower() == item.lower():
                    inStorage = True
                    break
            if not inStorage:
                item = raw_input("You search for it but you can't find it. Try another item.")
            else:
                print("You take",item,"from the MPR.")
                inventory.append(item)
                mprstorage.remove(item)
                inventoryCall()
                mprStorageCall()
                cont=False
    else:
        print("There aren't any items to take from the MPR.")   

def mprStorageCall():
    """prints things left in the mpr"""
    if len(mprstorage)==0:
        print("Nothing is on the table.")
    elif len(mprstorage)==1:
        print("The",mprstorage[0],"is on the table.")
    else:
        statement = "There are a few things on the table: "
        for item in mprstorage:
            statement += item+", "

def inventoryCall():
    print("You have ", end="")
    if len(inventory)==2:
        print("a",inventory[0],"and a",inventory[1],"in your hands.")
    elif len(inventory)==1:
        print("a",inventory[0],"in your hands.")
    else:
        print("nothing in your hands.")
        
def inventoryAdd(obj):
    """adds obj to inventory. obj should be a string"""
    size=1
    if obj=="TSA Trophy":
        size =2
        print("The TSA Trophy takes two hands to pick up.")
    if len(inventory)+size>2:
        print("Your hands are too full to pick up",obj+".")
    else:
        print("You picked up",obj)
        inventory.append(obj)
    inventoryCall()