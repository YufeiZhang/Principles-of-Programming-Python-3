from math import *
from turtle import *

def hypotrochoid(R,  r,  h, m, v1="red", v2="yellow",w = 3):
    speed (0)
    R = R  * m; r = m  *  r; h = h * m;  d = R - r + h;
    penup(); setpos(0, -R); pendown(); circle(R)
    penup(); setpos(R, 0); left(90); pendown(); circle(r)
    penup(); setpos(d + 1 , 0)
    
    pendown(); pencolor(v1); width(w)
    fillcolor(v2);  begin_fill()
    t = 0;  x=10
    while distance(d, 0)> 0.001:
        t += 5;  tr = t * pi / 180
        x = (R - r)* cos (tr) +  h * cos((R - r)/  r * tr)
        y = (R - r)* sin (tr) - h * sin((R - r)/  r * tr)
        setpos(x, y)
    end_fill()

hypotrochoid(200,100,20,1)
# hypotrochoid(200,120,200,1)
#hypotrochoid(255, 70, 100, 0.5)
# hypotrochoid(200, 30, 70, 0.5)
# hypotrochoid(200, 50, 70, 0.5)

done()
