#
### poker3000tm
#

import random

# If True, then the card has already been used
cardCache = { 'AC':False,'AD':False,'AH':False,'AS':False, '2C':False,'2D':False,'2H':False,'2S':False, '3C':False,'3D':False,'3H':False,'3S':False, '4C':False,'4D':False,'4H':False,'4S':False, '5C':False,'5D':False,'5H':False,'5S':False, '6C':False,'6D':False,'6H':False,'6S':False, '7C':False,'7D':False,'7H':False,'7S':False, '8C':False,'8D':False,'8H':False,'8S':False, '9C':False,'9D':False,'9H':False,'9S':False, '10C':False,'10D':False,'10H':False,'10S':False, 'JC':False,'JD':False,'JH':False,'JS':False, 'QC':False,'QD':False,'QH':False,'QS':False, 'KC':False,'KD':False,'KH':False,'KS':False }

"""
resetDecks = -1
while resetDecks != True and resetDecks != False:
    userInput = input("Do you want to reset the deck each hand? (y/n): ")
    if userInput.lower() == 'no' or userInput.lower() == 'n':
        resetDecks = False
    elif userInput.lower() == 'yes' or userInput.lower() == 'y':
        resetDecks = True
    else:
        print("That is not a valid response.")
"""

def setDecks():
    cardCache = { 'AC':False,'AD':False,'AH':False,'AS':False, '2C':False,'2D':False,'2H':False,'2S':False, '3C':False,'3D':False,'3H':False,'3S':False, '4C':False,'4D':False,'4H':False,'4S':False, '5C':False,'5D':False,'5H':False,'5S':False, '6C':False,'6D':False,'6H':False,'6S':False, '7C':False,'7D':False,'7H':False,'7S':False, '8C':False,'8D':False,'8H':False,'8S':False, '9C':False,'9D':False,'9H':False,'9S':False, '10C':False,'10D':False,'10H':False,'10S':False, 'JC':False,'JD':False,'JH':False,'JS':False, 'QC':False,'QD':False,'QH':False,'QS':False, 'KC':False,'KD':False,'KH':False,'KS':False }

def drawCard():
    key = random.choice(list(cardCache.keys()))
    while cardCache[key] == True:
        key = random.choice(list(cardCache.keys()))
    cardCache[key] = True
    return key
    
def dealHand(num):
    hand = [drawCard()]
    for i in range(num - 1):
        hand.append(drawCard())
    return hand

def checkWinner(allHands, sharedCards):
    winner = "idfk lol"
    return winner
    

def texasHoldem(players):
    print(▀█▀ █▀▀ ▀▄▀ ▄▀█ █▀   █░█ █▀█ █░░ █▀▄   ▀ █▀▀ █▀▄▀█)
    print(░█░ ██▄ █░█ █▀█ ▄█   █▀█ █▄█ █▄▄ █▄▀   ░ ██▄ █░▀░█)
    
    
    handSize = 2
    sharedSize = 5
    playing = True
    while playing: 
        setDecks()
        
        sharedCards = dealHand(sharedSize)
        print(f"Shared Cards: {sharedCards}")
        
        allHands = [dealHand(handSize)]
        for i in range(players-1):
            allHands.append(dealHand(handSize))
        for hand in allHands:
            print(hand)
            
        print()   
        print(f"{checkWinner(allHands, sharedCards)} wins the round!")
        print()
        
        playing = -1 
        while playing != True and playing != False:
            userInput = input("Another Round? (y/n): ")
            if userInput.lower() == 'no' or userInput.lower() == 'n':
                playing = False
            elif userInput.lower() == 'yes' or userInput.lower() == 'y':
                playing = True
            else:
                print("That is not a valid response.")
        
        
numPlayers = input("How many players? ")
print()
texasHoldem(int(numPlayers))

    


        
    
    
