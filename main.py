import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Pyton Turtle")
turtle_instance = turtle.Turtle()
'''
spuar
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle.done()
'''
''''
2. yol squar

for i in range(4):
  
  turtle_instance.forward(200)
  turtle_instance.left(90)
turtle.done()
'''
'''
#star
for i in range(5):
  turtle_instance.left(144)
  turtle_instance.forward(200)
turtle.done()

'''
#ploygon
side_num=8
agle=360.0/side_num
side_leng=100
for i in range(side_num):
  turtle_instance.left(agle)
  turtle_instance.forward(side_leng)
turtle.done()

