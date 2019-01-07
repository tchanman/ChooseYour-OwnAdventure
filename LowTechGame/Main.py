'''
Low Tech Low Game
Player comes to LTLU to send a mass mail and finds hidden secrets in this thrilling adventure
'''

from __future__ import print_function
from time import sleep
import os

#Constants
ROOMS = ['1','2','3','4','5','6','cse','court yard', 'math', 'mpr', 'research wing', 'cim']

MAP_1 = '''

                         ..zeeeeeee....                             
                    .zd$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$be. 
                 .e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\              
               .$$$$$$$$$$$$$$$$$$$$$$$$$$$^                   $$$        
             .$$$$$$$$$$*""        ""**""                      $$$  
            z$$$$$$$$""                                        $$$  
           d$$$$$$$"                          4.Research Wing  $$$  
          d$$$$$$"   1.CSE                                     $$$  
         d$$$$$$"         _.-""""-._                           $$$  
        .$$$$$$F        .'          `.                         $$$ 
        d$$$$$$        /      __      \                        $$$  
       .$$$$$$F       |     ==  ==     |       4$$$$$$$$$$$$$$$$$/           
       :$$$$$$|      |  5.Court Yard    |      |$$$$$$$$$$$$$$$P"            
       !$$$$$$|      |     ==    ==     |      |$$$$$$$            
        $$$$$$b       |     ==__==     |       4$$$$$$'           
        3$$$$$$        \              /        $$$$$$P            
         $$$$$$b        `._        _.'        d$$$$$$"            
         '$$$$$$b.         `-....-'          d$$$$$$F             
          "$$$$$$$b  2.Math         3.MPR  .$$$$$$$P       ================
           "$$$$$$$$.                    .$$$$$$$$"        Low Tech 
            ^$$$$$$$$$e.              .e$$$$$$$$$"         Low Univerity
              "$$$$$$$$$$$ee.    .ee$$$$$$$$$$$*           ================
                "$$$$$$$$$$$$|  |$$$$$$$$$$$$"    
                  "*$$$$$$$$$|  |$$$$$$$$$*"       
                     ^"*$$$$$|  |$$$$$*""      
                            "]  ["   
                            
                            '''

MAP_2 = '''

                                               $$$$$$$$$
                                               $       $
                                               $ 6.CIM $
                                               $       $
                                               $$$} {$$$
                                                  | |
                         ..zeeeeeee....           | |               
                    .zd$$$$$$$$$$$$$$$$$$$$$$$$$$$| |$$$$$$$$be. 
                 .e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$} {$$$$$$$$$$$\              
               .$$$$$$$$$$$$$$$$$$$$$$$$$$$^                   $$$        
             .$$$$$$$$$$*""        ""**""                      $$$  
            z$$$$$$$$""                                        $$$  
           d$$$$$$$"                          4.Research Wing  $$$  
          d$$$$$$"   1.CSE                                     $$$  
         d$$$$$$"         _.-""""-._                           $$$  
        .$$$$$$F        .'          `.                         $$$ 
        d$$$$$$        /      __      \                        $$$  
       .$$$$$$F       |     ==  ==     |       4$$$$$$$$$$$$$$$$$/           
       :$$$$$$|      |  5.Court Yard    |      |$$$$$$$$$$$$$$$P"            
       !$$$$$$|      |     ==    ==     |      |$$$$$$$            
        $$$$$$b       |     ==__==     |       4$$$$$$'           
        3$$$$$$        \              /        $$$$$$P            
         $$$$$$b        `._        _.'        d$$$$$$"            
         '$$$$$$b.         `-....-'          d$$$$$$F             
          "$$$$$$$b  2.Math         3.MPR  .$$$$$$$P       ================
           "$$$$$$$$.                    .$$$$$$$$"        Low Tech 
            ^$$$$$$$$$e.              .e$$$$$$$$$"         Low Univerity
              "$$$$$$$$$$$ee.    .ee$$$$$$$$$$$*           Dennis Unleashed
                "$$$$$$$$$$$$|  |$$$$$$$$$$$$"             ================
                  "*$$$$$$$$$|  |$$$$$$$$$*"       
                     ^"*$$$$$|__|$$$$$*""      
                            "    "   
                            
                            '''

MAP_3 = '''

                                               $$$$$$$$$
                                               $       $
                                               $ 6.CIM $
                                               $       $
                                               $$$} {$$$
                                                  | |
                         ..zeeeeeee....           | |               
                    .zd$$$$$$$$$$$$$$$$$$$$$$$$$$$| |$$$$$$$$be. 
                 .e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$} {$$$$$$$$$$$\              
               .$$$$$$$$$$$$$$$$$$$$$$$$$$$^                   $$$        
             .$$$$$$$$$$*""        ""**""                      $$$  
            z$$$$$$$$""                                        $$$  
           d$$$$$$$"                          4.Research Wing  $$$  
          d$$$$$$"   1.CSE                                     $$$  
         d$$$$$$"         _.-""""-._                           $$$  
        .$$$$$$F        .'          `.                         $$$ 
        d$$$$$$        /      __      \                        $$$  
       .$$$$$$F       |     ==  ==     |       4$$$$$$$$$$$$$$$$$/           
       :$$$$$$|      |  5.Court Yard    |      |$$$$$$$$$$$$$$$P"            
       !$$$$$$|      |     ==    ==     |      |$$$$$$$            
        $$$$$$b       |     ==__==     |       4$$$$$$'           
        3$$$$$$        \              /        $$$$$$P            
         $$$$$$b        `._        _.'        d$$$$$$"            
         '$$$$$$b.         `-....-'          d$$$$$$F             
          "$$$$$$$b  2.Math         3.MPR  .$$$$$$$P       ================
           "$$$$$$$$.                    .$$$$$$$$"        Low Tech 
            ^$$$$$$$$$e.              .e$$$$$$$$$"         Low Univerity
              "$$$$$$$$$$$ee.    .ee$$$$$$$$$$$*           Dennis Unleashed
                "$$$$$$$$$$$$|@@|$$$$$$$$$$$$"             ================
                  "*$$$$$$$$$|  |$$$$$$$$$*"       
                     ^"*$$$$$|  |$$$$$*""      
                            "]  ["   
                            
                            '''


