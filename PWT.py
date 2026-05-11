"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle


t = turtle.Turtle()

input()

#t.speed(05
#t.goto(-50, -100)

t.penup()
t.fillcolor("yellow")
t.pencolor("black")
t.pensize(3)
t.begin_fill()
t.goto(-100, 100)
t.pendown()
t.goto(100, 100)
t.goto(100, -100)
t.goto(-100, -100)
t.goto(-100, 100)
t.end_fill()


t.penup()
t.goto(0, 30)
t.pensize(1)
t.pendown()
t.fillcolor("white")
t.setheading(90)
t.begin_fill()
t.circle(25)
t.circle(-25)
t.end_fill()

t.penup()
t.goto(-15, 30)
t.dot(20)
t.goto(15, 30)
t.dot(20)

t.goto(35, -20)
t.pencolor("orange")
t.pensize(8)
t.pendown()
t.setheading(-90)
t.circle(-35, 180)
t.hideturtle()

#t.end_fill()

#t.penup()
#t.goto(-50, 50)
#t.fillcolor("white")
#t.begin_fill()
#t.circle(50)
#t.end_fill()
#t.dot(20)
#t.penup()

#t.goto(50, 50)
#t.dot(20)

#t.begin_fill()
#t.pendown()
#t.circle(25.0, 120)

#t.end_fill()
#def draw_rectangle(x0, y0, len, hgt, clr):
#    t.color(clr)
#    t.begin_fill()
#    draw_line(x0, y0, x0+len, y0)
#    draw_line(x0+len, y0, x0+len, y0+hgt)
#    draw_line(x0+len, y0+hgt, x0, y0+hgt)
#    draw_line(x0,y0+hgt, x0, y0)
#    t.end_fill()



#t.clear()


#draw_rectangle(-100.0, -150.0, 50, 20.0, 'blue')
#draw_rectangle(-30.0, -150.0, 50, 20.0, 'blue')
#draw_rectangle(-25.0, -50.0, 15, -100.0, 'grey')
#draw_rectangle(-55.0, -50.0, -15,-100.0, 'grey')
#draw_rectangle(-90.0, 100.0, 100,-150.0, 'red')
#draw_rectangle(-150.0, 70.0, 60, 15.0, 'grey')
#draw_rectangle(-150.0, 110.0, 15, -40.0, 'grey')
#draw_rectangle(10.0, 70.0, 60, 15.0, 'grey')
#draw_rectangle(55.0, 110.0, 15, -40.0, 'grey')
#draw_rectangle(-50.0, 120.0, 15, -20.0, 'grey')
#draw_rectangle(-85.0, 170.0, 80, -50.0, 'green')




#color('yellow', 'red')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()



#for c in ['red', 'green', 'yellow', 'blue']:
#    t.color(c)
#    t.forward(75)
#    t.left(90)
