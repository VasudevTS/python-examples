import turtle

def draw_name(vasu):
    vasu.left(120)
    vasu.forward(100)
    vasu.backward(100)
    vasu.right(60)
    vasu.forward(100)
    vasu.backward(100)

def draw_art():
    dev = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("#fff")
    dev.shape("turtle")
    dev.color("#333")
    draw_name(dev)

    window.exitonclick()
    
draw_art()
    
