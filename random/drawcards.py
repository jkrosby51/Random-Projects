#
### poker3000tm
#

import random

# If True, then the card has already been used
cardCache = { 'AC':False,'AD':False,'AH':False,'AS':False, '2C':False,'2D':False,'2H':False,'2S':False, '3C':False,'3D':False,'3H':False,'3S':False, '4C':False,'4D':False,'4H':False,'4S':False, '5C':False,'5D':False,'5H':False,'5S':False, '6C':False,'6D':False,'6H':False,'6S':False, '7C':False,'7D':False,'7H':False,'7S':False, '8C':False,'8D':False,'8H':False,'8S':False, '9C':False,'9D':False,'9H':False,'9S':False, '10C':False,'10D':False,'10H':False,'10S':False, 'JC':False,'JD':False,'JH':False,'JS':False, 'QC':False,'QD':False,'QH':False,'QS':False, 'KC':False,'KD':False,'KH':False,'KS':False }

resetDecks = False
while resetDecks != True and resetDecks != False:
    userInput = input("Do you want to reset the deck each hand? True/False: ")
    if userInput.lower() == 'false' or userInput.lower() == 'f':
        resetDecks = False
    elif userInput.lower() == 'true' or userInput.lower() == 't':
        resetDecks = True
    else:
        print("That is not a valid response.")

def setDecks():
    cardCache = { 'AC':False,'AD':False,'AH':False,'AS':False, '2C':False,'2D':False,'2H':False,'2S':False, '3C':False,'3D':False,'3H':False,'3S':False, '4C':False,'4D':False,'4H':False,'4S':False, '5C':False,'5D':False,'5H':False,'5S':False, '6C':False,'6D':False,'6H':False,'6S':False, '7C':False,'7D':False,'7H':False,'7S':False, '8C':False,'8D':False,'8H':False,'8S':False, '9C':False,'9D':False,'9H':False,'9S':False, '10C':False,'10D':False,'10H':False,'10S':False, 'JC':False,'JD':False,'JH':False,'JS':False, 'QC':False,'QD':False,'QH':False,'QS':False, 'KC':False,'KD':False,'KH':False,'KS':False }

def drawCard():
    key = random.choice(list(cardCache.keys()))
    while cardCache[key] == True:
        key = random.choice(list(cardCache.keys()))
    cardCache[key] = True
    print(key)
    
drawCard()
        
    
    
