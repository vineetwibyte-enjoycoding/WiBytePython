import tkinter as tk
import random

window = tk.Tk()
window.title("Minesweeper")
window.geometry("400x400")


Nrows = 9
Ncols = 9


def find_neighbors(r0, c0):
  nn = []
  # Return the list of neighbors of a given cell (r0, c0)
  temp_c = [c0-1, c0, c0+1]
  temp_r = [r0-1, r0, r0+1]

  # Remove the cells that are outside (for corner/edge cells)
  temp_c = [x for x in temp_c if x > -1 and x < Ncols]
  temp_r = [x for x in temp_r if x > -1 and x < Nrows]

  for r in temp_r:
    for c in temp_c:
      nn.append((r, c))

  nn.remove((r0, c0))
  return nn

colors = ['white', 'blue', 'green', 'red', 'dark blue', 'brown', 'cyan', 'black', 'gray']


def clickOn(r, c):
  
  if field[r][c] == 9:
    # Mine
    for kk in range(0, Nrows):
      for jj in range(Ncols):
          buttons[kk][jj]['state'] = 'disabled'
          buttons[kk][jj].config(relief=tk.SUNKEN)
          if field[kk][jj] == 9:
              buttons[kk][jj]["text"] = "*"
              buttons[kk][jj].config(background = 'red', disabledforeground = 'black')
                
  
  elif field[r][c] != 0:
    # Non-zero
    # display the number of mines in the neighborhood
    buttons[r][c]['state'] = 'disabled'
    buttons[r][c].config(relief=tk.SUNKEN)
    
    buttons[r][c]["text"] = str(field[r][c])
    buttons[r][c].config(disabledforeground=colors[field[r][c]])
  else:
    OpenUp(r, c)

  if checkWinner():
    print('Player Won')
    for location in locations:
      loc_xy = divmod(location, Ncols)
      buttons[loc_xy[0]][loc_xy[1]]['state'] = 'disabled'
      buttons[loc_xy[0]][loc_xy[1]].config(relief=tk.SUNKEN)
      buttons[loc_xy[0]][loc_xy[1]]["text"] = "*"
      buttons[loc_xy[0]][loc_xy[1]].config(background = 'green', disabledforeground = 'black')
    


def checkWinner():
  count = 0
  for r in range(Nrows):
    for c in range(Ncols):
      if buttons[r][c]["state"] == "disabled":
        count = count + 1    

  if count == Nrows*Ncols-Nmines:
    return True


def OpenUp(r, c):

  # Notice the function is first called on an empty cell, 
  # but on recursion this may be called by non-empty cells also 

  if buttons[r][c]["state"] == "disabled":
    return

  buttons[r][c]['state'] = 'disabled'
  buttons[r][c].config(relief=tk.SUNKEN)
  
  if field[r][c] == 0:
    nn = find_neighbors(r, c)
    for neighbors in nn:
      OpenUp(neighbors[0], neighbors[1])
  else:
    # A non-empty cell
    buttons[r][c]['text'] = str(field[r][c])
    buttons[r][c].config(disabledforeground=colors[field[r][c]])
    

  
  

buttons = []

# Create a Nrows x Ncols grid of buttons
for kk in range(Nrows):
  buttons.append([])
  for jj in range(Ncols):
    b = tk.Button(command = lambda r=kk, c=jj : clickOn(r, c))
    b.grid(row=kk, column = jj)
    b["width"] = 2
    b["font"] = 40
    b['text'] = ' '
    buttons[kk].append(b)





Nmines = 10
locations_all = [x for x in range(Nrows*Ncols)]
locations = random.sample(locations_all, Nmines)
#locations = [67, 72, 80, 79, 41, 26, 16, 5, 59, 6]
locations = [53, 62, 28, 38, 52, 25, 39, 64, 2, 69]
#locations = [53, 62, 28, 38, 52, 25, 39, 64, 2, 69]


field = [[0 for _ in range(Ncols)] for _ in range(Nrows)]

# Notice, the code above is equivalent to:
#field = []
#for jj in range(Nrows):
#  field.append([])
#  for _ in range(Ncols):
#    field[jj].append(0)

# Convert locations to a (x, y) tuple
for location in locations:
  loc_xy = divmod(location, Ncols)
  field[loc_xy[0]][loc_xy[1]] = 9; 

  # Update the field for this location 
  # find neighbors
  nn = find_neighbors(loc_xy[0], loc_xy[1])

  for neighbors in nn:
    if field[neighbors[0]][neighbors[1]] != 9:
      field[neighbors[0]][neighbors[1]] += 1




  

    


    
# b = tk.Button(command = lambda x=kk, y=jj: clickOn(x,y))