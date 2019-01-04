'''
Low Tech Low Game
Player comes to LTLU to send a mass mail and finds hidden secrets in this thrilling adventure
'''

#Constants

def map():
    if dennis:
        print MAP_2
    else:
        print MAP_1
    
def hall():
    rooms = ['1','2','3','4','5','6',"cse","court yard", "math", "mpr", "research wing", "cim"]
    
    room = input("Which room will you go to? (#):\n ").strip().lower()
    if room not in rooms:
        pass