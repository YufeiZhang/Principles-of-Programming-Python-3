# Draws a dodecadon with the colour of each sector alternating red and blue.
#
# Written by Eric Martin for COMP9021


from turtle import *


def draw_angle(edge_length, n, colour):
    color(colour)
    fd(edge_length)
    rt(180-360/n)
    fd(edge_length)
    lt(180 - 720/n)


def main(edge_length, n):
    home()
    colours = ["red","blue"]
    for i in range(n):
        draw_angle(edge_length, n, colours[i%2])


main(100,6)
