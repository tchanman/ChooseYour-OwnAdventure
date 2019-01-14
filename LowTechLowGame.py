'''
Low Tech Low Game
Player comes to LTLU to send a mass mail and finds hidden secrets in this thrilling adventure

By: Thomas Chan, Chukwuemekalum Kevin Patrick Echezona, and Jason Yan
'''

from __future__ import print_function
from time import sleep, time
import os
from random import randint

#Constants
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
                        0. Front Door
                            '''
MAP_2 = '''

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
                     ^"*$$$$$|==|$$$$$*""      
                            "    "   
                        0. Front Door
                            '''
MAP_3 = '''

                                              $$$$$$$$$$$
                                              $$       $$
                                              $$ 6.CIM $$
                                              $$       $$
                                              $$$$} {$$$$
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
                     ^"*$$$$$|==|$$$$$*""      
                            "    "   
                        0. Front Door    
                            '''

#Global variables
dennis = False
knowledge = False
dennis_riddle = False
cim_visited = False
end = False
game = True

inventory = []
mprstorage = []

name = ''
mail = ''

startTime = time()

#Functions
def mapCall():
    '''
    Prints map based on progress in story
    '''
    
    if dennis:
        print (MAP_2,end='')
    elif cim_visited:
        print (MAP_3,end='')
    else:
        print (MAP_1,end='')
    print('\n',end='')
        
def inventoryCall():
    """
    Prints things in inventory
    """
    
    print("You have ", end="")
    if len(inventory)==2:
        print("a",inventory[0],"and a",inventory[1],"in your hands.")
    elif len(inventory)==1:
        print("a",inventory[0],"in your hands.")
    else:
        print("nothing in your hands.")
        
def inventoryAdd(obj):
    """
    Adds obj to inventory. obj should be a string
    """
    
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

def clearScreen():
    '''
    Clears iPython screen
    '''
    
    clear = lambda: os.system('cls')
    clear()

#Rooms and affiliated functions
def cse():
    '''
    Initially locked, use key to open
    Send mass mail to school, locks front door and opens CIM room
    '''
    
    print("You arrive at the CSE room and try the door, but it's locked.");
    sleep(1)
    
    if not "key" in inventory:
        print("You go back into the halls.")
        sleep(1)
    else: 
        print("Using the room key, you open the door and enter the room.")
        sleep(1)
        print("There's a computer on in the corner.")
        sleep(0.75)
        choice = raw_input("Do you want to go to the (C)omputer, or (L)eave the room: (C/L)\n").lower()
        sleep(0.75)
        
        while choice not in "cl":
            choice = raw_input("You wander around the room but you do not see that. What do you do?\n")
            sleep(0.25)
        
        if choice == "l": 
            print("You go back into the halls.")
            sleep(1)
        elif choice == "c":
            global dennis
            dennis = True
            print("You sign into your gmail account. You open up an email and")
            print("address it to the entire school... teachers included!")
            sleep(2)
            
            global mail
            mail = raw_input("What do you want to say?\n\n")
            
            sleep(1)
            print("\nYou look at your masterly crafted email and click send.\n")
            sleep(1)
            print("Suddenly you hear...")
            sleep(1)
            print("BANG!")
            sleep(1)
            print ("SLAM!")
            sleep(1)
            print ("KABOOM!")
            sleep(1)
            print("...and a loud voice coming from around the research wing.\n")
            sleep(2)
            print("You don't think anything of it until it grows in intensity") 
            print("and you realize it's Mr. Dennis! You'd better check it out!\n")
            sleep(3)
            print("You rush back into the halls!")
            sleep(1)
    
def math():
    '''
    Initially locked, use key to open
    Use textbook to solve door riddle and win game
    Calculators as additional option, red herring
    '''
    
    print("You arrive at the math room and try the door, but it's locked.")
    sleep(1)
    
    if not "key" in inventory:
        print("You don't have a key with you so you go back into the halls.\n")
        sleep(1)
    else:
        print("You fiddle around with the key and unlock the door.")
        sleep(2)
        print("The math room is dark. You flick on the lights and take a look around the room.")
        sleep(1)
        print("There's a few calculators and a textbook on the desk.")
        sleep(0.5)
        
        cont = True
        while cont:
            choice = raw_input("Will you look at the (C)alculators, read the (T)extbook, or (L)eave? (C/T/L)\n")
            if choice.lower() == "c":
                print("\nYou take a look at the calculators.")
                sleep(1)
                print("They're charging.")
                sleep(1.5)
                print("Better leave them alone.")
            elif choice.lower() == "l":
                print("You shut off the lights and leave the math room.")
                cont=False
            elif choice.lower() == "t":
                if dennis_riddle == False:
                    print("\nYou glance at the cover.")
                    sleep(1)
                    print("Small text at the bottom of the cover catches your eye.")
                    sleep(1)
                    print("Written by Bishan??")
                    sleep(1.5)
                    print("Preposterous. You don't have time for fakes claiming to be the famous Bishan.")
                    sleep(1.5)
                else:
                    print("\nYou glance at the cover and see 'Written by Bishan'.")
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
                    global knowledge
                    knowledge = True
            else:
                print("You try to do",choice,"but trip.\nYou forget what you were trying to do when you get up.")

def mpr():
    '''
    Item storage for player
    '''
    
    print("\nYou walk into the vast MPR. It's a bit chilly. There's a lot of open space around")
    print("You should be able to leave things here to come back for them later.")
    sleep(2)
    mprStorageCall()
    sleep(1)
    inventoryCall()
    sleep(1)
    
    has_items = True
    while has_items:
        action = raw_input("Do you want to (T)ake something, (D)rop something, or (L)eave the MPR?\n").lower()
        if action == "d":
            dropInMPR()
        elif action =="t":
            takeFromMPR()
        elif action == 'l':
            pass
        else:
            print ('You fumble with your hands, uncertain of what you want to do.')
        if len(inventory) == 0:
            has_items = False
        
    print("You exit into the hall.")
            
            
def dropInMPR():
    """
    Drops items in MPR
    """
    
    cont=True
    if len(inventory)>0:
        item = raw_input("What do you want to leave in the MPR?\n")
        while cont:
            inInventory = False
            for stuff in inventory:
                if stuff.lower() == item.lower():
                    inInventory = True
                    break
            if not inInventory:
                item = raw_input("You search yourself for it but you can't find it. Try another item.\n")
            else:
                print("You leave",item,"in the MPR.")
                inventory.remove(item)
                mprstorage.append(item)
                inventoryCall()
                mprStorageCall()
                cont=False
    else:
        print("\nYou don't have any items with you to leave in the MPR.")    
    
def takeFromMPR():
    """
    Take items from MPR
    """
    
    cont=True
    if len(mprstorage)>0:
        item = raw_input("What do you want to take from the MPR?\n")
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
        print("\nThere aren't any items to take from the MPR.")   

def mprStorageCall():
    """
    Prints things left in the mpr
    """
    
    if len(mprstorage)==0:
        print("Nothing is on the table.")
    elif len(mprstorage)==1:
        print("The",mprstorage[0],"is on the table.")
    else:
        statement = "There are a few things on the table: "
        for item in mprstorage:
            statement += item+", "
        print (statement)



def research():
    """
    Player obtains flashlight at piano
    Player obtains computer at computers, red-herring
    """
    
    memes = ["We are Number One", "Darude Sandstorm", "Never Gonna Give You Up", "Allstar"]
    if dennis and not cim_visited:
        cim()
    else:
        print("You walk in to the research wing and start walking around.")
        sleep(0.75)
        
        print("Do you want to head towards the (P)iano, get a laptop from",end="")
        choice = raw_input("a (C)omputer cart or (L)eave?\n").lower()
        sleep(0.75)
        
        while choice not in "pcl":
            choice = raw_input("You look around the vast wing. That's not here. What do you want to do?\n")
            sleep(0.75)
        
        if choice == "p":
            print("You suddenly decide that you want to play something on the piano, so you head towards the piano in the back.")
            sleep(0.75)
            piece = memes[randint(0,3)]
            if 'flashlight' not in inventory:
                print("Just as you are about to play a beautiful rendition of \"{},\" you see a flashlight on the ground.".format(piece,end=""))
                sleep(0.75)
                choice = raw_input("Do you want to pick it up?\n").lower()
                sleep(0.75)
                
                while choice not in 'yn':
                    print("You don't know what to do with your hands. Maybe you should've gotten more sleep.")
                    choice = raw_input("Do you want to pick up the flashlight?\n")
                    sleep(0.75)
        
                if choice == "y":
                    inventoryAdd('flashlight')
                else:
                    print("You decide not to pick up the flashlight.")
                    sleep(0.75)
            else:
                print ("You masterfully play \"{}.\" Beethoven would've cried. ".format(piece))
        elif choice == 'c':
            choice = raw_input("What computer cart (A-E) do you go to?\n").lower()
            sleep(0.75)
            
            if choice not in 'abcde':
                print("You look for that computer cart but it's not here")
            else:
                print("You head to cart",choice.upper(),"but you see that there is nothing to sign out a laptop with.")
                sleep(1)
                comp = raw_input("You look around... no one is looking. Do you take a computer?").lower
                if comp in 'yes':
                    inventoryAdd('computer')
                    print('You rebel.')
                    print("You open the computer but you realize the last person using it didn't charge the carts.")
                    print('Damn')
                else:
                    print ('Good boy.')
                sleep(2)
        
        print("You leave the research wing and head back to the hallways.")
        sleep(1)   

def courtyard():
    '''
    Initially dark, use flashlight to see
    Player obtains room key
    Player obtains penny, extra item
    '''
    
    if 'flashlight' in inventory:
        action = raw_input('''You walk out into the chilly night. You peer around in the darkness. You decide 
to turn on the flashlight. A glint appears in some bushes. Do you want to search the bushes?\n''').strip().lower()
        if action == 'yes' or action == 'y':
            print ('\nYou walk over to the bush and dig around.')
            sleep(1)
            for i in range(3):
                print ('.')
                sleep(0.67)
            if 'key' in inventory or 'key' in mprstorage:
                if 'penny' in inventory or 'penny' in mprstorage:
                    print("You didn't find anything. Go to sleep sometime geez...")
                else:
                    print("You didn't find anything. Just a worthless penny.")
                    penny = raw_input('Do you want to pick up the penny?\n').strip().lower()
                    if penny == 'y' or penny == 'yes':
                        inventoryAdd('penny')
                    else:
                        print("\nIt's only a penny. You go back to the halls.")
            else:
                print('You found a key!')
                inventoryAdd('key')
            
        else:
            print ("You decide that shiny glint isn't worth your time. You go back into the halls.")
    else:
        print ("It is the middle of the night. You cannot see anything. You go back into the halls.")

def cim():
    '''
    Initially locked, not accessible until certain game events
    Player obtains TSA Trophy
    '''
    
    global cim_visited
    if not cim_visited and dennis:
        print ("You walk over to the research wing and see a room to the north. Of course! How could you")
        print("have forgotten? It's the CIM room! You peer through the glass windows and see your email on an open screen.")
        sleep(1)
        print ("Quickly, you step inside the room.")
        sleep(1)
            readBoard()
            sleep(3)
        else:
            print ("You remember you forgot how to read in the second grade.")
            sleep(2)
            print('Ouch.')
            sleep(0.25)
        takeTrophy()
        print ("You should probably leave before Dennis finds you.")
        cim_visited = True
    else:
        print ('You walk back inside the quiet CIM room.')
        readBoard()
        sleep(2)
        if 'TSA Trophy' not in inventory:
           takeTrophy()
        else:
            print ("There's nothing here but empty desks and quietly running elevators in the back.")
            if randint(0,10) > 8:
                print('BANG WHFOOOOMM. You hear a loud whirring coming from the back. You realize its just the air compressor though.')
def readBoard():
    read = raw_input('You take in the old room and find some writing on the whiteboard. Do you want to read it?\n').strip().lower()
        if read == 'y' or read == 'yes':
            print(
            '''
                |===================================================|
                |                                                   |
                |                                                   |
                |                                                   |
                |           I'M GUARDING THE FRONT DOOR             |
                |                 YOU CAN'T ESCAPE                  |
                |          COME AND FACE YOUR PUNISHMENT            |
                |                                                   |
                |                               - Dennis            |
                |                                                   |
                |                                                   |
                |===================================================|
            ''',end='')
            print('\n',end='')

def takeTrophy():
    '''
    Take TSA Trophy
    '''
    
    tsa = True
    while tsa:
        take = raw_input("Inside the CIM room, you see a TSA Trophy. Do you want to (T)ake the trophy or (L)eave?\n").lower()
        if take == 't' or take == 'take' or take == 'take the trophy':
            inventoryAdd('TSA Trophy')
            tsa = False
            if 'TSA Trophy' in inventory:
                print('You feel the power of the second place TSA trophy. This might come in handy. You go back into the halls.')
        elif take == 'leave' or take == 'l':
            print ("You leave the nostalgic room and go back into the halls.")
            tsa = False
        else:
            print ("You try to do",take, "but you find you can't.")
            
def door():
    '''
    Front door, acts as quit option in beginning and win scene
    Locks when certain game events occur
    '''
    
    if not dennis:
        print ("You peer out the door. It is cold. And lonely. Baby.")
        quit = raw_input('Do you want to leave Low Tech?\n')
        if quit == 'y' or quit == 'yes':
            global end 
            end = True
        else:
            print ("You go back inside. You haven't sent your email yet.")
    elif dennis_riddle:
        dennisRiddle()
    else:
        dennisDoor()



def dennisDoor():
    '''
    Front door locked sequence
    '''
    
    print("As you bend the corner to the front door and freedom, you spot Dennis guarding the entrance.")
    sleep(1)
    print("You hear he's saying something.")
    sleep(3)
    print("He's raving about the mass mail.")
    sleep(1)
    if "TSA Trophy" in inventory: 
        print("You walk up with the TSA Trophy.")
        sleep(1)
        print("You see the delight in Mr. Dennis's face.")
        sleep(2)
        print("He starts to talk about TSA")
        sleep(3)
        print("*20 minutes later*")
        sleep(3)
        print("Dennis is talking about his steak dinner with Arvind.")
        sleep(3)
        print("*1 hour later*")
        sleep(3)
        print("You agree with Dennis that elevators are fascinating.")
        sleep(3)
        print("Maybe the TSA Trophy was a bit too effective.")
        sleep(2)
        print("2 hours in, Dennis has forgotten the mass mail.")
        sleep(2)
        print("Dennis is pleased.")
        sleep(1)
        print("He'll let you go... if you can answer his riddle.")
        sleep(2)
        print("You steel youself and prepare for whatever he can throw at you.")
        sleep(3)
        global dennis_riddle
        dennis_riddle=True
        dennisRiddle()
    else:
        print("You need something to get his mind off of the mass mail.")
        
def dennisRiddle():
    '''
    Unlocked by math textbook
    Player given 3 chances to answer riddle, else game over
    '''
    
    if knowledge:
        print("\nDennis gives his riddle:")
        sleep(1)
        print("What is 9 + 10?\n")
        sleep(2)
        print("With your newfound knowledge, you now understand Dennis' tough question.")
        counter=0
        while counter<3:
            if counter == 2:
                print ("You can tell Dennis is growing impatient. This is your last chance, bud.")
            answer = raw_input("What's your answer?")
            if answer == "19":
                print("Dennis nods his head and approves.")
                break
            elif answer == "21":
                print("Dennis, being a living legend himself, appreciates the meme.")
                break
            else:
                print("Dennis shakes his head no.")
            counter+=1
        if counter == 3:
            print ("Bishan appears from a hidden closet and looks at you with disapproval.")
            sleep(1)
            print ("You immediately die from shame.")
            sleep(2)
            print ('\n\nGAME OVER')
            print ('THANKS FOR PLAYING')
            global game
            game = False
        else:
            sleep(2)
            print("Dennis lets you out of Low Tech.")
            sleep(1)
            print("Just as you step out into the fresh air, the sun rises and shines down on you.")
            sleep(1)
            print("Your chest swells as you feel a sense of pride in your accomplishment.")
            sleep(1)
            print("You take out your phone to check just how long you spent in Low Tech.")
            sleep(2)
            print('Oh right.')
            sleep(2)
            print("You realize you could have used your phone to send the mass mail.")
            for i in range(3):
                print ('.')
                sleep(0.67)
            print("Huh neat.")
            sleep(3)
            win()
    else:
        print("Dennis gives his riddle:\n")
        sleep(1)
        print("What is 9+10?\n")
        for i in range(3):
            print ('.')
            sleep(0.67)
        sleep(0.33)
        print("You stand in silence, struggling to comprehend this monstrously difficult riddle.")
        sleep(2)
        print("The riddle is simply too hard. There's no way you can possibly understand it")
        print("much less solve it, with what you know now.")
        sleep(2)
        print("Dennis gives a jolly laugh and starts to talk about elevators again.")
        sleep(1)
        print("You walk back into the halls, still confused.")

def help():
    '''
    Prints valid command options for player
    '''
    
    if not dennis:
        print ('''
You're at a loss for what to do but see a handy dandy "How to Survive Low Tech" 
pamphlet on the floor. You pick it up and read.

Commands:
0-5: Go to corresponding room
 M : Pull up your map
 I : Pull up your inventory
 Q : Quit the game
 H : Help menu
 ''',end='')
    else:
        print ('''
You pull the pamphlet out of your pocket and read it again.
Commands:
0-6: Go to corresponding room
 M : Pull up your map
 I : Pull up your inventory
 Q : Quit the game
 H : Help menu... obviously
 ''',end='')
    print('\n',end='')
    sleep(2)

def win():
    '''
    Prints win statistics and ends game
    '''
    
    clearScreen()
    print("YOU WIN")
    sleep(1)
    print('\n')
    print('\t' + mail+ '\n')
    print('\t\t-' + name)
    sleep(1)
    print("THANKS FOR PLAYING")
    sleep(1)
    print ("\nItems Found: " + str(len(inventory)+ len(mprstorage)) + '/5')
    print("\"Dennis\"s Unleashed: 1/1")
    secret = str(int((name=='jesus') or (name=='chris')))
    print("Secrets Unlocked: "+secret+"/1")
    global startTime
    totalTime = (time()-startTime)
    mins = int(totalTime/60)
    seconds = int(totalTime%60)
    print("Time Elapsed: %02d:%02d" % (mins,seconds))
    global game
    game = False

def intro():
    '''
    Prints introductory scene
    '''
    
    for i in 'LOW TECH LOW ADVENTURE':
        print(i, end="")
        sleep(0.33)
    
    sleep(1)
    global name
    name = raw_input("What's your name?\n").strip()
    if name.lower() == 'chanas' or name.lower() == 'hanas' or name.lower() == 'chris':
        print ('Oh hello there Chris. How are you today? It would be great if we could get a 100. Thanks\n')
    if name.lower() == 'jesus':
        print ('Hello Bob Dennis\n')
    if name == '':
        print ('Wow such a creative name. I applaud your parents.\n')
        name = '[REDACTED]'
    sleep(1)
    for i in '''
    ()
    ||/////////////////////
    ||~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    ||~~ ~ ~ Low Tech~ ~ ~~
    ||~ ~ Low University~ ~
    ||~~ ~ ~ ~ ~ ~ ~ ~ ~ ~~
    ||/////////////////////
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ''':
        print (i,end='')
        sleep(0.025)
    print ('''\nYou stand outside your university, the famous Low Tech Low University,
the #1 STEM University for 8 times in the past 7 years. A sudden urge comes over you.
You feel like sending a mass mail. Today is your day.''')
    sleep(5)
    mapCall()
    print ('You enter the familiar halls.',end='')
    help()

def hall():
    '''
    Player decisions to go to rooms
    '''
    
    sleep(1)
    command = raw_input("Where do you want to go? (#) What do you want to do?\n").strip().lower()
    if command == 'm' or command == 'map':
        mapCall()
    elif command == 'i' or command == 'inv' or command == 'inventory':
        inventoryCall()    
    elif command == 'q' or command == 'quit' or command == 'exit':
        global end
        end = True
    elif command == 'h':
        sleep(1)
        help()
    elif command == '0' or command == 'front door':
        sleep(1)
        door()
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
    else:
        sleep(1)
        print ("You wander around the halls but you don't find that room. Strange. Use command h for help.")

#Main
if __name__ == '__main__':
    '''
    Starts game immediately when program runs
    '''
    
    startTime = time()
    clearScreen()
    intro()
    game
    while game:
        hall()
        end
        if end:
            quitting = raw_input('Are you sure you want to quit?\n').strip().lower()
            if quitting == 'yes' or quitting =='y':
                clearScreen()
                print ('You remember you can use your phone to send your mass mail.') 
                sleep(1.5)
                for i in range(3):
                    print ('.')
                    sleep(0.67)
                print ('Huh, neat.')
                sleep(1)
                print ('\n\nGAME OVER')
                print ('THANKS FOR PLAYING')
                game = False
            elif quitting == 'n' or quitting == 'n':
                print ('You doubted whether you can do this, however you shake your head and steel your resolve.')
                end = False
            else:
                print ('You confuse yourself by answering', quitting, 'to a yes or no question. You go back into the halls.')