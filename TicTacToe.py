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

playerspeed = 222

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -222:
        x = -222
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 222:
        x = 222
    player.setx(x)
def move_up():
    y = player.ycor()
    y += playerspeed
    if y >  222:
        y = 222
    player.sety(y)
def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -222:
        y = -222
    player.sety(y)   

turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up") 
turtle.onkey(move_down, "Down")       


delay = input("Press enter to finish.")