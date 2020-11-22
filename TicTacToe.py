import turtle
import os
import math
import random 
from copy import deepcopy


# screen = turtle.Screen()
# screen.screensize(800,800)
# screen.bgcolor("white")
# screen.title("Tic-Tac-Toe")

#Bigger Board
screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("white")
screen.title("Tic-Tac-Toe")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-300,350)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(270)
border_pen.fd(700)
border_pen.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-100,350)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(270)
border_pen.fd(700)
border_pen.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(100,350)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(270)
border_pen.fd(700)
border_pen.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(300,350)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(270)
border_pen.fd(700)
border_pen.hideturtle()

#Horizontal Lines

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-500,210)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(0)
border_pen.fd(1000)
border_pen.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-500,70)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(0)
border_pen.fd(1000)
border_pen.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-500,-70)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(0)
border_pen.fd(1000)
border_pen.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-500,-210)
border_pen.pendown()
border_pen.pensize(2.5)
border_pen.setheading(0)
border_pen.fd(1000)
border_pen.hideturtle()

#Drawing Smaller circles and Squares now

# player = turtle.Turtle()
# player.color("red")
# player.shape("triangle")
# player.penup()
# player.speed(0)
# player.setposition(0, 0)
# player.setheading(90)

speed = 200
yspeed = 140

def move_left():
    x = player.xcor()
    x -= speed
    # if x < -222:
    #     x = -222
    player.setx(x)
def move_right():
    x = player.xcor()
    x += speed
    # if x > 222:
    #     x = 222
    player.setx(x)
def move_up():
    y = player.ycor()
    y += yspeed
    # if y >  222:
    #     y = 222
    player.sety(y)
def move_down():
    y = player.ycor()
    y -= yspeed
    # if y < -222:
    #     y = -222
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

# border_pen = turtle.Turtle()
# border_pen.speed(0)
# border_pen.color("black")
# border_pen.penup()
# border_pen.setposition(-111,333)
# border_pen.pendown()
# border_pen.pensize(2.5)
# border_pen.setheading(270)
# border_pen.fd(667)
# border_pen.hideturtle()


# border_pen1 = turtle.Turtle()
# border_pen1.speed(0)
# border_pen1.color("black")
# border_pen1.penup()
# border_pen1.setposition(111,333)
# border_pen1.pendown()
# border_pen1.pensize(2.5)
# border_pen1.setheading(270)
# border_pen1.fd(667)
# border_pen1.hideturtle()

# border_pen3 = turtle.Turtle()
# border_pen3.speed(0)
# border_pen3.color("black")
# border_pen3.penup()
# border_pen3.setposition(-333,111)
# border_pen3.pendown()
# border_pen3.pensize(2.5)
# # border_pen3.setheading(270)
# border_pen3.fd(666)
# border_pen3.hideturtle()

# border_pen4 = turtle.Turtle()
# border_pen4.speed(0)
# border_pen4.color("black")
# border_pen4.penup()
# border_pen4.setposition(-333,-111)
# border_pen4.pendown()
# border_pen4.pensize(2.5)
# # border_pen4.setheading(270)
# border_pen4.fd(666)
# border_pen4.hideturtle()

# player = turtle.Turtle()
# player.color("red")
# player.shape("triangle")
# player.penup()
# player.speed(0)
# player.setposition(0, 0)
# player.setheading(90)

computer = turtle.Turtle()
computer.color("blue")
computer.shape("square")
computer.penup()
computer.speed(0)
computer.setposition(0, 0)
computer.hideturtle()


# speed = 222

# def move_left():
#     x = player.xcor()
#     x -= speed
#     if x < -222:
#         x = -222
#     player.setx(x)
# def move_right():
#     x = player.xcor()
#     x += speed
#     if x > 222:
#         x = 222
#     player.setx(x)
# def move_up():
#     y = player.ycor()
#     y += speed
#     if y >  222:
#         y = 222
#     player.sety(y)
# def move_down():
#     y = player.ycor()
#     y -= speed
#     if y < -222:
#         y = -222
#     player.sety(y)


# def draw_circle():
#     turtle.pensize(2.5)
#     a = player.xcor()
#     b = player.ycor()
    
#     coord_value = [a, b]
    
    
#     turtle.hideturtle()
#     turtle.penup()
#     turtle.setpos(a, (b-60))

#     turtle.pendown()
#     turtle.circle(60)
#     turtle.hideturtle()

#     return coord_value 
    

