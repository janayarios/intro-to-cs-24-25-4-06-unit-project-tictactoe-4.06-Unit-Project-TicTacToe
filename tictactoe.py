# Tic-Tac-Toe

import math

board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

################## Gobal Variables ##################
turn = 1
player = 'X'
winner = False
############## Win Conidition Functions #############

def checkHorizontal(_board):
  for row in _board: 
      if row[0]==row[1]==row[2]:
       return player

def checkVerticle(_board, _move):
  if _board[0][_move] == _board[1][_move] == _board[2][_move]:
    return player

def checkDiagonal(_board):
  if _board[0][0] == _board[1][1] == _board[2][2] or _board[0][2] == _board[1][1] == _board[2][0]:
    return player

#################### Game Loop ######################
while not winner and turn < 10:
  if turn % 2 == 0:
    player = "0"
  else:
    player = "X"
  move = int(input(f"Where do you want to place your {player}?: "))
  y = (move % (len(board[0]))) - 1
  x = int(math.ceil(move / len(board[y])) - 1)
  if move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or board[x][y] in ["X", "0"]:
    print("You can't go there!")
  else:
    board[x][y] = player

    # Display Board
    for row in board:
      print(row)

    # Check horizontal win
    winner = checkHorizontal(board)
    winner = checkVerticle(board, y)
    winner = checkDiagonal(board)
   
    # Check vertical win


    # Check diagonal win

    turn += 1

if not winner:
  print("It's a draw!")
else:
  print(f"{player} wins!")
