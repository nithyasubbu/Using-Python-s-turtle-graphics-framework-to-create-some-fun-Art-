import turtle

#Draw shapes
def drawShapes():

	#window is basically the canvas where the square is drawn
	window = turtle.Screen()

	#the color of the screen is red
	window.bgcolor("red")

	draw_square()
	draw_circle()
	draw_triangle()
	
	window.exitonclick()

#Draw a square turtle
def draw_square():

	#brad is the person/point or contact
	brad = turtle.Turtle()

	#setting the curcor shape
	brad.shape("circle")

	#setting the pen, fill color of turtle
	brad.color("black")

	#setting the turtle speed
	brad.speed(8)

	#width of the pen
	brad.pensize(7)

	i = 0 

	while i<=3:
		#brad walks 100 steps forward
		brad.forward(100)
		#brad walks 90 degrees right
		brad.right(90)
		i = i+1


def draw_circle():

	#another instance to draw a circle
	katie = turtle.Turtle()

	#with radius 100 cm/mm
	katie.circle(100)

	#second instance turtle shape is arrow
	katie.shape("arrow")

	#second instance turtle color is red, yellow - pen/fill color
	katie.color("green")

	#second instance turtle speed is 5 - average
	katie.speed(5) 

	#width of the pen
	katie.pensize(6)

#Extra credit: draw a triangle turtle
def draw_triangle():

	#another instance to draw a triangle
	nicole = turtle.Turtle()

	#second instance turtle shape is arrow
	nicole.shape("turtle")

	#second instance turtle color is red, yellow - pen/fill color
	nicole.color("blue")

	#second instance turtle speed is 5 - average
	nicole.speed(9)

	#pen width
	nicole.pensize(4)

	#traingle coordinates 3 -> equilateral triangle
	nicole.forward(100)
	nicole.left(120)
	nicole.forward(100)
	nicole.left(120)
	nicole.forward(100)

def main():

	print("Turtle Shapes: ")
	print("1. Draw a square turtle")
	print("2. Draw a circle turtle")
	print("3. Draw a triangle turtle")
	print("4. Exit")
	drawShapes()

if __name__ == "__main__":
	main()
