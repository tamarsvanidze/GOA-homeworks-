from turtle import*
#we want to paint 3 houses, sun and tree

#step 1: draw a square

speed(8)
width(8)
color("green")
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)

#draw a door

forward(60)
color("red")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

#draw a roof
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

#draw windows
penup()
goto(20,160)
pendown()


color("yellow")
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
#first house  is already ready

#now we can start the second one

#move drawing pen
penup()
goto(210,0)
pendown()

#draw a cquare

right(180)
width(8)
color("green")
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)

#draw a door
forward(60)
color("red")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

#draw a roof

penup()
goto(390,180)
pendown()

color("blue")
begin_fill()
right(150)
forward(180)
left(120)
forward(180)
end_fill()

#draw windows

penup()
goto(230,160)
pendown()


color("brown")
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
goto(370,160)
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

#second house is done.

#now third house

#move drawing pen

penup()
goto(420,0)
pendown()
right(180)

#draw a square

width(8)
color("red")
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)

#draw a door

forward(60)
color("blue")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

#draw a roof

penup()
goto(600,180)
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
goto(440,160)
pendown()


color("yellow")
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
goto(580,160)
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

#houses are done, now a sun

#draw a sun

penup()
goto(-240,320)
color("yellow")
pendown()

begin_fill()
circle(60)
end_fill()
  
#draw a tree

penup()
goto(-290,0)
color("brown")
begin_fill()
pendown()
forward(20)
right(90)
forward(110)
right(90)
forward(20)
right(90)
forward(110)
end_fill()

penup()
goto(-335,125)
color("green")
pendown()

begin_fill()
circle(40)
end_fill()



