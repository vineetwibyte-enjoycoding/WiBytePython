import turtle

t = turtle.Turtle()


# square of side l, at x and y. 

def square(x, y, l):
  
  
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.goto(x+l, y)
  t.goto(x+l, y+l)
  t.goto(x, y+l)
  t.goto(x, y)

  if l > 10:
    #square(x+l, y+l, l/2)
    square(x + 3/4*l, y+ 1/4*l, l/2)
    square(x - 1/4*l, y+ 1/4*l, l/2)
    #square(x + 1/4*l, y- 1/2*l, l/2)

def branch(sz, level):
  if level > 0:
    t.forward(sz)
    t.right(30)
    branch(0.8*sz, level -1)
    t.right(-60)
    branch(0.8*sz, level -1)
    t.right(30)
    t.forward(-sz)

# Calling the functions

t.goto(0, 0)
square(-100, -100, 200)

input()
t.speed(0)
t.clear()
t.penup()
t.goto(0, -150)
t.pendown()
t.setheading(90)

branch(80, 10)