# def draw_x():
#     turtle.pensize(2.5)
#     a = player.xcor()
#     b = player.ycor()
#     turtle.hideturtle()
#     turtle.penup()
    
#     coord_value = [a, b]
    
   
#     turtle.setposition(a-50,b+50)
#     turtle.pendown()
#     turtle.setposition(a+50,b-50)
#     turtle.penup()
#     turtle.setposition(a-50,b-50)
#     turtle.pendown()
#     turtle.setposition(a+50,b+ 50)

#     return coord_value 

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

#Bigger Board, 5X5
#Column by Column, 00 is First Column, First Row
# Grid will be matrix like so:
#[[00, 01, 02, 03, 04,
#  10, 11, 12, 13, 14,   
#  20, 21, 22, 23, 24,
#  30, 31, 32, 33, 34, 
#  40, 41, 42, 43, 44
# 
# # ]]
Name_of_Bigger_Spots = ["00", "01", "02", "03", "04", "10", "11", "12", "13", "14", "20", "21", "22", "23", "24",\
    "30", "31", "32", "33", "34", "40", "41", "42", "43", "44"]

Bigger_Board_Coords = [[-400, 280], [-200, 280], [0, 280], [200, 280], [400, 280],\
    [-400, 140], [-200, 140], [0, 140], [200, 140], [400, 140], \
        [-400, 0], [-200, 0], [0, 0], [200, 0], [400, 0],\
            [-400, -140], [-200, -140], [0, -140], [200, -140], [400, -140],\
                [-400, -280], [-200, -280], [0, -280], [200, -280], [400, -280]
    ]

TicTacdict_5X5 = dict(zip(Name_of_Bigger_Spots, Bigger_Board_Coords))
print(TicTacdict_5X5)

#Need Winning Possible Lines

Winning_Lines_5X5_X = [("00", "01", "02", "03", "04"), ("10", "11", "12", "13", "14"), ("20", "21", "22", "23", "24"),\
    ("30", "31", "32", "33", "34"), ("40", "41", "42", "43", "44"), \
        ("00", "10", "20", "30", "40"),  ("01", "11", "21", "31", "41"), ("02", "12", "22", "32", "42"), \
            ("03", "13", "23", "33", "43"), ("04", "14", "24", "34", "44"), ("00", "11", "22", "33", "44"), \
                ("40", "31", "22", "13", "04")
     ]
Winning_Lines_5X5_O = [("00", "01", "02", "03", "04"), ("10", "11", "12", "13", "14"), ("20", "21", "22", "23", "24"),\
    ("30", "31", "32", "33", "34"), ("40", "41", "42", "43", "44"), \
        ("00", "10", "20", "30", "40"),  ("01", "11", "21", "31", "41"), ("02", "12", "22", "32", "42"), \
            ("03", "13", "23", "33", "43"), ("04", "14", "24", "34", "44"), ("00", "11", "22", "33", "44"), \
                ("40", "31", "22", "13", "04")
     ]
Winning_Lines_5X5_X_HARDER = [("00", "01", "02", "03"), ("01", "02", "03", "04"),("10", "11", "12", "13"), ("11", "12", "13", "14"),\
    ("20", "21", "22", "23"), ("21", "22", "23", "24"),("30", "31", "32", "33"), ("31", "32", "33", "34"),\
        ("40", "41", "42", "43"), ("41", "42", "43", "44"), ("00", "10", "20", "30"), ("10", "20", "30", "40"), \
            ("01", "11", "21", "31"), ("11", "21", "31", "41"), ("02", "12", "22", "32"), ("12", "22", "32", "42"),\
                ("03", "13", "23", "33"), ("13", "23", "33", "43"), ("04", "14", "24", "34"), ("14", "24", "34", "44"),\
                    ("01", "12", "23", "34"), ("00", "11", "22", "33"), ("11", "22", "33", "44"), ("10", "21", "32", "43"),\
                        ("30", "21", "12", "03"), ("40", "31", "22", "13"),("31", "22", "13", "04"), ("41", "32", "23", "14")]

Diagonal_line_list = [("01", "12", "23", "34"), ("00", "11", "22", "33"), ("11", "22", "33", "44"), ("10", "21", "32", "43"),\
    ("30", "21", "12", "03"), ("40", "31", "22", "13"),("31", "22", "13", "04"), ("41", "32", "23", "14")]
List_of_X_moves = []
List_of_O_moves = []

