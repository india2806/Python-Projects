import turtle

tu = turtle.Turtle()
tu.screen.bgcolor("black")
tu.pensize(2)
tu.color('green')

tu.left(90)

tu.backward(100)
tu.speed(0)
tu.shape("turtle")

def tree(length):
    if length < 10:
        return
    else:
        tu.forward(length)
        tu.color("orange")
        tu.circle(2)
        tu.color('brown')
        tu.left(30)
        tree(3*length/4)
        tu.right(60)
        tree(3*length/4)
        tu.left(30)
        tu.backward(length)



tree(100)
turtle.done()