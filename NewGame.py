import turtle
import os
import math
import random 

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("black")
screen.title("Dodge the squares")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-350,-350)
border_pen.pendown()
border_pen.pensize(2.5)
for side in range(0,4):
    border_pen.fd(700)
    border_pen.left(90)
border_pen.hideturtle()

# border_pen1 = turtle.Turtle()
# border_pen1.speed(0)
# border_pen1.color("white")
# border_pen1.penup()
# border_pen.setposition(-200,-200)
# border_pen.pendown()
# border_pen.pensize(2.5)
# border_pen.forward(200)
# border_pen.hideturtle


#draw player object


player = turtle.Turtle()
player.color("blue")
player.shape("square")
player.shapesize(1.5)
player.penup()
player.speed(0)
player.setposition(0, 0)
player.setheading(90)
playerspeed = 50


#Directions with keys

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -330:
        x = -330
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 330:
        x = 330
    player.setx(x)
def move_up():
    y = player.ycor()
    y += playerspeed
    if y >  330:
        y = 330
    player.sety(y)
def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -330:
        y = -330
    player.sety(y)    

def random_direction():
    
    random_direction = random.randint(0,3)
        
    if random_direction == 0:
        y = enemy.ycor()
        y += enemyspeed
        enemy.sety(y)
        if y > 320:
            enemyspeed *-1
        if y < -320:
            enemyspeed *-1    
    if random_direction == 1:
        y = enemy.ycor()
        y -= enemyspeed
        enemy.sety(y)
        if y > 320:
            enemyspeed *-1
        if y < -320:
            enemyspeed *-1     
    if random_direction == 2:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if x > 320:
            enemyspeed *-1
        if x < -320:
            enemyspeed *-1 
    if random_direction == 3:
        x = enemy.xcor()
        x -= enemyspeed
        enemy.setx(x)
        if x > 320:
            enemyspeed *-1
        if x < -320:
            enemyspeed *-1     

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.shapesize(2.2)
x = random.randint(-340,340)
y = random.randint(-340,340)
enemy.setposition(x,y)
enemyspeed = 15










turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up") 
turtle.onkey(move_down, "Down")  

# while True:
    
#     for enemy in enemies:
        # random_direction()
count1 = 0
speedcounter = 0
while True:

    x = enemy.xcor()
    x+= enemyspeed
    enemy.setx(x)
    
    if x > 320:
        enemyspeed *=-1
        count1+=1
    if x < -320:
        enemyspeed *=-1 
        count1 +=1 

        if count1 > 5:

            a = random.randint(-340,340)
            b = random.randint(-340,340)
            enemy.setposition(a,b)
            enemyspeed = random.randint(15,45)
            count1 = 0 


    
            




delay = input("Press enter to finish.")