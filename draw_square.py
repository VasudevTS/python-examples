import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    # Create a window
    window = turtle.Screen()

    # Add background color for the window
    window.bgcolor("#f9f9f9")

    # Create an object from Turtle class and assign it to name "brad"
    brad = turtle.Turtle()

    # Add a shape to brad    
    brad.shape("turtle")

    # Add color to the turtle
    brad.color("#8e44ad")

    # Specify some speed to the turtle
    brad.speed(2)

    for i in range(1,37):        
        # draw square using brad
        draw_square(brad)
        # move turtle 10 degrees right
        brad.right(10)

    # Create the turtle Angie - Draws a circle
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)

    window.exitonclick()
    

draw_art()
