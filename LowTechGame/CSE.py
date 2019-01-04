from __future__ import print_function
from time import sleep

inventory = ["key"]
def inventoryAdd(): pass
def inventoryCall(): pass

def CSE():
    print("You arrive at the CSE room and try the door, but it's locked.");
    sleep(1)
    
    # branches based on player having/not having the door key
    
    if not "key" in inventory: # player doesn't have key
        print("You don't have a key with you so you go back into the halls.\n")
        sleep(1)
    else: # player has key
        print("Using the room key, you open the door and enter the room.")
        sleep(1)
        print("There's a computer on in the corner.")
        sleep(0.75)
        choice = raw_input("Do you want to go to the (C)omputer, or (L)eave the room: (C/L) ").lower()
        sleep(0.75)
        
        # while loop until valid choice is chosen
        while choice not in "cl":
            choice = raw_input("That was not a choice. Choose C to go to the computer or L to leave the room." )
            sleep(0.25)
        
        if choice == "l": # player leaves
            print("You go back into the halls.\n")
            sleep(1)
        elif choice == "c": # player goes to computer
            dennis = True
            print("You sign into your gmail account. You open up an email and")
            print("address it to the entire school... teachers included!")
            
            raw_input("What do you want to say? ") # does not matter
            
            print("\nYou look at your masterly crafted email and click send.\n")
            sleep(1)
            print("Suddenly you hear a BANG! SLAM! KABOOM! and a loud voice")
            print("coming from around the research wing.\n")
            sleep(1)
            print("You don't think anything of it until it grows in intensity")
            print("and you realize it's Mr. Dennis! You'd better check it out!\n")
            sleep(1)
            print("You rush back into the halls!")
            sleep(1)
        
def gprint(text):
    """
    Prints letter by letter like some games.
    """
    for i in text:
        print(i, end="")
        sleep(0.075)
    print("")

"""

(Look at computer)
You sign into your account. You open up an email and address it to the entire school...\n
teachers included! What do you want to say?
*text prompt*
You look at your masterly crafted email. You click send. Suddenly... BANG! SLAM! KABOOM!\n
You hear a loud voice in the distance. You think nothing of it. It slowly grows in intensity \n
You now identify it as that of Mr. Dennis! You better check it out.

You rush back into the halls.
Which room will you go to? (#)
*room prompt*
"""