from turtle import *
#we want to paint a house
#step1: draw a square
speed(30)
width(7)
color("green")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a left window


color("green")
begin_fill()
left(30)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

#drawing a right window
begin_fill()
right(90)
forward(140)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
left(90)
forward(140)


exitonclick()