from turtle import *

tracer(0)
for i in range(2):
    fd(10*10)
    rt(90)
    fd(18*10)
    rt(90)
up()
fd(5*10)
rt(90)
fd(14*10)
rt(270)
down()
for j in range(2):
    fd(17*10)
    rt(90)
    fd(7*10)
    rt(90)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*10,y*10)
        dot(3,'blue')
update()
input()