#[[00, 01, 02, 03, 04,
#  10, 11, 12, 13, 14,   
#  20, 21, 22, 23, 24,
#  30, 31, 32, 33, 34, 
#  40, 41, 42, 43, 44
# 
# # ]]

Count_5X5 = [5,5,5,5,5,5,5,5,5,5,5,5]
Count_5X5_HARDER = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

Remaining_dict_X_5X5 = dict(zip(Winning_Lines_5X5_X, Count_5X5))
Remaining_dict_O_5X5 = dict(zip(Winning_Lines_5X5_O, Count_5X5))

Starting_Count2 = 5
X_list = ["winning_lines", "opponent_winning_lines", "sum_of_remaining_lines", "Can_increase_winning_lines", "Can_lower_opponent_lines"]
X_list2 = [0, 0, (len(Remaining_dict_X_5X5)*Starting_Count2), True, True]
O_list = ["winning_lines", "opponent_winning_lines", "sum_of_remaining_lines", "Can_increase_winning_lines", "Can_lower_opponent_lines"]
O_list2 = [0, 0, (len(Remaining_dict_O_5X5)*Starting_Count2), True, True]

Starting_Count3 = 4 

Remaining_dict_X_5X5_HARDER = dict(zip(Winning_Lines_5X5_X_HARDER, Count_5X5_HARDER))
Remaining_dict_O_5X5_HARDER = dict(zip(Winning_Lines_5X5_X_HARDER, Count_5X5_HARDER))

X_list3 = [0,0, (len(Remaining_dict_X_5X5_HARDER)*Starting_Count3), True, True]
O_list3 = [0,0, (len(Remaining_dict_X_5X5_HARDER)*Starting_Count3), True, True]



Updated_X_Dict_5X5 = dict(zip(X_list, X_list2))
Updated_O_Dict_5X5 = dict(zip(O_list, O_list2))

Updated_X_Dict_5X5_HARDER = dict(zip(X_list, X_list3))
Updated_O_Dict_5X5_HARDER = dict(zip(X_list, X_list3))
# print(Remaining_dict_X_5X5)
# print(Remaining_dict_O_5X5)
# print(Updated_X_Dict_5X5)
# print(Updated_O_Dict_5X5)


#Shows how many moves are needed to win, using this specific path
Remaining_dict_X = dict(zip(Winning_Lines, Count))
Remaining_dict_O = dict(zip(Winning_Lines2, Count2))
# print(Remaining_dict)

Starting_Count = 3
X_list = ["winning_lines", "opponent_winning_lines", "sum_of_remaining_lines", "Can_increase_winning_lines", "Can_lower_opponent_lines"]
X_list2 = [0, 0, (len(Remaining_dict_X)*Starting_Count), True, True]
O_list = ["winning_lines", "opponent_winning_lines", "sum_of_remaining_lines", "Can_increase_winning_lines", "Can_lower_opponent_lines"]
O_list2 = [0, 0, (len(Remaining_dict_O)*Starting_Count), True, True]

Updated_X_Dict = dict(zip(X_list, X_list2))
Updated_O_Dict = dict(zip(O_list, O_list2))
# print(Updated_X_Dict)
# print(Updated_O_Dict)



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
def decrease_values(dictionary, key_name, updated_dictionary):
    list_of_keys = []
    for key, value in dictionary.items():
        for keys in key:
            if key_name == keys:
                list_of_keys.append(key)
    for winning_line in list_of_keys:
        for key in dictionary.keys():
            if winning_line == key:
                dictionary[winning_line] = dictionary[winning_line]-1
    #We are updating the overall count of each dictionary, and sending it to corresponding updated dictionary
    #This will only matter if a player can not improve his amount of own winning lines, and can not lower opponents winning lines
    # Then, player will pick spot that maximizes his current count - new count 
    Count = 0
    for values in dictionary.values():
        Count +=values 
    updated_dictionary["sum_of_remaining_lines"] = Count 
    # print(updated_dictionary["sum_of_remaining_lines"])    

    Values = []
    for value in dictionary.values():
        Values.append(value)

    # print(min(Values))           
    if min(Values) == 0:
        return 0 
    else:
        return dictionary                       


#Created function that will remove a key, value pair from a dictionary, based on the dictionary, and a coordinate given 
def remove_dict(Key_Dictionary,  coordinate):
        
    for key,value in Key_Dictionary.items():
        if value == coordinate:
            storedvalue = key
    Key_Dictionary.pop(storedvalue)
    return Key_Dictionary
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

