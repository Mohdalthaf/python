import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_circle_of_squares(num_squares, initial_side_length):
    angle = 360 / num_squares
    for _ in range(num_squares):
        draw_square(initial_side_length)
        turtle.right(angle)

# Initialize Turtle
turtle.speed(0)  # Set the drawing speed (0 is the fastest)
turtle.bgcolor("black")  # Set the background color
turtle.color("white")  # Set the pen color

# Input parameters
num_squares = int(input("Enter the number of squares: "))
initial_side_length = int(input("Enter the side length of the squares: "))

# Draw the circle of squares
draw_circle_of_squares(num_squares, initial_side_length)

# Hide Turtle
turtle.hideturtle()

# Exit on click
turtle.exitonclick()
