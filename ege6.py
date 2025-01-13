from turtle import *
tracer(0)
for i in range(5):
    fd(8*10)
    rt(90)
    fd(11*10)
    rt(90)

up()
for x in range (-20,30):
    for y in range (-20,30):
        goto(x*10,y*10)
        dot(3,'blue')
update()
input()