def Thoughtful_Move(Your_Dictionary, Opponent_Dictionary, Key_Dictionary, Starting_count, Your_Updated_Dic, Opponent_Updated_Dic):
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
       
    #Setting up winning move if possible:
    Keys_to_win = []
    for winning_line, count in Opponent_Dictionary.items():
        for Line, Count in Your_Dictionary.items():
            if Line == winning_line:
                if Count == 1 and count == Starting_count:
                    for keys in Line:
                        if keys in Remaining_Keys:
                            Keys_to_win.append(keys)
    
    if len(Keys_to_win)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_win[0] == position:
                coordinates = coord
        computer.setpos(coordinates[0],coordinates[1])
        return                          
    
    #This check ensures if a spot must be blocked, then it is blocked first, and returned immediately
    if len(Keys_to_Remove)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_Remove[0] == position:
                coordinates = coord
        computer.setpos(coordinates[0],coordinates[1])
        return   
    
    #Check here to see if you can no longer increase winning possible lines, and we can lower opponents lines, 
    # We alter the while loop for keys to see how many opponent lines we can block instead...This exists after Flag is turned on

    #TO DO: 
    if Your_Updated_Dic["Can_increase_winning_lines"] == False and Your_Updated_Dic["Can_lower_opponent_lines"] == True :
        Keys_Remaining = len(Remaining_Keys)
        Lower_Line_Count = []
        Winning_lines_Container = []
        Count = 0
        index = 0
                
        #Checking how many lines in our dictionary that have 3 for a count, have opponent count < 3
        #Lower_Line_Count will represent each key, and their effect on lowering opponents winning_lines
        for winning_line, count in Your_Dictionary.items():
            if count == Starting_Count:
                Winning_lines_Container.append(winning_line)
        #The opponents winning lines are in the Winning_line_container
        #So we want the key that intersects as many of these lines as possible
        while Keys_Remaining > 0:
            key = Remaining_Keys[index]

            for winning_line in Winning_lines_Container:
                for keys in winning_line:
                    if key in keys:
                        Count +=1
            #This should append the amount of opponent winning lines each key intersects
            Lower_Line_Count.append(Count)
           
            Count = 0 
            index +=1
            Keys_Remaining -=1        

        Best_Destroyer = dict(zip(Remaining_Keys, Lower_Line_Count))
        # print(Best_Destroyer)
        Random_Best_Choice = []
        Random_Key = []    
        for key, value in Best_Destroyer.items():
            Random_Best_Choice.append(value)
    
        max_val = max(Random_Best_Choice)
        # print(max_val)
        if max_val == 0:
            Your_Updated_Dic["Can_lower_opponent_lines"] = False
            
            Keys_Remaining = len(Remaining_Keys)
            Max_Point_Reduction_Count = []
            Winning_lines_Containers = []
            Count = 0
            index = 0

        #You are taking your winning lines, and opponent winning lines, and adding the value together...if the value > Starting value
        # append that line to Winning_lines_Container, then check every key to see if it is in one of those lines
            for winning_line, count in Your_Dictionary.items():
                for Winning_Line, Count in Opponent_Dictionary.items():
                    if winning_line == Winning_Line:
                        if count + Count > Starting_count:
                            Winning_lines_Containers.append(winning_line)

            while Keys_Remaining > 0:

                key = Remaining_Keys[index]

                for winning_line in Winning_lines_Containers:
                    for keys in winning_line:
                        if key in keys:
                            Count +=1
                
                Max_Point_Reduction_Count.append(Count)
                Count = 0 
                index +=1
                Keys_Remaining -=1
            
            Best_Choice = dict(zip(Remaining_Keys, Max_Point_Reduction_Count))

            Random_Best_Choice = []
            
            Random_Key = []    
            for key, value in Best_Choice.items():
                Random_Best_Choice.append(value)
            max_val = max(0, max(Random_Best_Choice))
            
            for key, value in Best_Choice.items():
                if value == max_val:
                    Random_Key.append(key)
            Random_Final_Choice = []
            #Creating Randomized choice
            if len(Random_Key) > 1:
                random_guy = random.randint(0, (len(Random_Key)-1))
                Random_Final_Choice.append(Random_Key[random_guy])
                for position, coord in Key_Dictionary.items():
                    if Random_Final_Choice[0] == position:
                        coordinates = coord 

                        computer.setpos(coordinates[0],coordinates[1])
                        # print(Random_Key)
                        return 

            Best_Key = max(Best_Choice, key=Best_Choice.get)
            for position, coord in Key_Dictionary.items():
                if Best_Key == position:
                    coordinates = coord 

                computer.setpos(coordinates[0],coordinates[1])
            # print(Random_Key)
                return
        

        for key, value in Best_Destroyer.items():
            if value == max_val:
                Random_Key.append(key)
        
        Random_Final_Choice = []

    #Creating Randomized guess 
        if len(Random_Key) > 1:
            random_guy = random.randint(0, (len(Random_Key)-1))
            Random_Final_Choice.append(Random_Key[random_guy])
        
            for position, coord in Key_Dictionary.items():
                if Random_Final_Choice[0] == position:
                    coordinates = coord 

            computer.setpos(coordinates[0],coordinates[1])
                # print(Random_Key)
            return         
        
        Best_Key = max(Best_Destroyer, key=Best_Destroyer.get)
        for position, coord in Key_Dictionary.items():
            if Best_Key == position:
                coordinates = coord 

        computer.setpos(coordinates[0],coordinates[1])
    # print(Random_Key)
        return 
    #TODO 
    #Finally, we need a condition if you can not improve your winning lines, and you can not decrease opponent winning lines
    if Your_Updated_Dic["Can_lower_opponent_lines"] == False and Your_Updated_Dic["Can_increase_winning_lines"] == False:
        Keys_Remaining = len(Remaining_Keys)
        Max_Point_Reduction_Count = []
        Winning_lines_Containers = []
        Count = 0
        index = 0

        #You are taking your winning lines, and opponent winning lines, and adding the value together...if the value > Starting value
        # append that line to Winning_lines_Container, then check every key to see if it is in one of those lines
        for winning_line, count in Your_Dictionary.items():
            for Winning_Line, Count in Opponent_Dictionary.items():
                if winning_line == Winning_Line:
                    if count + Count > Starting_count:
                        Winning_lines_Containers.append(winning_line)

        while Keys_Remaining > 0:

            key = Remaining_Keys[index]

            for winning_line in Winning_lines_Containers:
                for keys in winning_line:
                    if key in keys:
                        Count +=1
            
            Max_Point_Reduction_Count.append(Count)
            Count = 0 
            index +=1
            Keys_Remaining -=1
        
        Best_Choice = dict(zip(Remaining_Keys, Max_Point_Reduction_Count))

        Random_Best_Choice = []
        
        Random_Key = []    
        for key, value in Best_Choice.items():
            Random_Best_Choice.append(value)
        max_val = max(0, max(Random_Best_Choice))
        
        for key, value in Best_Choice.items():
            if value == max_val:
                Random_Key.append(key)
        Random_Final_Choice = []
        #Creating Randomized choice
        if len(Random_Key) > 1:
            random_guy = random.randint(0, (len(Random_Key)-1))
            Random_Final_Choice.append(Random_Key[random_guy])
            for position, coord in Key_Dictionary.items():
                if Random_Final_Choice[0] == position:
                    coordinates = coord 

                    computer.setpos(coordinates[0],coordinates[1])
                    # print(Random_Key)
                    return 

        Best_Key = max(Best_Choice, key=Best_Choice.get)
        for position, coord in Key_Dictionary.items():
            if Best_Key == position:
                coordinates = coord 

            computer.setpos(coordinates[0],coordinates[1])
        # print(Random_Key)
            return 
         
    Keys_Remaining = len(Remaining_Keys)
    Winning_Line_Count = []
    Winning_lines_Containers = []
    Count = 0
    index = 0
    
    while Keys_Remaining > 0:
        
        key = Remaining_Keys[index]

        for winning_lines in Your_Dictionary.keys():
            for Winning_Lines, value in Opponent_Dictionary.items():
                if winning_lines == Winning_Lines and value == Starting_count:
                    Winning_lines_Containers.append(winning_lines)

        
        
        for actual_winning_lines in Winning_lines_Containers:
            for keys in actual_winning_lines:
                if key in keys:
                    Count +=1

        for winning_lines, current_count in Your_Dictionary.items():
            for line in Winning_lines_Containers:
                if winning_lines == line:
                    if current_count < Starting_Count:
                        Count -=1 

        Winning_Line_Count.append(Count)
        
        Count = 0 
        Winning_lines_Containers.clear()        
        index +=1
        Keys_Remaining -=1
    
    #Dictionary of remaining keys, and their values, higher = better spot
        
    Best_Choice = dict(zip(Remaining_Keys, Winning_Line_Count))
    print(Best_Choice)
    Random_Final_Choiz = []
    Random_Best_Choice = []
    Random_Key = []    
    for key, value in Best_Choice.items():
        Random_Best_Choice.append(value)
    
    max_val = max(Random_Best_Choice)
    
    for key, value in Best_Choice.items():
        if value == max_val:
            Random_Key.append(key)

    # print(max_val)
    
    if max_val <= 0:
        
        Your_Updated_Dic["Can_increase_winning_lines"] = False 

        Keys_Remaining = len(Random_Key)
        Lower_Line_Count = []
        Winning_lines_Container = []
        Opponent_lines_Container = []
        Winning_line_keys = set()
        Final_line_keys = set()
        index = 0
                
        #Checking how many lines in our dictionary that have 3 for a count, have opponent count < 3
        #Lower_Line_Count will represent each key, and their effect on lowering opponents winning_lines
        for winning_line, count in Your_Dictionary.items():
            for Winning_Line, Count in Opponent_Dictionary.items():
                if winning_line == Winning_Line and count == Count == Starting_count:
                    Winning_lines_Container.append(winning_line)
                elif winning_line == Winning_Line:
                    if Count < Starting_Count and count == Starting_count:
                        Opponent_lines_Container.append(Winning_Line)
        print(Winning_lines_Container)
        print(Opponent_lines_Container)
        #The opponents winning lines are in the Winning_line_container
        #So we want the key that intersects as many of these lines as possible
        while Keys_Remaining > 0:
            key = Random_Key[index]

            for winning_line in Winning_lines_Container:
                for keys in winning_line:
                    if key in keys:
                        Winning_line_keys.add(key)

            for Opp_Winning_Line in Opponent_lines_Container:
                for key in Winning_line_keys:
                    if key in Opp_Winning_Line:
                        Final_line_keys.add(key)           
            #This should append the amount of opponent winning lines each key intersects
            Lower_Line_Count.append(Count)
           
            
            index +=1
            Keys_Remaining -=1        
            
        Random_Keyz = []
        Random_Final_Choizes = []    
            
        for keys in Final_line_keys:
            Random_Keyz.append(keys)
        print(Random_Keyz)        
        
        if len(Random_Keyz) == 1:
            for position, coord in Key_Dictionary.items():
                if Random_Keyz[0] == position:
                    coordinates = coord 

                    computer.setpos(coordinates[0],coordinates[1])
                    # print(Random_Key)
                    return 
        elif len(Random_Keyz)> 1:
            random_guy = random.randint(0, (len(Random_Keyz)-1))
            Random_Final_Choizes.append(Random_Keyz[random_guy])
        
            for position, coord in Key_Dictionary.items():
                if Random_Final_Choizes[0] == position:
                    coordinates = coord 

                    computer.setpos(coordinates[0],coordinates[1])
                # print(Random_Key)
                    return  


        
                        
            
    if len(Random_Key) > 1:
        random_guy = random.randint(0, (len(Random_Key)-1))
        Random_Final_Choiz.append(Random_Key[random_guy])
        
        for position, coord in Key_Dictionary.items():
            if Random_Final_Choiz[0] == position:
                coordinates = coord 

                computer.setpos(coordinates[0],coordinates[1])
                # print(Random_Key)
                return     
    

    Best_Key = max(Best_Choice, key=Best_Choice.get)
    for position, coord in Key_Dictionary.items():
        if Best_Key == position:
            coordinates = coord 

    computer.setpos(coordinates[0],coordinates[1])
    # print(Random_Key)
    return 



