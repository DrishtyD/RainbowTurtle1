# rainbow
# using turtle programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'pink', 'white', 'indigo', 'violet', 'silver', 'gold', 'beige']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(speed=10)
for x in range(360):

    t.pencolor(colors[x % 13])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
