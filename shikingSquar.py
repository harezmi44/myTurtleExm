import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("python shiking squar")

turtle_instance=turtle.Turtle()
turtle_instance.color("yellow")

def shirikingsquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size=size-5


shirikingsquare(150)
shirikingsquare(130)
shirikingsquare(110)
shirikingsquare(90)
shirikingsquare(80)
shirikingsquare(70)
shirikingsquare(50)
shirikingsquare(20)
shirikingsquare(-10)
shirikingsquare(-30)
shirikingsquare(-50)

turtle.done()

