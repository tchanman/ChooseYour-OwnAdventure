from __future__ import print_function
from time import sleep
from random import randint

inventory = []
def inventoryAdd(item):
    pass

def cim():
    pass

dennis_unleashed = False

def resWing():
    """
    Player actions while in the research wing
    """
    memes = ["We are Number One", "Darude Sandstorm", "Never Gonna Give You Up", "Allstar"]
    if dennis_unleashed:
        cim()
    else:
        print("You walk in to the research wing and start walking around.")
        sleep(0.75)
        
        print("Do you want to head towards the (P)iano or get a laptop from",end="")
        choice = raw_input("a (C)omputer cart? (P/C) ").lower()
        sleep(0.75)
        
        while choice not in "pc":
            print("That wasn't a choice. Choose P to go to the piano",end="")
            choice = raw_input("or C to go a computer cart. ")
            sleep(0.75)
        
        if choice == "p":
            print("You suddenly decide that you want to play something")
            sleep(0.25)
            print("on the piano, so you head towards the piano in the back.")
            sleep(0.75)
            print("Just as you are about to play a beautiful rendition of")
            sleep(0.25)
            print("\"{},\" you see a flashlight on the ground.".format(memes[randint(0,3)]),end="")
            sleep(0.75)
            choice = raw_input("Do you want to pick it up? (Y/N)").lower()
            sleep(0.75)
            
            while choice not in "pc":
                print("That wasn't a choice. Choose Y to pick it up",end="")
                choice = raw_input("or N if you don't want to. ")
                sleep(0.75)