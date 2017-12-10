from turtle import*
import random 
import math

# class Ball(Turtle):
# 	def __init__(self,radius,color,speed):
# 		Turtle.__init__(self)
# 		self.shape('circle')
# 		self.shapesize(radius/10)
# 		self.radius=radius
# 		self.color(color)
# 		self.speed(speed)

# ball_1=Ball(15,'blue',10)
# ball_1.goto(50,50)
# ball_2=Ball(30,'red',20)
# ball_2.goto(90,50)		

# def check_collision(ball_1,ball_2):
# 	if ball_1.radius+ball_2.radius > math.sqrt(math.pow((ball_1.xcor()-ball_2.xcor()),2)+math.pow((ball_1.ycor()-ball_2.ycor()),2)):
# 		print('collision')
# check_collision(ball_1,ball_2)

# list1=[ball_1,ball_2]

#def list_collision(list1):
	#for i in list1
	#if i.radius+(i+1).radius  
	#for g in list1
	#if g.radius+(g+1).radius  

class rectangle(Turtle):
	def __init__(self,x,y,width,height):
		Turtle.__init__(self)
		register_shape('rectangle',(((int(width),0)),(int(width),int(height)),(0,int(height)),(0,0)))
		self.shape('rectangle')
		
		

rec1=rectangle(20,10)
rec2=rectangle(30,15)





mainloop()    