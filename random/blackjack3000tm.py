#
# blackjack3000tm
#

##  TO DO:
##  - fix bugs

import random

# If True, then the card has already been used
cardCache = {
  'Ac': False,
  'Ad': False,
  'Ah': False,
  'As': False,
  '2c': False,
  '2d': False,
  '2h': False,
  '2s': False,
  '3c': False,
  '3d': False,
  '3h': False,
  '3s': False,
  '4c': False,
  '4d': False,
  '4h': False,
  '4s': False,
  '5c': False,
  '5d': False,
  '5h': False,
  '5s': False,
  '6c': False,
  '6d': False,
  '6h': False,
  '6s': False,
  '7c': False,
  '7d': False,
  '7h': False,
  '7s': False,
  '8c': False,
  '8d': False,
  '8h': False,
  '8s': False,
  '9c': False,
  '9d': False,
  '9h': False,
  '9s': False,
  '10c': False,
  '10d': False,
  '10h': False,
  '10s': False,
  'Jc': False,
  'Jd': False,
  'Jh': False,
  'Js': False,
  'Qc': False,
  'Qd': False,
  'Qh': False,
  'Qs': False,
  'Kc': False,
  'Kd': False,
  'Kh': False,
  'Ks': False
}

cardVal = {
  'Ac': 11,
  'Ad': 11,
  'Ah': 11,
  'As': 11,
  '2c': 2,
  '2d': 2,
  '2h': 2,
  '2s': 2,
  '3c': 3,
  '3d': 3,
  '3h': 3,
  '3s': 3,
  '4c': 4,
  '4d': 4,
  '4h': 4,
  '4s': 4,
  '5c': 5,
  '5d': 5,
  '5h': 5,
  '5s': 5,
  '6c': 6,
  '6d': 6,
  '6h': 6,
  '6s': 6,
  '7c': 7,
  '7d': 7,
  '7h': 7,
  '7s': 7,
  '8c': 8,
  '8d': 8,
  '8h': 8,
  '8s': 8,
  '9c': 9,
  '9d': 9,
  '9h': 9,
  '9s': 9,
  '10c': 10,
  '10d': 10,
  '10h': 10,
  '10s': 10,
  'Jc': 10,
  'Jd': 10,
  'Jh': 10,
  'Js': 10,
  'Qc': 10,
  'Qd': 10,
  'Qh': 10,
  'Qs': 10,
  'Kc': 10,
  'Kd': 10,
  'Kh': 10,
  'Ks': 10
}
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
  global cardCache
  cardCache = {
    'Ac': False,
    'Ad': False,
    'Ah': False,
    'As': False,
    '2c': False,
    '2d': False,
    '2h': False,
    '2s': False,
    '3c': False,
    '3d': False,
    '3h': False,
    '3s': False,
    '4c': False,
    '4d': False,
    '4h': False,
    '4s': False,
    '5c': False,
    '5d': False,
    '5h': False,
    '5s': False,
    '6c': False,
    '6d': False,
    '6h': False,
    '6s': False,
    '7c': False,
    '7d': False,
    '7h': False,
    '7s': False,
    '8c': False,
    '8d': False,
    '8h': False,
    '8s': False,
    '9c': False,
    '9d': False,
    '9h': False,
    '9s': False,
    '10c': False,
    '10d': False,
    '10h': False,
    '10s': False,
    'Jc': False,
    'Jd': False,
    'Jh': False,
    'Js': False,
    'Qc': False,
    'Qd': False,
    'Qh': False,
    'Qs': False,
    'Kc': False,
    'Kd': False,
    'Kh': False,
    'Ks': False
  }


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
  
