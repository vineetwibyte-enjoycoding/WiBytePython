import turtle
import random

# Game of Connect 4 

screen = turtle.Screen()
screen.setup(800,700)
screen.setworldcoordinates(-500,-500,500,500)
screen.title("Connect 4")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0) # -- Immediate draw and update
t = turtle.Turtle()
t.up()
#score.hideturtle()

def draw_rectangle():
  t.goto(-350, -100)
  t.fillcolor('skyblue')
  t.pendown()
  t.begin_fill()
  t.goto(-350, 500)
  t.goto(350, 500)
  t.goto(350, -100)
  t.goto(-350, -100)
  t.end_fill()
  t.up()
# 6 rows and 7 columns

Nrows = 6
Ncols = 7

def draw_circle(x, y, r, fillcolor):
  # Draw a circle at (x, y), radius r and fill color 
  t.goto(x, y)
  t.setheading(-90)
  t.fillcolor(fillcolor)
  t.begin_fill()
  t.circle(r)
  t.end_fill()


board = []

nRows = 6
nCols = 7

board = [[0 for i in range(nCols)] for j in range(nRows)]

# The equivalent for loop for the code above
#for i in range(nRows):
#  row = []
#  for j in range(nCols):
#      row.append(0)
# board.append(row)

def draw_board():
  draw_rectangle()

  for kk in range(Nrows):
    for jj in range(Ncols):
      if board[kk][jj] == 0:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'white')
      if board[kk][jj] == 1:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'red')
      if board[kk][jj] == 2:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'blue')


def all_same(cells, value):
  # Return TRUE if ALL values of the list 
  # cells are equal to value
  allequal = True
  
  for cell in cells: 
    if cell != value:
      allequal = False
      break

  return allequal
  

def checkHorizontalWinner(value):
  # Scan entire board for horizontal wins
  winner = False
  for jj in range(nRows):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj][kk+cnt])
        
      if all_same(cells, value):
        winner = True
        break

  return winner

def checkVerticalWinner(value):
  winner = False
  # Scan entire board for vertical wins
  for jj in range(3):
    for kk in range(nCols):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk])
      if all_same(cells, value):
        winner = True
        break

  return winner

def checkDiagonalOneWinner(value):

  winner = False
  # Check for cells sloping upwards
  for jj in range(3,nRows,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj-cnt][kk+cnt])
      if all_same(cells, value):
        winner = True
        break

  return winner


def checkDiagonalTwoWinner(value):

  winner = False
  # Check for cells sloping downwards
  for jj in range(0,3,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk+cnt])
      if all_same(cells, value):
        winner = True
        break

  return winner







def checkwinner(value):
  
  winner = checkHorizontalWinner(value)
  if not winner:
    # No winner yet
    winner = checkVerticalWinner(value)
    if not winner:
      winner = checkDiagonalOneWinner(value)
      if not winner:
        winner = checkDiagonalTwoWinner(value)
        
  return winner

      
    


def lowest_row(col):
  # Find the lowest available row in a given column
  r = -1
  for kk in range(Nrows-1, -1, -1):
    if board[kk][col] == 0:
      r = kk
      break
      
  return r


def play(x, y):

  global turn, gameOver
  if gameOver:
    return
  
  col = int((x + 350)//100) # determine the column (Depending on the click location)
  
  if col < 0: 
    col = 0
  if col > Ncols-1:
    col = Ncols - 1

  avail_cols = find_open_cols()

  if col in avail_cols:
    # find the lowest available row in that column
    available_row = lowest_row(col)
    board[available_row][col] = 1
  
    draw_board()
    # Check for winner and accordingly decide whether next player or game over
    if checkwinner(1):
      gameOver = True
      print('Player Wins')
    else:
      turn = 2
  
  if turn == 2:
    playc()
  
  
  
def find_open_cols():
  open_cols = [m for m in range(Ncols)]
  full_cols = []

  # Remove those columns that are full
  for col in open_cols:
    if lowest_row(col) == -1:
      full_cols.append(col)

  for col in full_cols:
    open_cols.remove(col)

  return open_cols

def display_board():
  for kk in range(nRows):
    print(board[kk])



def playc():
  global turn, gameOver
  # Find which columns are available
  # Consider all the columns
  cols_avail = find_open_cols()
  #print(cols_avail)
  # Pick up a random column from those that are open
  if len(cols_avail) > 0:
    col = random.choice(cols_avail)
    available_row = lowest_row(col)
    board[available_row][col] = 2  
  
  draw_board()
  # Check for winner and accordingly decide whether next player or game over
  if checkwinner(2):
    gameOver = True
    print('Computer Wins')
  else:
    turn = 1


gameOver = False   
turn = 1


draw_board()
screen.onclick(play)