# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by *** for COMP9021


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, p1, p2):
        pass
        # Replace pass above with your code


class Parallelogram:
    def __init__(self, line1, line2, line3, line4):
        pass
        # Replace pass above with your code

    def divides_into_two_parallelograms(self, line):
        pass
        # Replace pass above with your code
        
'''
line = Line(Point(4, 8), Point(4, 8))
pt_11 = Point(-2, 5)
pt_12 = Point(6, 1)
pt_21 = Point(0, 6)
pt_22 = Point(-1, 0)
pt_31 = Point(2, -1)
pt_32 = Point(3, 5)
pt_41 = Point(-3, 3)
pt_42 = Point(1, 1)
line_1 = Line(pt_11, pt_12)
line_2 = Line(pt_21, pt_22)
line_3 = Line(pt_31, pt_32)
line_4 = Line(pt_41, pt_42)
line = Line(Point(4, -2), Point(6, 10))


parallelogram = Parallelogram(line, line_2, line_3, line_4)
parallelogram = Parallelogram(line_1, line_2, line_3, line_1)
line = Line(pt_41, Point(1, 2))
parallelogram = Parallelogram(line_1, line_2, line_3, line)
parallelogram = Parallelogram(line_1, line_2, line_3, line_4)


pt_1 = Point(-1, 4)
pt_2 = Point(2, 2)
line = Line(pt_1, pt_2)
print(parallelogram.divides_into_two_parallelograms(line))
#False
pt_1 = Point(-2, 4)
line = Line(pt_1, pt_2)
print(parallelogram.divides_into_two_parallelograms(line))
#True
print(parallelogram.divides_into_two_parallelograms(line_2))
#False
line = Line(Point(0, -2), Point(0, 7))
print(parallelogram.divides_into_two_parallelograms(line))
#False
line = Line(Point(-1, -3), Point(2, 15))
print(parallelogram.divides_into_two_parallelograms(line))
#True

'''



