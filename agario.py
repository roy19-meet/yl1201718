import turtle
import time
import random
from ind_proj import Ball
import math

turtle.colormode(255)
turtle.tracer(0)
turtle.hideturtle()
newscore=turtle.clone()
score=0
turtle.bgpic('fireandwater.gif')


RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,0,0,21,'red')

NUMBER_OF_BALLS=6
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=25
MINIMUM_BALL_DX=-2
MAXIMUM_BALL_DX=2
MINIMUM_BALL_DY=-2
MAXIMUM_BALL_DY=2

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

	print(x,y, dx, dy, radius, color)
	ball_1=Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball_1)


def move_all_balls(BALLS):
	for ball_1 in BALLS:
		ball_1.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	if ball_a.radius+ball_b.radius+10 > math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2)+math.pow((ball_a.ycor()-ball_b.ycor()),2)):		
		return True
	else:
		 return False

def check_all_collisions():
	for ball_A in BALLS:
		for ball_B in BALLS:
			if collide(ball_A , ball_B):
				r_a=ball_A.radius
				r_b=ball_B.radius

				x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx=random.randint(int( MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				dy=random.randint(int( MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
				radius=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
				r=random.randint(0,225)
 				g=random.randint(0,225)
 				b=random.randint(0,225)
 				color=(r,g,b)

				if r_a>r_b:
					ball_B.goto(x,y)
					ball_B.radius=radius
					ball_B.shapesize(ball_B.radius/10)
					ball_B.dx=dx
					ball_B.dy=dy
					ball_B.color(color)
					ball_A.radius+=1
					ball_A.shapesize(ball_A.radius/10)
				else: 
					ball_A.goto(x,y)
					ball_A.radius=radius
					ball_A.shapesize(ball_A.radius/10)
					ball_A.dx=dx
					ball_A.dy=dy
					ball_A.color(color)
					ball_B.radius+=1
					ball_B.shapesize(ball_B.radius/10)


def check_myball_collision():
	global score
 	for any_ball in BALLS:
 		if collide(any_ball,MY_BALL):
 			R_a=any_ball.radius
 			R_b=MY_BALL.radius
 			if R_a>R_b:
 				turtle.write('LOSER',move=False,align="center",font=('Ariel',48,"normal"))
 				return False
 				
 			else:
 				any_ball.goto(x,y)
				any_ball.radius=radius
				any_ball.shapesize(any_ball.radius/10)
				any_ball.dx=dx
				any_ball.dy=dy
				any_ball.color(color)
 				MY_BALL.radius+=1
 				MY_BALL.shapesize(MY_BALL.radius/10)
 				score+=1
 				newscore.clear()
 				newscore.penup()
 				newscore.goto(0,SCREEN_HEIGHT-100)
 				newscore.write('score:'+str(score),align='center',font=('Ariel',30,'bold'))
 	return True

def movearound(event): #mouse moving
	x=event.x-SCREEN_WIDTH
	y=SCREEN_HEIGHT-event.y
	MY_BALL.goto(x,y)

turtle.getcanvas().bind('<Motion>',movearound)
turtle.listen()	



while RUNNING==True:
	print("here")
	if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
	if SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2:
   		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
	print("here2")
	move_all_balls(BALLS)
	print("here3")
	check_all_collisions()
	print("here4")
	RUNNING=check_myball_collision()
	print("here5")
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	print("here6")
	turtle.getscreen().update()
	time.sleep(SLEEP)

		

turtle.mainloop()	
		











