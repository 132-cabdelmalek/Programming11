import turtle
t=turtle.Turtle()
t.setpos(-120, 140)
t.speed(0)
t.hideturtle()

def koch(length):
	if length<5:
		t.forward(length)
		t.left(60)
		t.forward(length)
		t.right(120)
		t.forward(length)
		t.left(60)
		t.forward(length)
	else:
		koch(length/2)
		t.left(60)
		koch(length/2)
		t.right(120)
		koch(length/2)
		t.left(60)
		koch(length/2)
			
for x in range(1, 51):
	koch(24.0)
	t.right(90)
	
import turtle
t = turtle.Turtle()

t.left(90)

def wave(length, xpos):
	t.setpos(xpos, -200)
	t.forward(length)
	if length > 1:	
		wave(length*10/11, xpos+5)

wave(400, -180)
