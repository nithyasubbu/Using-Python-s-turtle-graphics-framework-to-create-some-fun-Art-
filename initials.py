import turtle

#Miniproject - Draw initials using turtle

#Draw initials
def initials():

	#brad is the person/point or contact
	brad = turtle.Turtle()

	#second instance turtle shape is arrow
	brad.shape("arrow")

	#second instance turtle color is red, yellow - pen/fill color
	brad.color("blue")

	#second instance turtle speed is 5 - average
	brad.speed(3)

	#Initial : 'N' (First Name's initial)
	#Letter 'N' - positions & angles of the turtle arrow
	brad.right(90)
	brad.backward(100)
	brad.right(330)
	brad.forward(110)
	brad.right(30)
	brad.backward(100)

	#printing brad's position to move it to another point horizontally in space
	print(brad.position())

	#turtle.up() is a method where the arrow is moved without drawing
	brad.up()

	#set brad's x & y positions
	brad.setx(85)
	brad.sety(100)

	#Initialize brad's position & use turtle.down() to move the arrow while drawing
	brad.forward(100)
	brad.down()

	#Initial : 'S' (Second Name's initial)
	#Letter 'S' - positions & angles of the turtle arrow

	#for loop repeating 3 times moving the arrow to left by 90 degrees + followed by 45 steps forward
	for i in range(1,4,1):
 		brad.left(90)
 		brad.forward(45)

 	#for loop repeating twice to move the arrow to right by 90 degrees + followed by 45 steps forward
	for j in range(1,3,1):
		brad.right(90)
		brad.forward(45)
	

def drawArt():

	#window is basically the canvas where the square is drawn
	window = turtle.Screen()

	#the color of the screen is red
	window.bgcolor("lightgreen")

	#call the method initials()
	initials()

	#only exit the window on click
	window.exitonclick()

#call method drawArt()
drawArt()