def printCards(players, ifWin):
    if not ifWin:
        str = "[ x "
        for card in players[0][2][1:]:
          str = str + f"{card} "
        print(f"{players[0][0]}: {str}]")
        for i in range(len(players)-1):
            str = "[ "
            for card in players[i+1][2]:
              str = str + f"{card} "
            print(f"{players[i+1][0]}: {str}]")
    else:
        str = "[ "
        for card in players[0][2]:
          str = str + (f"{card} ")
        print(f"{players[0][0]}: {str}]")
        for i in range(len(players)-1):
            str = "[ "
            for card in players[i+1][2]:
              str = str + f"{card} "
            print(f"{players[i+1][0]}: {str}]")
        

def handVal(hand):
    val = 0
    aces = 0
    for card in hand:
        if "A" in card:
            aces = aces + 1

    for card in hand:
        val = val + cardVal[card]
    for i in range(aces):
        if val > 21:
            val = val - 10
    return val

def checkBust(players):
    for i in range(len(players)):
        #print(handVal(players[i][2]))
        if handVal(players[i][2]) > 21:
            if i == 0: 
                print(f"The dealer went over 21.")
                for player in players:
                    player[1] = player[1] + 1
                return(player[0])
            elif i == 1:
                print(f"The player went over 21.")
                players[0][1] = players[0][1] + 1
                return("The Dealer")
    return(-1)
    
def checkWinner(players):
    x = checkBust(players)
    if x != -1:
        return x
    scores = []
    for i in range(len(players)):
        scores.append(handVal(players[i][2]))
    if scores[0] > scores[1]:
        dealerScore = dealerScore + 1
        return("The Dealer")
    elif scores[1] > scores[0]:
        playerScore = playerScore + 1
        return("The Player")
    else:
        if len(players[i][2]) <= len(players[i+1][2]):
            dealerScore = dealerScore + 1
            return("The Dealer")
        else:
            playerScore = playerScore + 1
            return("The Player")
        
def blackJack(playerCount):
    players = [["Dealer", 0, []]]

    inputCheck = False
    
    for i in range(playerCount):
        ### [Name, Score, hand]
        players.append([f"Player {i+1}", 0, []])
        #print(players[i])
    play = True
    while play:
      badlyNamedBool = True
      for player in players:
          player[2] = dealHand(2)
    
     
      while True:
        printCards(players, False)
    
        winner = checkBust(players)
        if winner != -1:
            print()
            printCards(players, True)
            print()
            print(f"{winner} Wins!")
            print()
            for player in players:
                print(f"{player[0]}'s Score: {player[1]}")
            break
        if not badlyNamedBool:
            while handVal(players[0][2]) <= 16:
                players[0][2].append(drawCard())
                printCards(players, False)
            print()
            printCards(players, True)
            print()
            print(f"{checkWinner(players)} wins the hand!")
            print()
            for player in players:
                print(f"{player[0]}'s Score: {player[1]}")
            winner = -1
            break
        
        if handVal(players[0][2]) <= 16:
          players[0][2].append(drawCard())
        
        for i in range(len(players)-1):
            userInput = "e"
            while userInput.lower() not in ('y', 'n'):
                userInput = input(f"{players[i+1][0]}, Hit? (y/n): ")
                if userInput.lower() == 'no' or userInput.lower() == 'n':
                    badlyNamedBool = False
                elif userInput.lower() == 'yes' or userInput.lower() == 'y':
                    badlyNamedBool = True
                else:
                    print("That is not a valid response.")
            if badlyNamedBool: 
                players[i+1][2].append(drawCard())
        
      print()
      userInput = "e"
      while userInput.lower() not in ('y', 'n'):
        userInput = input("Play another hand? (y/n): ")
        if userInput.lower() == 'n':
            play = False
            print()
            print(f"Final score:")
            for player in players:
                print(f"{player[0]}'s Score: {player[1]}")
            print()
        elif userInput.lower() == 'y':
            play = True 
        else:
            print("That is not a valid response.")
      

inputCheck = False
while not inputCheck:
    try:
        playerCount = int(input("How many players? (1-8): "))
        if playerCount > 0 and playerCount < 9:
            inputCheck = True
        else: print("Must be within 1-8.")
    except: print("Must be an Integer 1-8.")
    
blackJack(int(playerCount))
