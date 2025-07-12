from turtle import *

speed(15)

width(5)

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

begin_fill()
forward(70)
left(90)
forward(120) #karebis simagle
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(190) #saxuravic morcha
left(118)
forward(199)
end_fill()

color("blue")   #fanjrebi
penup()
goto(140, 140)
pendown()

left(122)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)


color("blue")
penup()
goto(60, 140)
pendown()
right(90)
forward(50) #califanjara
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

exitonclick()