from turtle import *
tracer(0)
for i in range(4):
    fd(19*10)
    rt(90)
    fd(30*10)
    rt(90)
up()
fd(2*10)
rt(90)
fd(8*10)
rt(270)
down()
for j in range(4):
    fd(93*10)
    rt(90)
    fd(97*10)
    rt(90)

up()
for x in range(-40,40):
    for y in range(-40, 40):
        goto(x*10,y*10)
        dot(3,'red')






update()
input()