# Updated_X_Dict['winning_lines']  =  4
# print(Updated_X_Dict)

#These dictionaries will be used in the new function, to decide how the player moves his pieces

def Terminator_Move(Your_Dictionary, Opponent_Dictionary, Key_Dictionary, Starting_count, Your_Updated_Dic, Opponent_Updated_Dic,\
    List_of_Opponent_Moves, List_of_your_moves):
    '''
    This will be an improved function, for games where the amount of winning spots is less than the length or width of the board
    The logic should be stronger, but I have to test it against it's old self once it is completed, in both games, to see which is 
    Smarter
    '''
    
    
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
       
    #Setting up winning move if possible:
    Keys_to_win = []
    for winning_line, count in Opponent_Dictionary.items():
        for Line, Count in Your_Dictionary.items():
            if Line == winning_line:
                if Count == 1 and count == Starting_count:
                    for keys in Line:
                        if keys in Remaining_Keys:
                            Keys_to_win.append(keys)
    
    if len(Keys_to_win)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_win[0] == position:
                coordinates = coord
                computer.setpos(coordinates[0],coordinates[1])
                List_of_your_moves.append(Keys_to_win[0])
                return                          
    
    #This check ensures if a spot must be blocked, then it is blocked first, and returned immediately
    if len(Keys_to_Remove)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_Remove[0] == position:
                coordinates = coord
        computer.setpos(coordinates[0],coordinates[1])
        return
    
    
    Linez_to_block = []
    Key_blocker = []
    Keys_to_blockz = []
    adjacency_keys = []
    
    for winning_line, value in Opponent_Dictionary.items():
        for Line, val in Your_Dictionary.items():
            if value == (Starting_count -2) and val == Starting_count:
                Linez_to_block.append(winning_line)
    for line in Linez_to_block:
        for spot in line:
            if spot in List_of_Opponent_Moves:
                adjacency_keys.append(spot)
            elif spot not in List_of_Opponent_Moves:
                Keys_to_blockz.append(spot)

    #Adjacency keys have keys in the line we want to block, Keys to blocks represents keys we can use, 
    # We need to test which keys we can block by finding the keys in the line, and taking out the ones already player
    # Then we test remaining keys, to see if adjacency len value in the Adjacency Dict is > 5, meaning theyre not on an edge,
    # If so, we block that spot
    for keys, adjacency_list in Connected_Dict.items():
        for KEY in Keys_to_blockz:
            if KEY == keys:
                if len(adjacency_list) > 5:
                    # Key_blocker.append(KEY)

                    for position, coord in Key_Dictionary.items():
                        if KEY == position:
                            coordinates = coord
                            computer.setpos(coordinates[0],coordinates[1])
                        
                            List_of_your_moves.append(KEY)
                
                            return     

    #While loop for checking value
    
    Keys_Remaining = len(Remaining_Keys)
    Winning_Line_Count = []
    Winning_lines_Containers = []
    Blocking_lines_Containers = []
    Count = 0
    index = 0
    Adjacency_list = []
    while Keys_Remaining > 0:
        
        key = Remaining_Keys[index]

        for Winning_Line, value in Opponent_Dictionary.items():
            if value == Starting_count:
                Winning_lines_Containers.append(Winning_Line)
        
        for winning_line in Winning_lines_Containers:
            for value in winning_line:
                if key == value:
                    Count +=1
        
        #2) Blocking lines of opponent +1 point
        for Winning_lines, values in Opponent_Dictionary.items():
            for Winning_linez, valuez in Your_Dictionary.items():
                if Winning_lines == Winning_linez:
                    if values < Starting_count and valuez == Starting_count:
                        Blocking_lines_Containers.append(Winning_lines)

        for W_linez in Blocking_lines_Containers:
            for valu in W_linez:
                if key == valu:
                    Count +=1
        #3) Blocking Diagonal lines of Opponent
        for LINES in Diagonal_line_list:
            for values in LINES:
                if key in values:
                    Count +=1
        #4)Use adjacency values, and subtract current keys in list of opponent moves and your moves
        # Add that value to the count 
        for keys, adjacency_list in Connected_Dict.items():
            if key == keys:
                adjacent_to_key = adjacency_list
        
        for keys in List_of_Opponent_Moves:
            if keys in adjacent_to_key:
                Adjacency_list.append(keys)
        for keys in List_of_your_moves:
            if keys in adjacent_to_key:
                Adjacency_list.append(keys)

        Total_near = len(adjacent_to_key) - len(Adjacency_list)
        Count += Total_near                 
                     
        Winning_Line_Count.append(Count)
        Count = 0 
        Adjacency_list.clear()
        Winning_lines_Containers.clear()        
        index +=1
        Keys_Remaining -=1

    Best_Choice = dict(zip(Remaining_Keys, Winning_Line_Count))
    
    Random_Final_Choiz = []
    Random_Best_Choice = []
    Random_Key = []    
    for key, value in Best_Choice.items():
        Random_Best_Choice.append(value)
    print(Random_Best_Choice) 
    max_val = max(Random_Best_Choice)
    
    for key, value in Best_Choice.items():
        if value == max_val:
            Random_Key.append(key)
   
    if len(Random_Key) > 1:
        random_guy = random.randint(0, (len(Random_Key)-1))
        Random_Final_Choiz.append(Random_Key[random_guy])
        
        for position, coord in Key_Dictionary.items():
            if Random_Final_Choiz[0] == position:
                coordinates = coord 

                computer.setpos(coordinates[0],coordinates[1])
                List_of_your_moves.append(Random_Final_Choiz[0])
                # print(Random_Key)
                return     
    

    Best_Key = max(Best_Choice, key=Best_Choice.get)
    for position, coord in Key_Dictionary.items():
        if Best_Key == position:
            coordinates = coord 

    computer.setpos(coordinates[0],coordinates[1])
    List_of_your_moves.append(Best_Key)
    # print(Random_Key)
    return 


