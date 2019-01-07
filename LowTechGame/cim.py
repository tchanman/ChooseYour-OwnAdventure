from __future__ import print_function
from time import sleep

def inventoryAdd(thing):
    pass

def cim():
    print ('''You walk over to the research wing and see a room to the north. Of course! How could you
have forgotten? It's the CIM room! You peer through the glass windows and find Bob himself, reading your email.''')
    action = raw_input("What do you do?\n").lower()
    print ("You try to ", action, "but before you can do anything, Bob Dennis runs out the door in a fit of rage.")
    print ("Oh well.")
    take = raw_input("Inside the CIM room, you see a TSA Trophy. Do you want to take the trophy or leave?").lower()
    if take == 't' or take == 'take':
        inventoryAdd('TSA Trophy')
    elif take == 'leave' or take == 'l':
        print ("You leave the nostalgic room and go back into the halls.")
    else:
        print ("You try to do",action, "but you find you can't. You go back into the halls.") 
    print ("You look around and find the school is different.")
    global dennis_riddle
    dennis_riddle = True
    mapCall()