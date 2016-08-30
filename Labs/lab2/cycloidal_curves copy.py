from turtle import *
from math import *

def hypotrochoid(R, r, d, iteration): 
	x, y, up = 0, 0, 1
	penup(); fillcolor("green")
	while iteration:
		theta = iteration/180*pi
		x = (R-r) * cos(theta) + d * cos((R-r)/r*theta)
		y = (R-r) * sin(theta) - d * sin((R-r)/r*theta)
		goto(x,y)
		if up: pendown(); begin_fill(); up = 0	
		iteration -= 5
	end_fill()


def epitrochoid(R, r, d, iteration):
	x, y, up = 0, 0, 1
	penup(); fillcolor("green")
	while iteration:
		theta = iteration/180*pi
		x = (R+r) * cos(theta) - d * cos((R+r)/r*theta)
		y = (R+r) * sin(theta) - d * sin((R+r)/r*theta)
		goto(x,y)
		if up: pendown(); begin_fill(); up = 0	
		iteration -= 5
	end_fill()
	

def main():
	tp = textinput("Hypotrochoid or Epitrochoid","provide no input for an Epitrochoid, and any input for a Hypotrochoid")
	if tp: tp = "Hypotrochoid"
	else: tp = "Epitrochoid"
	R = numinput("Fixed circle", "Radius R between 10 and 290")
	r = numinput("Rolling circle", "Radius r between 10 and 290")
	d = numinput("Point", "Distance d to centre of rolling circle between 0 and 218")
	period = int(r) / gcd(int(R), int(r))	
	print(tp,"for R =",R,"r =",r,"d =",d,"-- Period =", period)
	if tp == "Hypotrochoid": hypotrochoid(R,r,d,period*360)
	else: epitrochoid (R,r,d,period*360)


if __name__ == '__main__':
    main(); done()
