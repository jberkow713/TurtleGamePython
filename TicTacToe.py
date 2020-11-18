import turtle
import os
import math
import random 
from copy import deepcopy


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
computer.setposition(0, 0)
computer.hideturtle()


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


#Once something gets drawn, the keys in the 


def draw_circle():
    turtle.pensize(2.5)
    a = player.xcor()
    b = player.ycor()
    
    coord_value = [a, b]
    
    
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(a, (b-60))

    turtle.pendown()
    turtle.circle(60)
    turtle.hideturtle()

    return coord_value 
    

def draw_x():
    turtle.pensize(2.5)
    a = player.xcor()
    b = player.ycor()
    turtle.hideturtle()
    turtle.penup()
    
    coord_value = [a, b]
    
   
    turtle.setposition(a-50,b+50)
    turtle.pendown()
    turtle.setposition(a+50,b-50)
    turtle.penup()
    turtle.setposition(a-50,b-50)
    turtle.pendown()
    turtle.setposition(a+50,b+ 50)

    return coord_value 

def comp_draw_x():
    turtle.pensize(2.5)
    a = computer.xcor()
    b = computer.ycor()
    turtle.hideturtle()
    turtle.penup()

    coord_value = [a, b]
    

    turtle.setposition(a-50,b+50)
    turtle.pendown()
    turtle.setposition(a+50,b-50)
    turtle.penup()
    turtle.setposition(a-50,b-50)
    turtle.pendown()
    turtle.setposition(a+50,b+ 50)

    return coord_value 

def computer_draw_circle():

    turtle.pensize(2.5)
    a = computer.xcor()
    b = computer.ycor()

    coord_value = [a, b]
    # x = player.position(a, (b-50))
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(a, (b-60))

    turtle.pendown()
    turtle.circle(60)
    turtle.hideturtle()

    return coord_value 

#STUFF LEFT TO DO, before making the Loop


#Advanced, will do later 
# when a line is not able to reach 3 in count, it is crossed off of a list, so the computer will not be able to move back to it
# once it has originally moved there

# Also advanced, computer has to know his moves, will update later
# in the weird option that human is trying to trick computer, computer will always try to finish his own line, if hes at 2,
# before trying to block humans 2

#start with random roll from 0-1, x = random.randint(0,1), if 0, computer starts, if 1, player starts
# Computer, if he goes first , will place a piece at random, otherwise, 



Coords = [[-222, 222], [0,222], [222,222], [-222,0], [0,0], [222, 0], [-222,-222], [0,-222], [222,-222]]
Name_of_Spots = ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]

TicTacdict = dict(zip(Name_of_Spots, Coords))
print(TicTacdict)
Winning_Lines = [("TL", "TM", "TR"), ("ML", "MM", "MR"), ("BL", "BM", "BR"), ("TL", "ML", "BL"),\
    ("TM", "MM", "BM",), ("TR", "MR", "BR"), ("TL", "MM", "BR"), ("BL", "MM", "TR")]
Count = [3,3,3,3,3,3,3,3]

#Shows how many moves are needed to win, using this specific path
Remaining_dict = dict(zip(Winning_Lines, Count))
print(Remaining_dict)


def set_comp_position():
    #This function will find the lowest value in the dictionary, choose a random position in 
    # those values, in case of a tie, choose random spot, and move the computer to that spot
    value_list = []
    possible_spots = set()
    position_list = []
    
    for key, value in Remaining_dict.items():
        value_list.append(value)
    for key, value in Remaining_dict.items():
        if value == min(value_list):
            for spot in key:
                possible_spots.add(spot)
    for position in possible_spots:
        position_list.append(position)
    
    Spot_key = False
    
    while Spot_key == False:
        
        random_index = random.randint(0, (len(position_list)-1))
        #random position represents list of possible positions computer can move to, their name, TL, MM, etc...
        random_position = position_list[random_index]

        if random_position in TicTacdict.keys():
            for position, coord in TicTacdict.items():
                if random_position == position:
                    coordinates = coord
                    Spot_key = True 
        elif random_position not in TicTacdict.keys():
            #this is removing an element from the list so that when you run the randomizer again, it cant be selected
            position_list.remove(random_position)
            
        

    #set the position of the computer at the random spot it needs to move to if spot exists
    computer.setpos(coordinates[0],coordinates[1]) 
    # return coordinates