# Name_of_Bigger_Spots = ["00", "01", "02", "03", "04", "10", "11", "12", "13", "14", "20", "21", "22", "23", "24",\
#    "30", "31", "32", "33", "34", "40", "41", "42", "43", "44"]

                                                    #[[00, 01, 02, 03, 04,
                                                    #  10, 11, 12, 13, 14,   
                                                    #  20, 21, 22, 23, 24,
                                                    #  30, 31, 32, 33, 34, 
                                                    #  40, 41, 42, 43, 44

Connected_List = [("01", "10", "11"), ("00", "02", "10", "11", "12"), ("01", "11", "12", "13", "03"), ("02", "12", "13", "14", "04"),\
    
    ("03", "13", "14"), ("00", "01", "11", "20", "21"), ("00", "01", "02", "10", "12", "20", "21", "22"), ("01", "02", "03", "11", "13", "21", "22", "23"),\
        ("02", "03", "04", "12", "14", "22", "23", "24"), ("03", "04", "13", "23", "24"),\
            ("10", "11", "21", "30", "31"), ("10", "11", "12", "20", "22", "30", "31", "32"), ("11", "12", "13", "21", "23", "31", "32", "33"),\
                ("12", "13", "14", "22", "24", "32", "33", "34"), ("13", "14", "23", "33", "34"),\
                    ("20", "21", "31", "40", "41"), ("20", "21", "22", "30", "32", "40", "41", "42"),\
                        ("21", "22", "23", "31", "33", "41", "42", "43"),("22", "23", "24", "32", "34", "42", "43", "44"),\
                            ("30", "31", "41"), ("30", "31", "32", "40", "42"), ("31", "33", "33", "41", "43"),\
                                ("32", "33", "34", "42", "44"), ("33", "34", "43")]

