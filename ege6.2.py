from turtle import  *
tracer(0)
for i in range(3):
    fd(7*10)
    rt(90)
    fd(12 * 10)
    rt(90)
up()
fd(4*10)
rt(90)
fd(6 * 10)
rt(270)
down()
for j in range(4):
    fd(83 * 10)
    rt(90)
    fd(77 * 10)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40, 40):
        goto(x*10,y*10)
        dot(3,'blue')
update()
input()