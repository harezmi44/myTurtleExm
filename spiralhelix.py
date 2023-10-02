import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light yellow")
turtle_screen.title("python spiralhelix")

turtle_instance=turtle.Turtle()
turtle_instance.color("red")
turtle_color=["red","yellow","green","purple","black","blue"]
turtle.speed(0)

for i in range(10):
    turtle_instance.color(turtle_color[i%6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)#
    #turtle_intance.left(i) bu komut sola kaydırır
#turtle.done() oyunlarda mainloop kullanılr
turtle.mainloop()