Connected_Dict = dict(zip(Name_of_Bigger_Spots, Connected_List))
print(Connected_Dict)


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
while Count <25 and Game_over == False:
    
       
    
    while Variable  == 1:
        Terminator_Move(Remaining_dict_O_5X5_HARDER, Remaining_dict_X_5X5_HARDER, TicTacdict_5X5, 4, Updated_O_Dict_5X5_HARDER, Updated_X_Dict_5X5_HARDER,\
            List_of_X_moves, List_of_O_moves)
        Coordinat = (computer_draw_circle())
        key = (key_name(TicTacdict_5X5, Coordinat))
        
        # decrease_values(Remaining_dict_O, key)
        if decrease_values(Remaining_dict_O_5X5_HARDER, key, Updated_O_Dict_5X5_HARDER) == 0:
            print("O WINS!!!")
            Game_over = True 
            break
            
            
        remove_dict(TicTacdict_5X5, Coordinat)
        
                
        Variable *= -1
        Count +=1
        
        if Count == 25:
            break

    
    while Variable == -1:
        if Count == 25:
            break 

        Terminator_Move(Remaining_dict_X_5X5_HARDER, Remaining_dict_O_5X5_HARDER, TicTacdict_5X5, 4, Updated_X_Dict_5X5_HARDER, Updated_O_Dict_5X5_HARDER,\
            List_of_O_moves, List_of_X_moves)
        Coordinat = (comp_draw_x())
        key = (key_name(TicTacdict_5X5, Coordinat))
        # decrease_values(Remaining_dict_X, key)
        if decrease_values(Remaining_dict_X_5X5_HARDER, key, Updated_X_Dict_5X5_HARDER) == 0:
            print("X WINS!!!")
            Game_over = True 
            break
             
        remove_dict(TicTacdict_5X5, Coordinat)
        
        
        Variable *=-1
        Count +=1

        if Count == 25:
            break 
             
# print(Updated_O_Dict_5X5)
# print(Updated_X_Dict_5X5)
          
delay = input("Press enter to finish.")