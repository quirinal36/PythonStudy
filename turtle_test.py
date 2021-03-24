import turtle
window = turtle.Screen()

x = 100

geoff = turtle.Turtle()
geoff.forward(x)

turtle.setpos(x, 0)
turtle.write('hello')
window.exitonclick()