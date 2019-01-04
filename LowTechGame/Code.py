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
                            "]  ["   '''

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
                            "    "   '''

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
                            "]  ["   '''


#Global variables
dennis = False
main_door_riddle = False
has_key = False
inventory = []
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

def invCall():
    pass

def cse():
    pass
    
def math():
    pass

def mpr():
    pass

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
    room = raw_input("Which room will you go to? (#):\n").strip().lower()
    if room == 'm' or room == 'map':
        mapCall()
    elif room == 'i' or room == 'inv' or room == 'inventory':
        invCall()    
    elif room == 'q' or room == 'quit':
        global end
        end = True
    elif room not in ROOMS:
        sleep(1)
        print ("You wander around the halls but you don't find that room. Strange.")
    elif room == '1' or room == 'cse':
        sleep(1)
        cse()
    elif room == '2' or room == 'math':
        sleep(1)
        math()
    elif room == '3' or room == 'mpr':
        sleep(1)
        mpr()
    elif room == '4' or room == 'research wing':
        sleep(1)
        research()
    elif room == '5' or room == 'court yard':
        sleep(1)
        courtyard()
    elif room == '6' or room == 'cim':
        if not dennis:
            sleep(1)
            print ("You vaguely remember a room like that but you don't find that around the halls.")
        else:
            sleep(1)
            cim()
    

def intro():
    clear = lambda: os.system('cls')
    clear()
    
    INTRO_TIME=0.3
    print ('L',end='')
    sleep(INTRO_TIME)
    print ('O',end='')
    sleep(INTRO_TIME)
    print ('W',end='')
    sleep(INTRO_TIME)
    print (' ',end='')
    sleep(INTRO_TIME)
    print ('T',end='')
    sleep(INTRO_TIME)
    print ('E',end='')
    sleep(INTRO_TIME)
    print ('C',end='')
    sleep(INTRO_TIME)
    print ('H',end='')
    sleep(INTRO_TIME)
    print (' ',end='')
    sleep(INTRO_TIME)
    print ('L',end='')
    sleep(INTRO_TIME)
    print ('O',end='')
    sleep(INTRO_TIME)
    print ('W',end='')
    sleep(INTRO_TIME)
    print (' ',end='')
    sleep(INTRO_TIME)
    print ('A',end='')
    sleep(INTRO_TIME)
    print ('D',end='')
    sleep(INTRO_TIME)
    print ('V',end='')
    sleep(INTRO_TIME)
    print ('E',end='')
    sleep(INTRO_TIME)
    print ('N',end='')
    sleep(INTRO_TIME)
    print ('T',end='')
    sleep(INTRO_TIME)
    print ('U',end='')
    sleep(INTRO_TIME)
    print ('R',end='')
    sleep(INTRO_TIME)
    print ('E',end='')
    sleep(INTRO_TIME)
    
    global name
    name = raw_input("What's your name?\n").strip().lower()
    if name == 'chanas':
        print ('Oh hello there Chris. How are you today? It would be great if we could get a 100. Thanks\n')
    if name == 'jesus':
        print ('Hello Bob Dennis\n')
    if name == '':
        print ('Wow such a creative name. I applaud your parents.\n')
        name = '[REDACTED]'
    sleep(1)
    print ('''You stand outside your university, the famous Low Tech Low University,
the #1 STEM University for 8 times in the past 7 years. A sudden urge comes over you.
You feel like sending a mass mail. Today is your day.''')
    sleep(5)
    
    
    mapCall()
    print ('You enter the familiar halls.',end='')

def clearScreen():
    clear = lambda: os.system('cls')
    clear()
#Main
def main():
#if __name__ == '__main__':
    clearScreen()
    intro()
    game = True
    while game:
        hall()
        global end
        if end:
            quitting = raw_input('Are you sure you want to quit?\n').strip().lower()
            if quitting == 'yes' or quitting =='y':
                clearScreen()
                print ('\nYou remember you can use your phone to send your mass mail.') 
                sleep(1.5)
                print ('\nHuh, neat.\n\n')
                sleep(2)
                print ('GAME OVER')
                print ('THANKS FOR PLAYING')
                game = False
            elif quitting == 'n' or quitting == 'n':
                print ('You doubted whether you can do this, however you shake your head and steel your resolve.')
            else:
                print ('You confuse yourself by answering', quitting, 'to a yes or no question. You go back into the halls.')