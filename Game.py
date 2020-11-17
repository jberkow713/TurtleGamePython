import turtle
import os
import math
import random 

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("black")
screen.title("Space Invaders")

#Draw border:

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

player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -300)
player.setheading(90)

playerspeed = 17.5
#moving player left and right

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


# Create the enemy invader ships

#Choose number of enemies
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:

    enemy.color("blue")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(175,300)
    enemy.setposition(x,y)

enemyspeed = 5   



#create player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40
#Define the bullet state
#ready-ready to fire
# fire- bullet is firing
bulletstate = "ready"


Score = 0
Score_pen = turtle.Turtle()
Score_pen.color("white")
Score_pen.speed(0)
Score_pen.penup()
Score_pen.setposition(-340, 320)
scorestring = "Score: %s" %Score
Score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
Score_pen.hideturtle()
# enemybomb = turtle.Turtle()
# enemybomb.color("green")
# enemybomb.shape("square")
# enemybomb.penup()
# enemybomb.speed(0)
# enemybomb.setheading(270)
# enemybomb.shapesize(.3, .3)
# enemybomb.hideturtle()
# enemybombspeed = -10

def fire_bullet():
    #declare bulletstate as global
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fired"

        #move bullet to just above player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()
#create keybindings
#cool functionality, the left key is built in to trigger when left
# arrow is pressed, then call the left function
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False    

turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right") 
turtle.onkey(fire_bullet, "space")  

#Main game loop

while True:
    
    for enemy in enemies:
           
    #move enemy across screen
        x = enemy.xcor()
        x+= enemyspeed
        enemy.setx(x)
        #start it going right, once hits border, 
        
        if enemy.xcor() >= 330:
            for enemy in enemies:
                y = enemy.ycor()
                y-=40
                enemy.sety(y)
            enemyspeed *=-1
        if enemy.xcor() < -330:
            for enemy in enemies:
                y = enemy.ycor()
                y-=40
                
                enemy.sety(y)
            enemyspeed *=-1

        if isCollision(bullet, enemy):
        #reset bullet, reset enemy position
            Score +=1
            scorestring = "Score: %s" %Score
            Score_pen.clear()
            Score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -450)
            #reset enemy
            enemy.setposition(-250, 300)   
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER!!")
            break                
    # fire bullet if can be fired, if space bar is pressed
    # so y coordinate is just going up and up and up, until player presses spacebar, at which point it relocates to right
    # above the player, and then goes up by bulletspeed
    
    y = bullet.ycor()
    y+=bulletspeed
    bullet.sety(y)
    # set condition to check if bullet went off map
    #once it does, then it is READY to be fired again, in other words, the bullet can not be fired until its y coor is higher
    # than the maps y coord
    if bullet.ycor()> 350:
        bullet.hideturtle()
        bulletstate = "ready"
    





















delay = input("Press enter to finish.")

