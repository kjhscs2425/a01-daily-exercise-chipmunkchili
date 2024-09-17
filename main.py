import turtle

side = 100
def draw_triangles():
    for i in range(3):
        for i in range(3):
            turtle.forward(side)
            turtle.right(120)
        turtle.right(120)


draw_triangles()
turtle.right(180)
draw_triangles()


turtle.exitonclick()