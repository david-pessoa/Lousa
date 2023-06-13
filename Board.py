from turtle import Turtle, Screen
cursor = Turtle()
screen = Screen()

def front():
    cursor.forward(10)
def back():
    cursor.backward(10)
def ClockWise():
    cursor.right(30)
def CounterClockWise():
    cursor.left(30)
def CleanScreen():
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()

screen.listen()
screen.onkey(front, "w")
screen.onkey(back, "s")
screen.onkey(ClockWise, "d")
screen.onkey(CounterClockWise, "a")
screen.onkey(CleanScreen, "c")
screen.exitonclick()