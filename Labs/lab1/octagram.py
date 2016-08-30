# Draws a dodecadon with the colour of each sector alternating red and blue.
#
# Written by Eric Martin for COMP9021


from turtle import *
import math


def draw_triangle(i, colour, n, vertices):
    color(colour)
    begin_fill()
    goto(vertices[i + n])
    goto(vertices[(i+1)%n])
    end_fill()


def draw_inside(colour, n, vertices):
    color(colour)
    begin_fill()
    for i in range(n):
        goto(vertices[i%n])
        goto(vertices[(i+1)%n])
    end_fill()


def find_points(edge_length, n, vertices):
    length = 2 * edge_length * abs(math.cos(1/n * math.pi))
    penup()
    for i in range(n):
        right(i * 360 / n)
        forward(edge_length)
        vertices.append(pos())
        home()
    for i in range(n):
        right((i+0.5)*360 / n)
        forward(length)
        vertices.append(pos())
        home()
    vertices.append(vertices[0])
    return vertices


def main(edge_length, n, vertices):
    vertices = find_points(edge_length, n, vertices)
    pendown()
    home()
    draw_inside('yellow', n, vertices)
    for i in range(n):
        goto(vertices[i])
        if i % 2:
            colour = 'red'
        else:
            colour = 'blue'
        draw_triangle(i, colour, n, vertices)


main(100,8,[])
