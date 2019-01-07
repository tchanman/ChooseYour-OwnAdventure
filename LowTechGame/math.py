from __future__ import print_function
inventory = ["key"]
from time import sleep


def math():
    print("You arrive at the math room and try the door, but it's locked.")
    sleep(1)
    
    # branches based on player having/not having the door key
    
    if not "key" in inventory: # player doesn't have key
        print("You don't have a key with you so you go back into the halls.\n")
        sleep(1)
    else: # player has key
        print("You fiddle around with the key and unlock the door.")
        sleep(2)
        print("The math room is dark. You flick on the lights and take a look around the room.")
        sleep(1)
        print("There's a few calculators and a textbook on the desk.")
        sleep(0.5)
        cont = True
        while cont:
            choice = raw_input("Will you look at the (C)alculators, read the (T)extbook, or (L)eave? (C/T/L)")
            if choice.lower() == "c":
                print("You take a look at the calculators.")
                sleep(1)
                print("They're charging.")
                sleep(1.5)
                print("Better leave them alone.")
            elif choice.lower() == "l":
                print("You shut off the lights and leave the math room.")
                cont=False
            elif choice.lower() == "t":
                if dennis_riddle == False:
                    print("You glance at the cover.")
                    sleep(1)
                    print("Small text at the bottom of the cover catches your eye.")
                    sleep(1)
                    print("Written by Bishawn??")
                    sleep(1.5)
                    print("Preposterous. You don't have time for fakes claiming to be the famous Bishawn.")
                    sleep(1.5)
                else:
                    print("You glance at the cover and see 'Written by Bishan'.")
                    sleep(0.75)
                    print("It'll probably be a fake but it was worth a shot.")
                    sleep(1)
                    print("You open the book.")
                    sleep(3)
                    print("You are stunned as your head is flooded with knowledge.")
                    sleep(1)
                    print("You quickly shut the book before your brain is fried.")
                    sleep(0.75)
                    print("You think you have learned enough math.")
            else:
                print("You try to do",choice,"but trip.\nYou forget what you were trying to do when you get up.")

            