#Global variables
dennis = False
main_door_riddle = False
has_key = False
inventory = []
mprstorage = []
end = False
name = ''

#Functions
def mapCall():
    if dennis:
        print (MAP_2)
    elif main_door_riddle:
        print (MAP_3)
    else:
        print (MAP_1)

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
    
def math():
    pass

def mpr():
    print('''You walk into the vast MPR. It's a bit chilly. There's a lot of open space around
You should be able to leave things here to come back for them later.''')
    sleep(3)
    mprStorageCall()
    sleep(2)
    inventoryCall()
    sleep(2)
    leave = raw_input("Do you want to leave anything in the MPR? (Y/N)\n")
    if leave.lower()=="y":
        leaveInMPR()
    take = raw_input("Do you want to take anything from the MPR? (Y/N)\n")
    if take.lower()=="y":
        takeFromMPR()
    print("You exit into the hall.")
            
            
def leaveInMPR():
    """Leave items in MPR"""
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
    """Take items from MPR"""
    cont=True
    if len(mprstorage)>0:
        item = raw_input("What do you want to take from the MPR?")
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
    """Prints things left in the mpr"""
    if len(mprstorage)==0:
        print("Nothing is on the table.")
    elif len(mprstorage)==1:
        print("The",mprstorage[0],"is on the table.")
    else:
        statement = "There are a few things on the table: "
        for item in mprstorage:
            statement += item+", "

def inventoryCall():
    """Prints things in inventory"""
    print("You have ", end="")
    if len(inventory)==2:
        print("a",inventory[0],"and a",inventory[1],"in your hands.")
    elif len(inventory)==1:
        print("a",inventory[0],"in your hands.")
    else:
        print("nothing in your hands.")
        
def inventoryAdd(obj):
    """Adds obj to inventory. obj should be a string"""
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

def research():
    pass    

def courtyard():
    for item in inventory:
        if item == 'key':
            global has_key
            has_key = True

def cim():
    pass

def hall():
    '''User decisions'''
    sleep(1)
    command = raw_input("Where do you want to go? (#) What do you want to do?\n").strip().lower()
    if command == 'm' or command == 'map':
        mapCall()
    elif command == 'i' or command == 'inv' or command == 'inventory':
        inventoryCall()    
    elif command == 'q' or command == 'quit':
        global end
        end = True
    elif command not in ROOMS:
        sleep(1)
        print ("You wander around the halls but you don't find that room. Strange. Use command h for help.")
    elif command == '1' or command == 'cse':
        sleep(1)
        cse()
    elif command == '2' or command == 'math':
        sleep(1)
        math()
    elif command == '3' or command == 'mpr':
        sleep(1)
        mpr()
    elif command == '4' or command == 'research wing':
        sleep(1)
        research()
    elif command == '5' or command == 'court yard':
        sleep(1)
        courtyard()
    elif command == '6' or command == 'cim':
        if not dennis:
            sleep(1)
            print ("You vaguely remember a room like that but you don't find that around the halls.")
        else:
            sleep(1)
            cim()
    elif command == 'h':
        help()

def intro():
    INTRO_TIME=0.3
    for i in 'LOW TECH LOW ADVENTURE':
        print(i, end="")
        sleep(INTRO_TIME)
    sleep(1)
    global name
    name = raw_input("What's your name?\n").strip().lower()
    if name == 'chanas' or name == 'hanas' or name == 'chris':
        print ('Oh hello there Chris. How are you today? It would be great if we could get a 100. Thanks\n')
    if name == 'jesus':
        print ('Hello Bob Dennis\n')
    if name == '':
        print ('Wow such a creative name. I applaud your parents.\n')
        name = '[REDACTED]'
    sleep(1)
    print ('''\nYou stand outside your university, the famous Low Tech Low University,
the #1 STEM University for 8 times in the past 7 years. A sudden urge comes over you.
You feel like sending a mass mail. Today is your day.''')
    sleep(5)
    
    
    mapCall()
    print ('You enter the familiar halls.',end='')

def clearScreen():
    clear = lambda: os.system('cls')
    clear()

#Main
if __name__ == '__main__':
    clearScreen()
    intro()
    game = True
    while game:
        hall()
        if end:
            quitting = raw_input('Are you sure you want to quit?\n').strip().lower()
            if quitting == 'yes' or quitting =='y':
                clearScreen()
                print ('You remember you can use your phone to send your mass mail.') 
                sleep(1.5)
                for i in range(3):
                    print ('.')
                    sleep(0.67)
                print ('\nHuh, neat.\n\n')
                sleep(2)
                print ('GAME OVER')
                print ('THANKS FOR PLAYING')
                game = False
            elif quitting == 'n' or quitting == 'n':
                print ('You doubted whether you can do this, however you shake your head and steel your resolve.')
            else:
                print ('You confuse yourself by answering', quitting, 'to a yes or no question. You go back into the halls.')