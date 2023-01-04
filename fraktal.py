import turtle

def fractal(level,some_pen,size):
    if (level==0):
        some_pen.begin_fill()
        some_pen.right(60)
        for i in range(1,3):
            some_pen.forward(size)
            some_pen.right(120)
        some_pen.forward(size)
        some_pen.end_fill()
    else:
        fractal(level-1,some_pen,size)
        some_pen.right(120)
        some_pen.forward((2**(level-1))*size)
        some_pen.left(60)
        fractal(level-1,some_pen,size)
        some_pen.left(120)
        some_pen.forward((2**(level-1))*size)
        some_pen.right(180)
        fractal(level-1,some_pen,size)
        some_pen.forward((2**(level-1))*size)

def draw():
    window = turtle.Screen()
    window.bgcolor("pink")

    pen = turtle.Turtle()

    pen.penup()
    pen.sety(200)
    pen.pendown()

    #pen.shape("turtle")
    #pen.color("blue")
    pen.speed(10)

    fractal(6,pen,5)

    window.exitonclick()

draw()
 
