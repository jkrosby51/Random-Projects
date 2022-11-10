players = [["Dealer", 0, []]]

inputCheck = False
while not inputCheck:
    try:
        playerCount = int(input("How many players? (1-8): "))
        if playerCount > 0 and playerCount < 9:
            inputCheck = True
        else: print("Must be within 1-8.")
    except: print("Must be an Integer 1-8.")

for i in range(playerCount+1):
    ### [Name, Score, hand]
    players.append([f"Player {i+1}", 0, []])
    print(players[i])
