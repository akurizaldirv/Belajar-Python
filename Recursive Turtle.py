import turtle

pen=turtle.Turtle()
window=turtle.Screen()
pen.speed(3)

def fraktal(panjang, level):
    if level == 0:
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(180)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
    else:
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(180)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang/4)
        pen.right(90)
        pen.forward(panjang/4)
        pen.right(180)
        fraktal(panjang/2, level-1)




fraktal(500, 4)
