import turtle
import time
import random
from ind_proj import Ball
import math

turtle.colormode(255)
turtle.tracer(0)
turtle.hideturtle()

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,10,10,15,'red')

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]
for i in range (NUMBER_OF_BALLS):
	x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx=random.randint(int( MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
	dy=random.randint(int( MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
	radius=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
	r=random.randint(0,225)
 	g=random.randint(0,225)
 	b=random.randint(0,225)
 	color=(r,g,b)

	ball_1=Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball_1)


def move_all_balls():
	for i in BALLS():
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	if ball_a.radius+ball_b.radius+10 > math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2)+math.pow((ball_a.ycor()-ball_b.ycor()),2)):		
		return True
		else return False
def check_all_collisions():
	for ball_A in BALLS:
		for ball_B in BALLS:
			if collide(ball_A , ball_B) :
				r1=ball_A.radius()
				r2=ball_B.radius()
				if r1>r2:
					relocate'''i should write a code for relocating''' ball_B
					else if r2>r1 relocate ball_A





