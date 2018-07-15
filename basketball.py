import turtle

SPACE = 0
Direction = True



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


# dy=

def space_throw(event):
	global SPACE, Direction
	if(Direction):
		SPACE+=1
	else:
		SPACE-=1
	if(SPACE>100):
		Direction = False
	if(SPACE<0):
		Direction = True
		while Direction == True:
			BALL.dx+=1
			BALL.dy-=1	
	print("Pressed")








turtle.getcanvas().bind('<space>',space_throw)

turtle.listen()

while True:
	print(SPACE)
	turtle.getscreen().update()

		



