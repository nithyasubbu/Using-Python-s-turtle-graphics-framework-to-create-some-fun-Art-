import turtle

#Draw a triangle
def draw_square():

	#brad is the person/point or contact
	brad = turtle.Turtle()

	#second instance turtle shape is arrow
	brad.shape("arrow")

	#second instance turtle color is red, yellow - pen/fill color
	brad.color("blue")

	#second instance turtle speed is 5 - average
	brad.speed(7)

	#Draw a flower with multiple triangles starting and ending a point until 360 degrees
	#for deg in range(1,37,1):
		#draw a triangle
	for i in range(1,36,1):
		brad.right(120)
		brad.forward(100)
		brad.right(120)
		brad.forward(100)
		brad.right(120)
		brad.forward(100)
	#brad.right(120)
		
		brad.right(10)
	brad.left(80)
	brad.forward(-500)

def drawArt():

	#window is basically the canvas where the square is drawn
	window = turtle.Screen()

	#the color of the screen is red
	window.bgcolor("lightgreen")

	draw_square()

	window.exitonclick()

drawArt()
