import turtle

t = turtle.Turtle()
s= turtle.Screen()

s.bgcolor("pink")
t.hideturtle()
t.goto(0, -10)

t.pensize(3)
t.color("red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-160, 135)
t.pendown()
t.color("white")
t.write("JANGAN BADMOOD YAA", font=("Verdana", 18, "bold"))

t.penup()
t.goto(-100, 165)
t.pendown()
t.color("white")
t.write("PUPUT CANTIKK", font=("Verdana", 18, "bold"))

t.penup()
t.goto(-25, 100)
t.pendown()
t.color("white")
t.write("ILY❤️", font=("Verdana", 18, "bold"))

turtle.done()