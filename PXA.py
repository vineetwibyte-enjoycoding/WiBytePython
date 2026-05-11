"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
ts = t.getscreen()


def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)

def draw_rectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    t.end_fill()

# Make the drawing instant
ts.tracer(0)

# Draw 1 row of rectangles. 
n_cols = 20 
x_val  = -150
y_val  = 0

for jj in range(n_cols):
    if jj < 5:
       draw_rectangle(x_val, y_val, 20, 20, "red")
    elif jj > 4 and jj < 15:
       draw_rectangle(x_val, y_val, 20, 20, "blue")
    else:
       draw_rectangle(x_val, y_val, 20, 20, "green")
    x_val = x_val + 20

t.hideturtle()    


# input()
# Now show the drawing
ts.update()
input()
t.clear()

# Create a grid of squares
n_rows = 20
y_val = 150
x_val = -150
ts.tracer(0)
for kk in range(n_rows): 
    for jj in range(n_cols):
        if kk==jj:
           draw_rectangle(x_val, y_val, 15, 15, "red")
        else:
           draw_rectangle(x_val, y_val, 15, 15, "green")
        x_val = x_val + 15
    x_val = -150
    y_val = y_val - 15

ts.update()

input()

t.clear()
t.hideturtle()



ts.tracer(0)
n_rows = 20; 
n_cols = 20; 
x_val = -150; 
y_val = 150

# Create MARIO
# color_list is a list that contains WHICH color we want on the specific pixel of a given row. 
# 1 = white, 2 = red, 3 = brown, 4= gold, 5 = black, 6 = blue. 

# kk is the row index
# Define the color list per row
for kk in range(n_rows):
    if kk==0 or kk==1:
        color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif kk==2:
        color_list = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    elif kk==3:
        color_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
    elif kk==4:
        color_list = [1, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 5, 4, 1, 1, 1, 1, 1, 1, 1]
    elif kk==5:
        color_list = [1, 1, 1, 1, 1, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 1, 1, 1, 1, 1]
    elif kk==6:
        color_list = [1, 1, 1, 1, 1, 3, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 1, 1, 1, 1]
    elif kk==7:
        color_list = [1, 1, 1, 1, 1, 1, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1, 1, 1, 1, 1]
    elif kk==8:
        color_list = [1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1]
    elif kk==9:
        color_list = [1, 1, 1, 1, 1, 1, 2, 2, 6, 2, 2, 6, 2, 2, 1, 1, 1, 1, 1, 1]
    elif kk==10:
        color_list = [1, 1, 1, 1, 1, 2, 2, 2, 6, 2, 2, 6, 2, 2, 2, 1, 1, 1, 1, 1]
    elif kk==11:
        color_list = [1, 1, 1, 1, 2, 2, 2, 2, 6, 6, 6, 6, 2, 2, 2, 2, 1, 1, 1, 1]
    elif kk==12:
        color_list = [1, 1, 1, 1, 4, 4, 2, 6, 4, 6, 6, 4, 6, 2, 4, 4, 1, 1, 1, 1]
    elif kk==13:
        color_list = [1, 1, 1, 1, 4, 4, 4, 6, 6, 6, 6, 6, 6, 4, 4, 4, 1, 1, 1, 1]
    elif kk==14:
        color_list = [1, 1, 1, 1, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 1, 1, 1, 1]
    elif kk==15:
        color_list = [1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 6, 6, 6, 1, 1, 1, 1, 1, 1]
    elif kk==16:
        color_list = [1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1]
    elif kk==17:
        color_list = [1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1]
    else:
        color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        
    for jj in range(n_cols):

        if color_list[jj]==1:
            draw_rectangle(x_val, y_val, 15, 15, "white")
        elif color_list[jj]==2:
            draw_rectangle(x_val, y_val, 15, 15, "red")
        elif color_list[jj]==3:
            draw_rectangle(x_val, y_val, 15, 15, "brown")
        elif color_list[jj]==4:
            draw_rectangle(x_val, y_val, 15, 15, "gold")
        elif color_list[jj]==5:
            draw_rectangle(x_val, y_val, 15, 15, "black")
        else:
            draw_rectangle(x_val, y_val, 15, 15, "blue")    
        x_val = x_val + 15
    x_val = -150
    y_val = y_val - 15

t.hideturtle()

#elif kk+jj>9 and kk+jj<29:
        #   draw_rectangle(x_val, y_val, 15, 15, "blue")



ts.update()    
ts.mainloop()

# t.done()
    
#x_val = -100
#y_val = y_val - 10


#for jj in range(10):
#    for kk in range(10):
#        if kk < 5:
#            draw_rectangle(kk*15, -100, 15, 15, "orange")
#        else:
#            draw_rectangle(kk*15, -100, 15, 15, "green")
         
#ts.update()        
#ts.tracer(0)

#t.speed(1)

#for kk in range(100):
#   t.forward(50)
#   t.back(50)
#   t.left(31)

#ts.update()
    
#t.goto(0, 0)
#t.goto(100, 100)
#t.goto(200, 0)

#ts.update()
