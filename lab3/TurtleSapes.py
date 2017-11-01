import turtle
turtle.left(180)
for i in range(5):
	turtle.forward(100)
	turtle.left(72)
turtle.penup()

turtle.goto(-100,0)
turtle.left(180)	

turtle.pendown()
def triangles():
	for i in range(3):
		turtle.forward(100)
		turtle.left(120)
triangles()
def star():	
	turtle.left(192)
	triangles()
for i in range(5):
	star()








turtle.mainloop()

