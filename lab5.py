from turtle import*
import random
#colormode(255)
#class Square(Turtle):
	#def __init__(self,size):
		#Turtle.__init__(self)
		#self.shapesize(size)
		#self.shape("square")
	#def random_color(self):
		#r = random.randint(0,255)
		#g = random.randint(0,255)
		#b = random.randint(0,255)
		#self.color(r,g,b)

			
#square1=Square(size=10)
#square1.random_color()
#print(square1)

#class Rectangle(Turtle):
	#def __init__(self,width,height):
		#Turtle.__init__(self)
		#register_shape('rectangle',(((int(width),0)),(int(width),int(height)),(0,int(height)),(0,0)))
		#self.shape('rectangle')
#class Square(Rectangle):
	#def __init__(self,size):
		#Rectangle.__init__(self,size,size)
class Haxegon(Turtle):
	def __init__(self):
		Turtle.__init__(self)
		register_shape('haxegon')
		for i in range (6):
			forward(size)
			left(60)

			




mainloop()