# This is in the case of player going first, forcing computer into one of the corner spots
def comp_pos_if_first_center():
    possible_spots = ["TL", "TR", "BL", "BR"]
    random_index = random.randint(0, (len(possible_spots)-1))
    random_position = possible_spots[random_index]

    for position, coord in TicTacdict.items():
        if random_position == position:
            coordinates = coord 

    computer.setpos(coordinates[0],coordinates[1]) 

# (set_comp_position())
comp_pos_if_first_center()
# The drawing functions themselves, return a coordinate, based on where the player, or computer was, before it drew
# This way, you can remove the coordinate after drawing, so that when the computer goes to check a position in the dictionary,
# it won't check already drawn positions

x = (computer_draw_circle())
print(x)
#Find the key associated with the coordinates of the marked X, or O
def key_name(dictionary, coordinate):
    for key, value in dictionary.items():
        if value == coordinate:
            position = key
    return position        

print(key_name(TicTacdict, x))

#This function will decrease the count in a dictionary if one part of one of its keys is triggered
def decrease_values(dictionary, key_name):
    list_of_keys = []
    for key, value in dictionary.items():
        for keys in key:
            if key_name == keys:
                list_of_keys.append(key)
    for winning_line in list_of_keys:
        for key in dictionary.keys():
            if winning_line == key:
                dictionary[winning_line] = dictionary[winning_line]-1
    return dictionary                       

#Find the key associated with the coordinates of the marked X, or O
key =(key_name(TicTacdict, x))
print(key)
#Plug the key into the remaining dictionary, to update the values of particular winning lines, to reflect how many more are needed
#To win the game, for a particular line
print(decrease_values(Remaining_dict, key))


#Created function that will remove a key, value pair from a dictionary, based on the dictionary, and a coordinate given 
def remove_dict(dictionary, coordinate):
        
    for key,value in TicTacdict.items():
        if value == coordinate:
            storedvalue = key
    dictionary.pop(storedvalue)
    return dictionary
print(remove_dict(TicTacdict, x))
print(len(TicTacdict))    


#Lets go over the order:

#start with random roll from 0-1, x = random.randint(0,1), if 0, computer starts, if 1, player starts

# Computer, if it goes first , it will roll 0,1 and O if 0, 1 if x, 
# If the computer is going first, the human will obviously place the opposite piece,
# based on what the computer rolls, for the entirety of that game, it will only place those pieces

#If the initial roll lets human go first, human will just choose whatever O or X, and be forced to choose that
# for the rest of the game, and the computer will be forced to choose the opposite of the human for the rest of the game

# So after first roll, if human moves, human is forced into drawing only that type the rest of the game, and as is computer
# And vice versa

# Computer will choose location based on the count in the Remaining Dict, or the player will just choose on his own
# At this point, the player, or the computer, will draw, an X or an O
# A coordinate is returned, that coordinate reflects a key in the TicTacdict keys, and also in the RemainingDict keys
# First, we remove the key from TicTacdict, 
# Then we decrease the value associated with the key and all of it's winning lines in the RemainingDict,

#The process then repeats, the player will choose on its own, and the computer will choose based on where the Player has chosen
# There are two ways in which the while loop ends...
# One way, if any value in the RemainingDict == 0, the game is over
# The other way, if the length of TicTacDict == 0, that means all the different boxes have been filled




turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up") 
turtle.onkey(move_down, "Down")
turtle.onkey(draw_circle, "o") 
turtle.onkey(draw_x, "x")      


delay = input("Press enter to finish.")