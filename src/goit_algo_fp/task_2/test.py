import turtle

t = turtle.Turtle()
t.speed(0)
t.color("darkred")
t.width(2)
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("white")


def naked_pythagoras_tree(length, depth, angle=45, ratio=0.7):
    if depth == 0:
        return

    # draw trunk / branch
    t.forward(length)

    # left branch
    t.left(angle)
    naked_pythagoras_tree(length * ratio, depth - 1, angle, ratio)

    # right branch
    t.right(2 * angle)
    naked_pythagoras_tree(length * ratio, depth - 1, angle, ratio)

    # restore position
    t.left(angle)
    t.backward(length)


# initial position
t.penup()
t.goto(0, -300)
t.setheading(90)
t.pendown()

naked_pythagoras_tree(length=160, depth=9, angle=45, ratio=0.72)

turtle.done()
