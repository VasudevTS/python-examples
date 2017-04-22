import turtle

def draw_triangle(some_turtle):
    for i in range(1,3):
        some_turtle.forward(150)
        some_turtle.right(45)

        some_turtle.forward(150)
        some_turtle.right(135)
        

def draw_art():
    brad = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("#fff")

    brad.shape("turtle")
    brad.color("#03A9F4")

    brad.pensize(2)

    for i in range(1,37):
        draw_triangle(brad)
        brad.right(10)

    brad.sety(-450)

    window.exitonclick()

draw_art()
    
