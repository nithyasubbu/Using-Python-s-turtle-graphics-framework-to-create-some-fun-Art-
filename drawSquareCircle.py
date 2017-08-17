import turtle

#Draw a square
def draw_square():

	#window is basically the canvas where the square is drawn
	window = turtle.Screen()

	#setting the curcor shape
	turtle.shape("circle")

	#setting the pen, fill color of turtle
	turtle.color("red","yellow")

	#setting the turtle speed
	turtle.speed(8)
	#the color of the screen is red
	window.bgcolor("red")

	#brad is the person/point or contact
	brad = turtle.Turtle()

	#brad walks 100 steps forward
	brad.forward(100)
	#brad walks 90 degrees right
	brad.right(90)
	#brad walks 100 steps forward
	brad.forward(100)
	#brad walks 90 degrees right
	brad.right(90)
	#brad walks 100 steps forward
	brad.forward(100)
	#brad walks 90 degrees right
	brad.right(90)
	#brad walks 100 steps forward
	brad.forward(100)
	#brad walks 90 degrees right
	brad.right(90)

	#another instance to draw a circle
	katie = turtle.Turtle()

	#with radius 100 cm/mm
	katie.circle(100)

	#second instance turtle shape is arrow
	katie.shape("arrow")

	#second instance turtle color is red, yellow - pen/fill color
	katie.color("blue")

	#second instance turtle speed is 5 - average
	katie.speed(5)
	window.exitonclick()

draw_square()
