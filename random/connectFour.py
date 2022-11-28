# 
# Connect Four(?)
#
import numpy

def setBoard():
  board = numpy.full((6,7), '_')
  return board

def printBoard(board):
  print()
  print(board)
  print("   0   1   2   3   4   5   6")

def findLowest(board, x):
  for y in range(5, -1, -1):
    #print(f"board[x][y] == {board[x][y]}")
    if board[y][x] == "_":
      return y
  return -1

def checkDraw(board):
  for x in range(len(board[0])):
    for y in range(len(board)):
      if board[y][x] == '_':
        return False
  return True

def checkWin(board):
  lenX = len(board[0])
  lenY = len(board)
  
  countX = 0
  countY = 0
  # Horizontal Checks
  for y in range(lenY):
    countX = 0
    countO = 0
    #print("heya")
    for x in range(lenX):
      #print("hello")
      #print(f"x{countX}")
      #print(f"o{countO}")
      if board[y][x] == 'X': 
        countX = countX + 1
        countO = 0
      elif board[y][x] == 'O': 
        countO = countO + 1
        countX = 0
      else:
        countX = 0
        countO = 0

      if countX >= 4:
        return 'X'
      if countO >= 4:
        return 'O'

  # Vertical Checks
  for x in range(lenX):
    countX = 0
    countO = 0
    for y in range(lenY):
      if board[y][x] == 'X': 
        countX = countX + 1
        countO = 0
      elif board[y][x] == 'O': 
        countO = countO + 1
        countX = 0
      else:
        countX = 0
        countO = 0

      if countX >= 4:
        return 'X'
      if countO >= 4:
        return 'O'
  # / diag
  for y in range(lenY):
    countX = 0
    countO = 0
    countX2 = 0
    countO2 = 0
    countX3 = 0
    countO3 = 0
    countX4 = 0
    countO4 = 0
    str = ""
    for x in range(y+1):
      str = str + board[lenY-x-1][y-x]
      # Top Half
      if board[y-x][x] == 'X': 
        countX = countX + 1
        countO = 0
      elif board[y-x][x] == 'O': 
        countO = countO + 1
        countX = 0
      else:
        countX = 0
        countO = 0
      # Bot Half
      if board[lenY-x-1][lenX-y+x-1] == 'X': 
        countX2 = countX2 + 1
        countO2 = 0
      elif board[lenY-x-1][lenX-y+x-1] == 'O': 
        countO2 = countO2 + 1
        countX2 = 0
      else:
        countX2 = 0
        countO2 = 0

      if board[y-x][lenX-x-1] == 'X':
        countX3 = countX3 + 1
        countO3 = 0
      elif board[y-x][lenX-x-1] == 'O':
        countO3 = countO3 + 1
        countX3 = 0
      else:
        countX3 = 0
        countO3 = 0

      if board[lenY-x-1][y-x] == 'X':
        #print("hi")
        countX4 = countX4 + 1
        countO4 = 0
      elif board[lenY-x-1][y-x] == 'O':
        countO4 = countO4 + 1
        countX4 = 0
      else:
        countX4 = 0
        countO4 = 0
        
      if countX >= 4 or countX2 >= 4 or countX3 >= 4 or countX4 >= 4:
        return 'X'
      if countO >= 4 or countO2 >= 4 or countO3 >= 4 or countO4 >= 4:
        return 'O'
      #print(countX4)
    #print(str)
  return None

play = True
while True:
  board = setBoard()
  
  while play:
    printBoard(board)
    winner = checkWin(board)
    if winner != None:
      print(f"Player {winner} wins!")
      if winner == 'X':
        print("X score up") #x score up
      if winner == 'O':
        print("O score up") #o score up
      break
    if checkDraw(board):
      print("It's a draw.")
      break
      
    badlyNamedBool = True # stopper 
    while badlyNamedBool == True:
      print()
      userInput = input("Player 1 (X), where would you like to play? ")
      try:
        userInput = int(userInput)
  
        if userInput >= 0 and userInput <= 6:
          if findLowest(board, userInput) != -1:
            badlyNamedBool = False
          else:
            print("That column is full.")
        else:
          print("Unknown column.")
      except:
        print("Must be an Integer (0-6).")
    board[findLowest(board, userInput)][userInput] = 'X'

    printBoard(board)
    winner = checkWin(board)
    if winner != None:
      print(f"Player {winner} wins!")
      if winner == 'X':
        print("X score up") #x score up
      if winner == 'O':
        print("O score up") #o score up
      break
        
    
    badlyNamedBool = True
    while badlyNamedBool == True:
      print()
      userInput = input("Player 2 (O), where would you like to play? ")
      try:
        userInput = int(userInput)
  
        if userInput >= 0 and userInput <= 6:
          if findLowest(board, userInput) != -1:
            badlyNamedBool = False
          else:
            print("That column is full.")
        else:
          print("Unknown column.")
      except:
        print("Must be an Integer (0-6).")
    board[findLowest(board, userInput)][userInput] = 'O'

  print()
  userInput = "e"
  while userInput.lower() not in ('y', 'n'):
    userInput = input("Would you like to play again? (y/n): ")
    if userInput.lower() == 'n':
      play = False
    elif userInput.lower() == 'y':
      play = True 
    else:
      print("That is not a valid response.")
  if not play: break
    
