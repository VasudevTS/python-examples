import turtle

def draw_green_triangle(ram):
    ram.color("#64DD17")
    ram.begin_fill()
    
    for i in range(1,3):
        ram.forward(100) 
        ram.left(120)
        
    ram.forward(100)
    ram.end_fill()
    
def draw_white_triangle(guru):
    
    guru.left(120)
    guru.forward(100)
    guru.left(120)
    guru.forward(50)
    
    guru.begin_fill()
    guru.color("#fff")
    
    guru.left(60)
    guru.forward(50)

    for i in range(1,3):
        guru.left(120)
        guru.forward(50)
    
    guru.end_fill()

def draw_full_triangle(block):
    # first triangle
    draw_green_triangle(block)
    draw_white_triangle(block)
    # second triangle
    block.left(60)
    block.forward(50)
    block.right(120)
    draw_green_triangle(block)
    draw_white_triangle(block)
    # third triangle
    block.right(120)
    block.forward(50)
    block.right(60)
    draw_green_triangle(block)
    draw_white_triangle(block)
    
def draw_art():
    dev = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("#fff")

    dev.setpos(0,0)
    dev.shape("turtle")

    for i in range(1,4):
        draw_full_triangle(dev)
        dev.left(60)
        dev.forward(50)
        dev.right(120)

    window.exitonclick()
    
draw_art()
