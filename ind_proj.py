from turtle import*
import random
import math

class Ball(Turtle):
 	def __init__(self,x,y,dx,dy,radius,color):
 		Turtle.__init__(self)
 		self.shape('circle')
 		self.dx=dx
 		self.dy=dy
 		self.shapesize(radius/10)
 		self.radius=radius
 		self.color(color)
 		self.pu()
 		self.goto(x,y)

 		

 	def move(self,screen_width,screen_height):
 		current_x=self.xcor()
 		new_x=current_x+self.dx
 		current_y=self.ycor()
 		new_y=current_y+self.dy
 		right_side_ball=new_x+self.radius
 		left_side_ball=new_x-self.radius
 		ball_top=new_y+self.radius
 		ball_bottom=new_y-self.radius
 		self.goto(new_x,new_y)
 		if (right_side_ball>=screen_width or left_side_ball<= -screen_width):
 			self.dx=-self.dx
		if (ball_top>=screen_height or ball_bottom<= -screen_height):
 			self.dy=-self.dy 
