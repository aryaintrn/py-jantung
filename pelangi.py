import turtle
sc = turtle.Screen()
pen = turtle.Turtle()

def semi_circle(col,rad,val):
    pen.color(col)
    pen.circle(rad,-180)
    pen.up()
    pen.setpos(val,0)
    pen.down()
    pen.right(180)
color = ['red','orange','yellow','green','blue','purple']
sc.setup(600,600)
sc.bgcolor('pink')
pen.right(90)
pen.width(10)
pen.speed(7)
for i in range(7):
    semi_circle(color[i], 10*(i+8),-10*(i+1))

pen.hideturtle()
pen.done()