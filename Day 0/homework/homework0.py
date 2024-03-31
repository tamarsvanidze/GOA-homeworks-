from turtle import*
   
   #we want to paint a house

#step 1 : draw a square


width(7)
color("blue")
forward(180)
left(90)

forward(180)
left(90)
forward(180)
left(90)

forward(180)
left(90)

#drawing a door

forward(60)
color("green")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

penup()
goto(180,180)
pendown()

color("purple")
begin_fill()
right(150)
forward(180)
left(120)
forward(180)
end_fill()

#drawing windows
penup()
goto(20,160)
pendown()


color("red")
left(120)
forward(46)
right(90)
forward(46)
right(90)
forward(46)
right(90)
forward(46)
 
left(180)
forward(23)
left(90)
forward(46)
left(90)
forward(23)
left(90)
forward(23)
left(90)
forward(46)

penup()
goto(160,160)
pendown()

forward(46)
right(90)
forward(46)
right(90)
forward(46)
right(90)
forward(46)

left(180)
forward(23)
left(90)
forward(46)
left(90)
forward(23)
left(90)
forward(23)
left(90)
forward(46)