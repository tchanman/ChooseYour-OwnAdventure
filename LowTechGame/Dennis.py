from __future__ import print_function
from time import sleep
inventory=["TSA Trophy"]
knowledge=True
def dennisDoor():
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
        dennis_riddle=True
        dennisRiddle()
    else:
        print("You need something to get his mind off of the mass mail.")
        
def dennisRiddle():
    if knowledge:
        print("Dennis gives his riddle:")
        sleep(1)
        print("What is 9+10?")
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
        else:
            sleep(2)
            print("Dennis lets you out of Low Tech.")
            sleep(2)
            print("You step out into the fresh air, proud of your accomplishment.")
            sleep(2)
            print("You take out your phone to check just how long you spent in Low Tech.")
            sleep(2)
            print("You realize you could have used your phone to send the mass mail.")
            
            print("Huh neat.")
    else:
        print("Dennis gives his riddle:")
        sleep(1)
        print("What is 9+10?")
        sleep(3)
        print("You stand in silence, struggling to comprehend this monstrously difficult riddle.")
        sleep(2)
        print("""The riddle is simply too hard. There's no way you can possibly understand it, 
much less solve it, with what you know now.""")
        sleep(2)
        print("Dennis gives a jolly laugh and starts to talk about elevators again.")
        sleep(1)
        print("You walk back into the halls, still confused.")
        
        
        