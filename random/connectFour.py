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
  for y in range(5, 0, -1):
    #print(f"board[x][y] == {board[x][y]}")
    if board[y][x] == "_":
      return y
  return -1

while True:
  board = setBoard()
  
  play = True
  while play:
    printBoard(board)
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
            
    
    
