from turtle import *
import time
import turtle
import turtle
turtle.setup( width = 800, height = 550, startx = None, starty = None)

turtle.bgpic("court2.gif")

counter = 15
score = 0
RUNNING = True
scoreturtle = turtle.clone()
turtle.hideturtle()
turtle.pu()
turtle.goto(-390,240)
stamplist1 = []


class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)
	def tside(self):
		tside = self.y+(self.r/2)
		return tside
	def bside(self):
		bside = self.y-(self.r/2)
		return bside
	def lside(self):
		lside = self.x-(self.r/2)
		return lside
	def rside(self):
		rside = self.x+(self.r/2)
		return rside
		class Rectangle(Turtle):
	def __init__(self,width,height,x,y, color):
		Turtle.__init__(self)
		self.pu()
		self.x = x

def move_left(event): 
	x=event.x-SCREEN_WIDTH
	y=current_y
	MY_PLAYER.goto(x,y)

turtle.getcanvas().bind('<LEFT>',move_left)

def move_right(event): 
	x=event.x-SCREEN_WIDTH
	y=current_y
	MY_PLAYER.goto(x,y)

turtle.getcanvas().bind('<RIGHT>',move_right)

if coliding_with_basket(ball,basket)==True:
	ball.penup()
	ball.goto(MY_PLAYER.current_x+5,MY_PLAYER.current_y)
	ball.pendown()


	
		