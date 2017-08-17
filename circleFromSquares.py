import turtle

#Draw a square
def draw_square():

	#brad is the person/point or contact
	brad = turtle.Turtle()

	#second instance turtle shape is arrow
	brad.shape("arrow")

	#second instance turtle color is red, yellow - pen/fill color
	brad.color("blue")

	#second instance turtle speed is 5 - average
	brad.speed(5)

	#Draw a circle with multiple squares starting and ending a point until 360 degrees
	for deg in range(1,37,1):
		for i in range(1,5,1):
		
			#brad walks 100 steps forward
			brad.forward(100)
			#brad walks 90 degrees right
			brad.right(90)

		brad.right(10)


def drawArt():

	#window is basically the canvas where the square is drawn
	window = turtle.Screen()

	#the color of the screen is red
	window.bgcolor("lightgreen")

	draw_square()

	window.exitonclick()

drawArt()
