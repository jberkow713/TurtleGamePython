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


Coords = [[-222, 222], [0,222], [222,222], [-222,0], [0,0], [222, 0], [-222,-222], [0,-222], [222,-222]]
Name_of_Spots = [ "TL","TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]

TicTacdict = dict(zip(Name_of_Spots, Coords))
# print(TicTacdict)
Winning_Lines = [("TL", "TM", "TR"), ("ML", "MM", "MR"), ("BL", "BM", "BR"), ("TL", "ML", "BL"),\
    ("TM", "MM", "BM",), ("TR", "MR", "BR"), ("TL", "MM", "BR"), ("BL", "MM", "TR")]
Count = [3,3,3,3,3,3,3,3]

Winning_Lines2 = [("TL", "TM", "TR"), ("ML", "MM", "MR"), ("BL", "BM", "BR"), ("TL", "ML", "BL"),\
    ("TM", "MM", "BM",), ("TR", "MR", "BR"), ("TL", "MM", "BR"), ("BL", "MM", "TR")]
Count2 = [3,3,3,3,3,3,3,3]

#Shows how many moves are needed to win, using this specific path
Remaining_dict_X = dict(zip(Winning_Lines, Count))
Remaining_dict_O = dict(zip(Winning_Lines2, Count2))
# print(Remaining_dict)


# This is in the case of player going first, forcing computer into one of the corner spots
def comp_pos_if_first_center():
    possible_spots = ["TL", "TR", "BL", "BR"]
    random_index = random.randint(0, (len(possible_spots)-1))
    random_position = possible_spots[random_index]

    for position, coord in TicTacdict.items():
        if random_position == position:
            coordinates = coord 

    computer.setpos(coordinates[0],coordinates[1]) 


# print(x)
#Find the key associated with the coordinates of the marked X, or O
def key_name(dictionary, coordinate):
    for key, value in dictionary.items():
        if value == coordinate:
            position = key
    return position        

# print(key_name(TicTacdict, x))

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
    Values = []
    for value in dictionary.values():
        Values.append(value)

    # print(min(Values))           
    if min(Values) == 0:
        return 0 
    else:
        return dictionary                       


#Created function that will remove a key, value pair from a dictionary, based on the dictionary, and a coordinate given 
def remove_dict(dictionary, coordinate):
        
    for key,value in TicTacdict.items():
        if value == coordinate:
            storedvalue = key
    dictionary.pop(storedvalue)
    return dictionary
# print(remove_dict(TicTacdict, x))
# print(len(TicTacdict))


def random_move(dictionary):
    random_list = []
    if len(dictionary)>=0:

        for key in dictionary.keys():
            random_list.append(key)
        dict_len = len(random_list) -1
        if dict_len > 0:
            random_choice = random.randint(0, dict_len)
        else:
            random_choice = 0    
    #Random value in the list
        random_position = random_list[random_choice]
    
    for key, value in dictionary.items():
        if random_position == key:
            coordinates = value

    computer.setpos(coordinates[0],coordinates[1])
    remove_dict(dictionary, coordinates)
        
    return dictionary

def Thoughtful_Move(Your_Dictionary, Opponent_Dictionary, Key_Dictionary, Starting_count):
    '''
    Your Dictionary is your Dictionary of Winning Lines and their counts
    Opponent Dictionary is their Dictionary of Winning Lines and their counts
    Key Dictionary is a list of remaining Keys, and their coordinates
    Starting Count is how many spots in a row you need to win a given game
    '''
    #Get list of remaining keys
    Remaining_Keys = []
    for key in Key_Dictionary.keys():
        Remaining_Keys.append(key)
    #This check makes sure, first, that you block opponent's move, puts key to remove in Keys_to_Remove list
    Keys_to_Remove = []
    for winning_line, count in Opponent_Dictionary.items():
        for Line, Count in Your_Dictionary.items():
            if winning_line == Line:
                if count == 1 and Count == Starting_count:
                    for keys in Line:
                        if keys in Remaining_Keys:
                            Keys_to_Remove.append(keys)
    #This check ensures if a spot must be blocked, then it is blocked first, and returned immediately
    if len(Keys_to_Remove)> 0:
        for position, coord in TicTacdict.items():
            if Keys_to_Remove[0] == position:
                coordinates = coord
        computer.setpos(coordinates[0],coordinates[1])
        return         

                
        # if len(Keys_to_Remove) >=2:
        #     random_to_remove = random.randint(0, (len(Keys_to_Remove)-1) )
        #     return Keys_to_Remove[random_to_remove]
        # else:
        #     random_to_remove = 0
        #     return Keys_to_Remove[0]
    
    Keys_Remaining = len(Remaining_Keys)
    Winning_Line_Count = []
    Winning_lines_Containers = []
    Count = 0
    index = 0
    
    while Keys_Remaining > 0:
        
        key = Remaining_Keys[index]

        for winning_lines in Your_Dictionary.keys():
            if key in winning_lines:
                Winning_lines_Containers.append(winning_lines)

        for line in Winning_lines_Containers:
            for key, value in Opponent_Dictionary.items():
                if line == key:
                    if value == Starting_count:
                        Count +=1

        Winning_Line_Count.append(Count)

        Count = 0 
        Winning_lines_Containers.clear()        
        index +=1
        Keys_Remaining -=1
    #Dictionary of remaining keys, and their values, higher = better spot
    Best_Choice = dict(zip(Remaining_Keys, Winning_Line_Count))

    Random_Best_Choice = []
    Random_Key = []    
    for key, value in Best_Choice.items():
        Random_Best_Choice.append(value)
    max_val = max(Random_Best_Choice)
    for key, value in Best_Choice.items():
        if value == max_val:
            Random_Key.append(key)
    Random_Final_Choice = []
    #Creating Randomized games 
    if len(Random_Key) > 1:
        random_guy = random.randint(0, (len(Random_Key)-1))
        Random_Final_Choice.append(Random_Key[random_guy])
        for position, coord in TicTacdict.items():
            if Random_Final_Choice[0] == position:
                coordinates = coord 

                computer.setpos(coordinates[0],coordinates[1])
                # print(Random_Key)
                return 

    Best_Key = max(Best_Choice, key=Best_Choice.get)
    for position, coord in TicTacdict.items():
        if Best_Key == position:
            coordinates = coord 

    computer.setpos(coordinates[0],coordinates[1])
    # print(Random_Key)
    return 

turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up") 
turtle.onkey(move_down, "Down")
turtle.onkey(draw_circle, "o") 
turtle.onkey(draw_x, "x")      



Count = 0

random_start = random.randint(0,1)
if random_start == 0:
    Variable = 1
else:
    Variable = -1  
Game_over = False
while Count <9 and Game_over == False:
    
       
    
    while Variable  == 1:
        Thoughtful_Move(Remaining_dict_O, Remaining_dict_X, TicTacdict, 3)
        Coordinat = (computer_draw_circle())
        key = (key_name(TicTacdict, Coordinat))
        
        # decrease_values(Remaining_dict_O, key)
        if decrease_values(Remaining_dict_O, key) == 0:
            print("O WINS!!!")
            Game_over = True 
            break
            
            
        remove_dict(TicTacdict, Coordinat)
        
                
        Variable *= -1
        Count +=1
        
        if Count == 9:
            break

    
    while Variable == -1:
        if Count == 9:
            break 

        Thoughtful_Move(Remaining_dict_X, Remaining_dict_O, TicTacdict, 3)
        Coordinat = (comp_draw_x())
        key = (key_name(TicTacdict, Coordinat))
        # decrease_values(Remaining_dict_X, key)
        if decrease_values(Remaining_dict_X, key) == 0:
            print("X WINS!!!")
            Game_over = True 
            break
             
        remove_dict(TicTacdict, Coordinat)
        
        
        Variable *=-1
        Count +=1

        if Count == 9:
            break 
             

          
delay = input("Press enter to finish.")