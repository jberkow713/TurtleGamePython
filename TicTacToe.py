import turtle
import os
import math
import random 

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("white")
screen.title("Tic-Tac-Toe")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-111,333)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(270)
border_pen.fd(667)
border_pen.hideturtle()


border_pen1 = turtle.Turtle()
border_pen1.speed(0)
border_pen1.color("black")
border_pen1.penup()
border_pen1.setposition(111,333)
border_pen1.pendown()
border_pen1.pensize(2.5)
border_pen1.setheading(270)
border_pen1.fd(667)
border_pen1.hideturtle()

border_pen3 = turtle.Turtle()
border_pen3.speed(0)
border_pen3.color("black")
border_pen3.penup()
border_pen3.setposition(-333,111)
border_pen3.pendown()
border_pen3.pensize(2.5)
# border_pen3.setheading(270)
border_pen3.fd(666)
border_pen3.hideturtle()

border_pen4 = turtle.Turtle()
border_pen4.speed(0)
border_pen4.color("black")
border_pen4.penup()
border_pen4.setposition(-333,-111)
border_pen4.pendown()
border_pen4.pensize(2.5)
# border_pen4.setheading(270)
border_pen4.fd(666)
border_pen4.hideturtle()

player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, 0)
player.setheading(90)

computer = turtle.Turtle()
computer.color("blue")
computer.shape("square")
computer.penup()
computer.speed(0)
computer.setposition(222, 222)


speed = 222

def move_left():
    x = player.xcor()
    x -= speed
    if x < -222:
        x = -222
    player.setx(x)
def move_right():
    x = player.xcor()
    x += speed
    if x > 222:
        x = 222
    player.setx(x)
def move_up():
    y = player.ycor()
    y += speed
    if y >  222:
        y = 222
    player.sety(y)
def move_down():
    y = player.ycor()
    y -= speed
    if y < -222:
        y = -222
    player.sety(y)

def draw_circle():
    turtle.pensize(2.5)
    a = player.xcor()
    b = player.ycor()
    # x = player.position(a, (b-50))
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(a, (b-60))

    turtle.pendown()
    turtle.circle(60)
    turtle.hideturtle()

def draw_x():
    turtle.pensize(2.5)
    a = player.xcor()
    b = player.ycor()
    turtle.hideturtle()
    turtle.penup()
    
    
    turtle.setposition(a-50,b+50)
    turtle.pendown()
    turtle.setposition(a+50,b-50)
    turtle.penup()
    turtle.setposition(a-50,b-50)
    turtle.pendown()
    turtle.setposition(a+50,b+ 50)

#Need to instruct the computer square, where to go, once i draw a shape
# It then needs to move there, and draw the opposite shape
# there are 8 possible lines to win tic tac toe, 3 across, 3 down, 2 diagonal,
# when the player draws on a specific line, that line count gets incremented, from 0->1->2->3
# so basically, the computer will move to a spot with the highest count, and place the opposite drawing
# in the case of a tie, the computer will choose randomly among the tied lines, move to a spot on one of them, and draw

# so basically, we have to program 8 coordinate systems, each line has 3, and the computer will move to a spot 
# on one of those lines, as long as we program his movement correctly...does not matter how computer reaches proper coordinate
# computer could take the shortest route to coordinate system, in case of a tie, if there is a tie, and choices are same distance, 
# computer will choose randomly

# when a line is not able to reach 3 in count, it is crossed off of a list, so the computer will not be able to move back to it
# once it has originally moved there

# if player chooses the first spot in the middle, computer has to randomly choose a corner option to move to
#if players first move is in middle, computer needs to first go to opposite corner

#once the initial computer move has been made, then we implement the other loop, which moves along highest count lines, based 
# on proximity, this will mean computer is really smart

# in the weird option that human is trying to trick computer, computer will always try to finish his own line, if hes at 2,
# before trying to block humans 2







turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up") 
turtle.onkey(move_down, "Down")
turtle.onkey(draw_circle, "o") 
turtle.onkey(draw_x, "x")      


delay = input("Press enter to finish.")