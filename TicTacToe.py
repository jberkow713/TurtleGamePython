import turtle
import os
import math
import random 
from copy import deepcopy
import numpy as np

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
    
#     return coord_value 
# turtle.onkey(draw_x, "x")     
#     turtle.setposition(a-50,b+50)
#     turtle.pendown()
#     turtle.setposition(a+50,b-50)
#     turtle.penup()
#     turtle.setposition(a-50,b-50)
#     turtle.pendown()
#     turtle.setposition(a+50,b+ 50)

     

def Create_Player_Custom_Commands(Boardsize, Squares):
    '''
    Setting up custom size movement and x,o drawings to implement player versus computer matches
    Need to test further
    '''
    
    Square_Length = round((Boardsize / np.sqrt(Squares)))
    #speed is used for how far player moves with keystroke
    speed = Square_Length

    player = turtle.Turtle()
    player.color("red")
    player.shape("triangle")
    player.penup()
    player.speed(0)
        
    Starting_pos_x = -(Boardsize/2) + .5*(Square_Length) + (((np.sqrt(Squares)-1)/2) * Square_Length)
    Starting_pos_y = (Boardsize/2) - .5*(Square_Length) - (((np.sqrt(Squares)-1)/2) * Square_Length)
    
    player.setposition(Starting_pos_x , Starting_pos_y )
    player.setheading(90)
    
    movement = (Boardsize/Squares)*1.5

    def move_left():
        
        x = player.xcor()
        x -= speed      
        
        if x < -(Boardsize/2)+ .5*(Square_Length):
            x = -(Boardsize/2)+ .5*(Square_Length)
        
        player.setx(x)
        player.setpos(x, player.ycor())
        print(player.pos())
    def move_right():
        x = player.xcor()
        x += speed
        if x > (Boardsize/2) - .5*(Square_Length):
            x = (Boardsize/2) - .5*(Square_Length)
        player.setx(x)
        player.setpos(x, player.ycor())
        print(player.pos())
    def move_up():
        y = player.ycor()
        y += speed
        if y >  (Boardsize/2) - .5*(Square_Length):
            y = (Boardsize/2) - .5*(Square_Length)
        player.sety(y)
        player.setpos(player.xcor(), y)
        print(player.pos())
    def move_down():
        y = player.ycor()
        y -= speed
        if y < -(Boardsize/2)+ .5*(Square_Length):
            y = -(Boardsize/2)+ .5*(Square_Length)
        player.sety(y)
        player.setpos(player.xcor(), y)
        print(player.pos())
    
    def draw_circle():
        turtle.pensize(2.5)
        a = player.xcor()
        b = player.ycor()
        
        coord_value = [a, b]
                
        turtle.hideturtle()
        turtle.penup()
        turtle.setpos(a, (b-movement))

        turtle.pendown()
        turtle.circle(movement)
        turtle.hideturtle()

        # print(coord_value)
        # return coord_value 
    
    def draw_x():
        turtle.pensize(2.5)
        a = player.xcor()
        b = player.ycor()
        turtle.hideturtle()
        turtle.penup()
        
        coord_value = [a, b]
            
        turtle.setposition(a-movement,b+movement)
        turtle.pendown()
        turtle.setposition(a+movement,b-movement)
        turtle.penup()
        turtle.setposition(a-movement,b-movement)
        turtle.pendown()
        turtle.setposition(a+movement,b+ movement)
        # print(coord_value)
        return coord_value     
    
    turtle.listen()
    turtle.onkey(move_left, "Left") 
    turtle.onkey(move_right, "Right")
    turtle.onkey(move_up, "Up") 
    turtle.onkey(move_down, "Down")
    # turtle.onkey(draw_circle, "o") 
    turtle.onkey(draw_x, "x") 

    if turtle.onkey(draw_x, "x"):
        return draw_x() 

       
    




def Create_Board(Boardsize, Squares, Screen_Color, Screen_Title, Line_Color, Line_Size):
    #Sets size of screen, used in making squares
    #Squares has to obviously be a square value, and we're just going to allow it only to be an odd number, aka, 3x3, 5x5, 7x7
    Total_Horizontal_Lines = (math.sqrt(Squares)-1)
    Total_Vertical_Lines = (math.sqrt(Squares)-1)

    Total_Vertical_Distance = Boardsize 
    Total_Horizontal_Distance = Boardsize
    Distance_in_Between_Lines = (Boardsize / math.sqrt(Squares))
    #Have to implement Coordinate system
    First_Vertical_Line_X_Coords = -(Boardsize/2) + Distance_in_Between_Lines 
    First_Vertical_Line_Y_Coords = (Boardsize/2)
    First_Horizontal_Line_X_Coords = -(Boardsize/2)
    First_Horizontal_Line_Y_Coords = (Boardsize/2) - Distance_in_Between_Lines

    screen = turtle.Screen()          
    screen.screensize(Boardsize,Boardsize)
    screen.bgcolor(Screen_Color) #"white", needs ""
    screen.title(Screen_Title) # also needs "" 

    #Going to use while loop here instead
    Remaining_lines = Total_Vertical_Lines
    Current_X = First_Vertical_Line_X_Coords
    Current_Y = First_Vertical_Line_Y_Coords
    
    while Remaining_lines > 0:
                
        border_pen = turtle.Turtle()
        border_pen.speed(0)
        border_pen.color(Line_Color)
        border_pen.penup()
        border_pen.setposition(Current_X, Current_Y)
        border_pen.pendown()
        border_pen.pensize(Line_Size)
        border_pen.setheading(270)
        border_pen.fd(Boardsize)
        border_pen.hideturtle

        Current_X += Distance_in_Between_Lines
        Remaining_lines -=1 
    
    
    Remaining_lines = Total_Horizontal_Lines
    Current_X = First_Horizontal_Line_X_Coords
    Current_Y = First_Horizontal_Line_Y_Coords
    
    while Remaining_lines > 0:
        
        border_pen = turtle.Turtle()  
        border_pen.speed(0)
        border_pen.color(Line_Color)
        border_pen.penup()
        border_pen.setposition(Current_X, Current_Y)
        border_pen.pendown()
        border_pen.pensize(Line_Size)
        border_pen.setheading(0)
        border_pen.fd(Boardsize)
        border_pen.hideturtle()

        Current_Y -= Distance_in_Between_Lines
        Remaining_lines -=1 
    



#Store name of spots in a simple list, from 0 to # of squares, and their coordinates  
# TODO 
# FIX THIS STUPID FUNCTION , IT IS SCREWING UP MY FUN!     
def create_key_dict_and_coords(Boardsize, Squares):
    '''
    This function takes Boardsize, number of Squares, creates a list of each Square as a key, 
    and the key's value corresponds to an [X, Y, coordinate] list, returns dictionary
    '''
    Name_of_Spots = list(range(0, Squares))
    Square_Length = round((Boardsize / np.sqrt(Squares)))
    Mid_Square_Length = (Square_Length / 2)
    Max_X_Coordinate = (Boardsize/2) - Mid_Square_Length
    Min_Y_Coordinate = -(Boardsize/2) + Mid_Square_Length 

    Coordinate_list = []
        
    Len_Coordinate_list = len(Name_of_Spots)
    Starting_X_Coordinate = -(Boardsize/2) + Mid_Square_Length
    Starting_Y_Coordinate = (Boardsize/2) - Mid_Square_Length
    
    X_coord = (Starting_X_Coordinate)
    Y_coord = (Starting_Y_Coordinate)
        
    while Len_Coordinate_list > 0:
        
        Individ_coord = []
        Individ_coord.append(X_coord)
        Individ_coord.append(Y_coord)
        
        Len_Coordinate_list -=1
        Coordinate_list.append(Individ_coord)


        if Len_Coordinate_list % int(math.sqrt(Squares)) == 0:
            X_coord = Starting_X_Coordinate
            Y_coord -= Square_Length
            

        elif Len_Coordinate_list % int(math.sqrt(Squares)) != 0:
            X_coord += Square_Length


    Key_Dict = dict(zip(Name_of_Spots, Coordinate_list))
    print(Key_Dict)
    return Key_Dict 

def create_remaining_dict(Squares, Squares_to_win):
    #We need a matrix, like if it's 5X5
    # We need a matrix with rows and columns, with each value corresponding

    Matrix = []
    list_size = int(np.sqrt(Squares))
    starting = 0
    ending = int(np.sqrt(Squares))
    len_matrix = Squares
    
    while len_matrix > 0:
        list_to_add = []

        for i in range(starting, ending):
            list_to_add.append(i)
       
        Matrix.append(list_to_add)
        starting += list_size 
        ending += list_size
        len_matrix -= list_size 
    #Winning_Lines represents all possible winning lines in the grid
    # print(Matrix)
    
    Winning_Lines = []
    Horizontal_lines_in_Matrix = int(math.sqrt(Squares))
        
    
    Total_Squares = 0
    smaller_list = []
    Row_index = 0
    Column_Idx = 0
    Total_Rows = Horizontal_lines_in_Matrix
    Total_Squares_per_iteration = int(Squares_to_win)
    Iterations_per_row = int(math.sqrt(Squares)-Squares_to_win)+1
    Starting_Column = 0
    Starting_Row = 0
    
    while Horizontal_lines_in_Matrix > 0:
                
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row * Horizontal_lines_in_Matrix):
            
            # print(Column_Idx)    
            smaller_list.append(Matrix[Row_index][Column_Idx])
            # print(Row_index)
            # print(Column_Idx)
            
            Column_Idx +=1
            Total_Squares +=1

            #When we come back to this loop, we start off where we last were, only 1 row lower
                    
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row) :
                a = smaller_list[:]
                # print(a)
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Row +=1
                Row_index = Starting_Row
                Total_Squares = 0
                Horizontal_lines_in_Matrix -=1
                Starting_Column = 0
                Column_Idx = Starting_Column
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                # Row_index = 0 + (Total_Rows - Horizontal_lines_in_Matrix)  
                Starting_Column +=1
                Column_Idx = Starting_Column
                
                break 


    Vertical_lines_in_Matrix = math.sqrt(Squares)            
    Total_Squares = 0
    smaller_list = []
    Row_index = 0
    Column_Idx = 0
    Total_Columns = Vertical_lines_in_Matrix 
    Total_Squares_per_iteration = int(Squares_to_win)
    Iterations_per_row = int(math.sqrt(Squares)-Squares_to_win)+1
    Starting_Column = 0
    Starting_Row = 0
    
    while Vertical_lines_in_Matrix > 0:
        
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row * Vertical_lines_in_Matrix):

            # print(Row_index)
            # print(Column_Idx)    
            smaller_list.append(Matrix[Row_index][Column_Idx])
            # print(Row_index)
            # print(Column_Idx)
            
            Row_index +=1
            Total_Squares +=1

            #When we come back to this loop, we start off where we last were, only 1 row lower
                    
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row) :
                a = smaller_list[:]
                # print(a)
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Column +=1
                Column_Idx = Starting_Column
                Total_Squares = 0
                Vertical_lines_in_Matrix -=1
                Starting_Row = 0
                Row_index = Starting_Row
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                # Row_index = 0 + (Total_Rows - Horizontal_lines_in_Matrix)  
                Starting_Row +=1
                Row_index = Starting_Row
                
                break
    
    Rows_to_iterate_using_Diagonals = int(1 + (math.sqrt(Squares)-Squares_to_win)) #==2
    Iterations_per_row_using_Diagonals = 1 + (math.sqrt(Squares)-Squares_to_win) #==2
    Total_Squares_per_iteration = int(Squares_to_win) # ===4

    Total_Rows = int(Rows_to_iterate_using_Diagonals)
    smaller_list = []
    Total_Squares = 0
    Row_index = 0
    Column_Idx = 0
    Starting_Column = 0
    Starting_Row = 0

    while Rows_to_iterate_using_Diagonals > 0:
               
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals* Rows_to_iterate_using_Diagonals):
                   
            smaller_list.append(Matrix[Row_index][Column_Idx])
            # print(Row_index)
            # print(Column_Idx)
            
            Row_index +=1
            Column_Idx +=1
            Total_Squares +=1

            #When we come back to this loop, we start off where we last were, only 1 row lower
                    
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals) :
                a = smaller_list[:]
                # print(a)
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Row +=1
                Row_index = Starting_Row
                Starting_Column = 0
                Column_Idx = Starting_Column
                Total_Squares = 0
                Rows_to_iterate_using_Diagonals -=1
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                # Row_index = 0 + (Total_Rows - Rows_to_iterate_using_Diagonals)  
                Starting_Column +=1
                Column_Idx = Starting_Column
                Row_index = Starting_Row

                break 
           
    Rows_to_iterate_using_Diagonals = int(1 + (math.sqrt(Squares)-Squares_to_win)) #==2
    Iterations_per_row_using_Diagonals = 1 + (math.sqrt(Squares)-Squares_to_win) #==2
    Total_Squares_per_iteration = int(Squares_to_win) # ===4

    Total_Rows = int(Rows_to_iterate_using_Diagonals)
    smaller_list = []
    Total_Squares = 0
    Row_index = int(math.sqrt(Squares)-1)
    Column_Idx = 0
    Starting_Column = 0
    Starting_Row = int(math.sqrt(Squares)-1)

    
    while Rows_to_iterate_using_Diagonals > 0:
                
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals* Rows_to_iterate_using_Diagonals):
                  
            smaller_list.append(Matrix[Row_index][Column_Idx])
            # print(Row_index)
            # print(Column_Idx)
            
            Row_index -=1
            Column_Idx +=1
            Total_Squares +=1

            #When we come back to this loop, we start off where we last were, only 1 row lower
                    
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals) :
                a = smaller_list[:]
                # print(a)
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Row -=1
                Row_index = Starting_Row
                Starting_Column = 0
                Column_Idx = Starting_Column
                Total_Squares = 0
                Rows_to_iterate_using_Diagonals -=1
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                # Row_index = 0 + (Total_Rows - Rows_to_iterate_using_Diagonals)  
                Starting_Column +=1
                Column_Idx = Starting_Column
                Row_index = Starting_Row

                break 
           

    Count_Lists = [Squares_to_win] * len(Winning_Lines)
    Winning_Lines_Tuples =  [tuple(x) for x in Winning_Lines]

    Remaining_dict = dict(zip(Winning_Lines_Tuples, Count_Lists))    
    return Remaining_dict
    # return Remaining_Dict
def neighbors(Matrix, row, column):
    
    Neighbors = []
    len_matrix = len(Matrix)-1
    

    if column < len_matrix:
        e = Matrix[row][column+1]
        Neighbors.append(e)
    if column < len_matrix and row > 0:
        c = Matrix[row-1][column+1]
        Neighbors.append(c)
    if column > 0:
        d = Matrix[row][column-1]
        Neighbors.append(d)
    if column > 0 and row > 0:
        a = Matrix[row-1][column-1]
        Neighbors.append(a)
    if row > 0:
        b = Matrix[row-1][column]
        Neighbors.append(b)
    if row < len_matrix:
        g = Matrix[row+1][column]
        Neighbors.append(g)
    if row < len_matrix and column < len_matrix:
        h = Matrix[row+1][column+1]
        Neighbors.append(h)
    if row < len_matrix and column > 0:
        f = Matrix[row+1][column-1]
        Neighbors.append(f)
    
    Neighbors.sort()    
    
    return Neighbors                

def Adjacency_Dict(Squares):
    '''
    Returns dictionary
    '''
    #Create the Matrix from the Squares
    Matrix = []
    list_size = int(np.sqrt(Squares))
    starting = 0
    ending = int(np.sqrt(Squares))
    len_matrix = Squares
    
    while len_matrix > 0:
        list_to_add = []

        for i in range(starting, ending):
            list_to_add.append(i)
       
        Matrix.append(list_to_add)
        starting += list_size 
        ending += list_size
        len_matrix -= list_size

    a = int(len(Matrix))

    x= 0
    y= 0

    Adjacency_list = []

    while a > 0:
        
        output = neighbors(Matrix,x,y)
        Adjacency_list.append(output)

        y+=1

        if y == len(Matrix):
            y = 0
            x+=1
            a-=1


    Name_of_Squares = list(range(0, Squares))    
    # Adjacency_list_Tuples =  [tuple(x) for x in Adjacency_list]

    Adjacency_dict = dict(zip(Name_of_Squares, Adjacency_list))    
    
    return(Adjacency_dict)    



def comp_draw_customized_x(boardsize, squares):
    turtle.pensize(2.5)
    turtle.color("blue")
    a = computer.xcor()
    b = computer.ycor()
    turtle.hideturtle()
    turtle.penup()

    coord_value = [a, b]
    
    movement = (boardsize/squares)*1.5

    turtle.setposition(a-movement,b+movement)
    turtle.pendown()
    turtle.setposition(a+movement,b-movement)
    turtle.penup()
    turtle.setposition(a-movement,b-movement)
    turtle.pendown()
    turtle.setposition(a+movement,b+ movement)

    return coord_value 

def computer_draw_customized_circle(boardsize, squares):
    
    movement = (boardsize/squares)*1.5
    
    turtle.pensize(2.5)
    turtle.color("red")
    a = computer.xcor()
    b = computer.ycor()

    coord_value = [a, b]
    # x = player.position(a, (b-50))
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(a, (b-movement))
    
    turtle.pendown()
    turtle.circle(movement)
    turtle.hideturtle()

    return coord_value 

def create_updated_dictionary(Remaining_dict, Squares_to_win):

    
    X_list = ["winning_lines", "opponent_winning_lines", "sum_of_remaining_lines", "Can_increase_winning_lines", "Can_lower_opponent_lines"]
    X_list2 = [0, 0, (len(Remaining_dict) * Squares_to_win), True, True]

    Updated_Dict = dict(zip(X_list, X_list2))

    return Updated_Dict 

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

def Thoughtful_Move(Your_Dictionary, Opponent_Dictionary, Key_Dictionary, Starting_count, Your_Updated_Dic, Opponent_Updated_Dic, \
    List_of_your_moves):
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
        List_of_your_moves.append(Keys_to_win[0])
        return                          
    
    #This check ensures if a spot must be blocked, then it is blocked first, and returned immediately
    if len(Keys_to_Remove)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_Remove[0] == position:
                coordinates = coord
        computer.setpos(coordinates[0],coordinates[1])
        List_of_your_moves.append(Keys_to_Remove[0])
        
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
                        List_of_your_moves.append(Random_Final_Choice[0])
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
            List_of_your_moves.append(Random_Final_Choice[0])
                # print(Random_Key)
            return         
        
        Best_Key = max(Best_Destroyer, key=Best_Destroyer.get)
        for position, coord in Key_Dictionary.items():
            if Best_Key == position:
                coordinates = coord 

        computer.setpos(coordinates[0],coordinates[1])
        List_of_your_moves.append(Best_Key)
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
                    List_of_your_moves.append(Random_Final_Choice[0])
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
            if key in actual_winning_lines:
                Count +=1

        for winning_lines, current_count in Your_Dictionary.items():
            for line in Winning_lines_Containers:
                if winning_lines == line:
                    if current_count < Starting_count:
                        Count -=1 

        Winning_Line_Count.append(Count)
        
        Count = 0 
        Winning_lines_Containers.clear()        
        index +=1
        Keys_Remaining -=1
    
    #Dictionary of remaining keys, and their values, higher = better spot
        
    Best_Choice = dict(zip(Remaining_Keys, Winning_Line_Count))
    # print(Best_Choice)
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
        # print(Random_Keyz)        
        
        if len(Random_Keyz) == 1:
            for position, coord in Key_Dictionary.items():
                if Random_Keyz[0] == position:
                    coordinates = coord 

                    computer.setpos(coordinates[0],coordinates[1])
                    List_of_your_moves.append(Random_Keyz[0])
                    # print(Random_Key)
                    return 
        elif len(Random_Keyz)> 1:
            random_guy = random.randint(0, (len(Random_Keyz)-1))
            Random_Final_Choizes.append(Random_Keyz[random_guy])
        
            for position, coord in Key_Dictionary.items():
                if Random_Final_Choizes[0] == position:
                    coordinates = coord 

                    computer.setpos(coordinates[0],coordinates[1])
                    List_of_your_moves.append(Random_Final_Choizes[0])
                # print(Random_Key)
                    return  
                       
            
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


def Terminator_Move(Your_Dictionary, Opponent_Dictionary, Key_Dictionary, Starting_count, List_of_Opponent_Moves, List_of_your_moves,\
    Adjacency_Dict):
    '''
    This will be an improved function, for games where the amount of winning spots is less than the length or width of the board
    The logic should be stronger, but I have to test it against it's old self once it is completed, in both games, to see which is 
    Smarter
    '''
    
    #Remaining Keys represents possible spots to move to in any given move
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
    #Check if you can win
    if len(Keys_to_win)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_win[0] == position:
                coordinates = coord
                computer.setpos(coordinates[0],coordinates[1])
                List_of_your_moves.append(Keys_to_win[0])
                return                          
    
    #Check if you MUST block winning move of opponent
    if len(Keys_to_Remove)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_Remove[0] == position:
                coordinates = coord
                computer.setpos(coordinates[0],coordinates[1])
                List_of_your_moves.append(Keys_to_Remove[0])
                return
            
    Pre_lines = []
    Set_list = []
    Linez_to_make_triples = []
    Keys_to_move_to = []
    adjacency_keys = []

    for Ln, value in Your_Dictionary.items():
        if value == Starting_count-2:
            for Line, Val in Opponent_Dictionary.items():
                if Ln == Line and Val == Starting_count:
                    Pre_lines.append(Ln)
    
    for lst in Pre_lines:
        setlists = set(lst)
        Set_list.append(setlists)

    #Finding the specific 2 lines to operate on
    Len_Pre_lines = len(Pre_lines)
    Count = 0
    index = 0
    while Len_Pre_lines > 0:

        key = Pre_lines[index]
        Keys_Set = set(key)
        #so we want to turn all lists inside Pre_Lines into sets, this is found in Set_list
        #Now we want to compare Keys_Set to all the sets inside Set_list
        for Lsts in Set_list:
            A = Keys_Set.intersection(Lsts)
            Count += len(A)

        if Count >= (Starting_count + (Starting_count-1)):
            Linez_to_make_triples.append(key)

        Count = 0
        index +=1
        Len_Pre_lines -=1
                           
    #This will trigger if computer CAN make an optimal line of 3, at any given point in the game
    if len(Linez_to_make_triples) == 2:
        
        # print(Linez_to_make_triples) 
        
        for position in Linez_to_make_triples:
            for spot in position:
                if spot in List_of_your_moves:
                    if spot not in adjacency_keys:
                        adjacency_keys.append(spot)
                elif spot not in List_of_your_moves:
                    if spot not in Keys_to_move_to:
                        Keys_to_move_to.append(spot)
       

        Len_Keys = len(Keys_to_move_to)
        Shared_adjacency_list_value = []
        Count = 0
        index = 0 
        while Len_Keys > 0:
            #Keys to move to represents the possible OPEN spot to move to
            key = Keys_to_move_to[index]

            for keys, adjacency_list in Adjacency_Dict.items():
                for KYS in adjacency_keys:
                    if KYS == keys:
                        if key in adjacency_list:
                            Count +=1

            if Count == 2:
                Shared_adjacency_list_value.append(key)
            else:
                Count = 0
                index +=1
                Len_Keys -=1

            #This while loop is basically checking if one of the keys is in between 2 keys in existence...in which case, 
            # you move to it, such as __ X __ X __  it will always move to the middle value

        if len(Shared_adjacency_list_value) == 1:
            # print(Shared_adjacency_list_value[0])
            for position, coord in Key_Dictionary.items():
                if Shared_adjacency_list_value[0] == position:
                    coordinates = coord
                    computer.setpos(coordinates[0],coordinates[1])
                    List_of_your_moves.append(Shared_adjacency_list_value[0])
                    return
        #If the key is not between 2 open keys, we have to decide which key to move to
        # Take the 3 keys to check, check their adjacency values, choose one with longest list
        elif len(Shared_adjacency_list_value) == 0:
            
            Mx_adj_val = []
               
            for KYs in Keys_to_move_to:
                for keys, adjacency_list in Adjacency_Dict.items():
                
                    if KYs == keys:
                        Mx_adj_val.append(len(adjacency_list))
                       
            #                 Ky_to_Block.append(KYs)
            Max_Adjacent_Dict = dict(zip(Keys_to_move_to, Mx_adj_val))
            # print(Max_Adjacent_Dict)
            Best_Key = max(Max_Adjacent_Dict, key=Max_Adjacent_Dict.get)
            for position, coord in Key_Dictionary.items():
                if Best_Key == position:
                    coordinates = coord 

                    computer.setpos(coordinates[0],coordinates[1])
                    List_of_your_moves.append(Best_Key)
            # print(Random_Key)
                    return 

    # This is exactly the same functionality as above, but instead it decides if it MUST block line of 3 instead 
    Pre_lines = []
    Set_list = []
    Linez_to_block_triples = []
    Keys_to_move_to = []
    adjacency_keys = []

    for Ln, value in Opponent_Dictionary.items():
        if value == Starting_count-2:
            for Line, Val in Your_Dictionary.items():
                if Ln == Line and Val == Starting_count:
                    Pre_lines.append(Ln)
    
    for lst in Pre_lines:
        setlists = set(lst)
        Set_list.append(setlists)
    
                    
    Len_Pre_lines = len(Pre_lines)
    Count = 0
    index = 0
    while Len_Pre_lines > 0:

        key = Pre_lines[index]
        Keys_Set = set(key)
        
        for Lsts in Set_list:
            A = Keys_Set.intersection(Lsts)
            Count += len(A)

        if Count >= (Starting_count + (Starting_count-1)):
            Linez_to_block_triples.append(key)

        Count = 0
        index +=1
        Len_Pre_lines -=1
    
    #Now you have the optimal 2 lines to block, you want to find exact position to move to                 
    
    if len(Linez_to_block_triples) == 2:
        # print(Linez_to_block_triples)
        # print(Linez_to_make_triples) 
        
        for position in Linez_to_block_triples:
            for spot in position:
                if spot in List_of_Opponent_Moves:
                    if spot not in adjacency_keys:
                        adjacency_keys.append(spot)
                elif spot not in List_of_Opponent_Moves:
                    if spot not in Keys_to_move_to:
                        Keys_to_move_to.append(spot)
        

        Len_Keys = len(Keys_to_move_to)
        Shared_adjacency_list_value = []
        Count = 0
        index = 0 
        while Len_Keys > 0:
            #Keys to move to represents the possible OPEN spot to move to
            key = Keys_to_move_to[index]

            for keys, adjacency_list in Adjacency_Dict.items():
                for KYS in adjacency_keys:
                    if KYS == keys:
                        if key in adjacency_list:
                            Count +=1

            if Count == 2:
                Shared_adjacency_list_value.append(key)
            else:
                Count = 0
                index +=1
                Len_Keys -=1

            # Same as above, check if gap exists in this line, move there

        if len(Shared_adjacency_list_value) == 1:
            # print(Shared_adjacency_list_value[0])
            for position, coord in Key_Dictionary.items():
                if Shared_adjacency_list_value[0] == position:
                    coordinates = coord
                    computer.setpos(coordinates[0],coordinates[1])
                    List_of_your_moves.append(Shared_adjacency_list_value[0])
                    return
        #If the key is not between 2 open keys, we have to decide which key to move to to block opponent
        elif len(Shared_adjacency_list_value) == 0:
            
            Mx_adj_val = []
               
            for KYs in Keys_to_move_to:
                for keys, adjacency_list in Adjacency_Dict.items():
                
                    if KYs == keys:
                        Mx_adj_val.append(len(adjacency_list))
                        
            Max_Adjacent_Dict = dict(zip(Keys_to_move_to, Mx_adj_val))
            # print(Max_Adjacent_Dict)
            Best_Key = max(Max_Adjacent_Dict, key=Max_Adjacent_Dict.get)
            for position, coord in Key_Dictionary.items():
                if Best_Key == position:
                    coordinates = coord 

                    computer.setpos(coordinates[0],coordinates[1])
                    List_of_your_moves.append(Best_Key)
            # print(Random_Key)
                    return

    #In the case that the computer can not win, can not block final block, can not MOVE to opening of 3, and can not block
    # third spot, it then has the following loop to choose where exactly it moves...this is still sort of a work in progress
    
    Keys_Remaining = len(Remaining_Keys)
    Winning_Line_Count = []
    Winning_lines_Containers = []
    Blocking_lines_Containers = []
    Count = 0
    index = 0
    Adjacency_list = []
    Adj_list_2 = []
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
        # for LINES in Diagonal_line_list:
        #     for values in LINES:
        #         if key in values:
        #             Count +=1
        #4)Use adjacency values, and subtract current keys in list of opponent moves and your moves
        # Add that value to the count 
        for keys, adjacency_list in Adjacency_Dict.items():
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
        Adj_list_2.clear()
        Winning_lines_Containers.clear()        
        index +=1
        Keys_Remaining -=1

    Best_Choice = dict(zip(Remaining_Keys, Winning_Line_Count))
    # print(Best_Choice)
    Random_Final_Choiz = []
    Random_Best_Choice = []
    Random_Key = []    
    for key, value in Best_Choice.items():
        Random_Best_Choice.append(value)
    # print(Random_Best_Choice) 
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

# turtle.listen()
# turtle.onkey(move_left, "Left") 
# turtle.onkey(move_right, "Right")
# turtle.onkey(move_up, "Up") 
# turtle.onkey(move_down, "Down")
# turtle.onkey(draw_circle, "o") 
# turtle.onkey(draw_x, "x")      

def Play_Game(Boardsize, Squares, Squares_to_win, Player=False):
    '''
    Function to play entire game using all other functions. One ring, to rule them all!
    '''
    Create_Board(Boardsize, Squares, "white", "Tic-Tac-Toe", "black", 2.5)
    Key_Dictionary = create_key_dict_and_coords(Boardsize, Squares)
    Remaining_Dict_O = create_remaining_dict(Squares, Squares_to_win)
    Remaining_Dict_X = create_remaining_dict(Squares, Squares_to_win)
    Adjacency_Dict1 = Adjacency_Dict(Squares)
    List_of_X_moves = []
    List_of_O_moves = []
    Updated_Dict = create_updated_dictionary(Remaining_Dict_O, Squares_to_win)
    # player = turtle.Turtle()
    
    
      
    

    if Player==False:

        Count = 0

        random_start = random.randint(0,1)
        if random_start == 0:
            Variable = 1
        else:
            Variable = -1  

        Game_over = False
        while Count <Squares and Game_over == False:
                    
            while Variable  == 1:
                Terminator_Move(Remaining_Dict_O, Remaining_Dict_X, Key_Dictionary, Squares_to_win, List_of_X_moves, List_of_O_moves,\
                    Adjacency_Dict1)
                Coordinat = (computer_draw_customized_circle(Boardsize, Squares))
                key = (key_name(Key_Dictionary, Coordinat))
                
                # decrease_values(Remaining_dict_O, key)
                if decrease_values(Remaining_Dict_O, key, Updated_Dict) == 0:
                    print("O WINS!!!")
                    Game_over = True 
                    break
                                
                remove_dict(Key_Dictionary, Coordinat)
                                    
                Variable *= -1
                Count +=1
                
                if Count == Squares:
                    break
            
            while Variable == -1:
                if Count == Squares:
                    break 
                
                # Thoughtful_Move(Remaining_Dict_X, Remaining_Dict_X, Key_Dictionary, Squares_to_win, Updated_Dict, Updated_Dict, \
                # List_of_X_moves)         
                Terminator_Move(Remaining_Dict_X, Remaining_Dict_O, Key_Dictionary, Squares_to_win, List_of_O_moves, List_of_X_moves,\
                   Adjacency_Dict1)
                Coordinat = (comp_draw_customized_x(Boardsize, Squares))
                key = (key_name(Key_Dictionary, Coordinat))
                # decrease_values(Remaining_dict_X, key)
                if decrease_values(Remaining_Dict_X, key, Updated_Dict) == 0:
                    print("X WINS!!!")
                    Game_over = True 
                    break
                    
                remove_dict(Key_Dictionary, Coordinat)
                    
                Variable *=-1
                Count +=1

                if Count == Squares:
                    break
    
    if Player==True:
        
        # ABC = Create_Player_Custom_Commands(Boardsize, Squares)
        Square_Length = round((Boardsize / np.sqrt(Squares)))
        #speed is used for how far player moves with keystroke
        speed = Square_Length
        
        player = turtle.Turtle()
        player.color("red")
        player.shape("triangle")
        player.penup()
        player.speed(0)
        Starting_pos_x = -(Boardsize/2) + .5*(Square_Length) + (((np.sqrt(Squares)-1)/2) * Square_Length)
        Starting_pos_y = (Boardsize/2) - .5*(Square_Length) - (((np.sqrt(Squares)-1)/2) * Square_Length)
        player.setposition(Starting_pos_x , Starting_pos_y )
        player.setheading(90)        
        
        
                        
        movement = (Boardsize/Squares)*1.5

        Count = 0

        random_start = random.randint(0,1)
        if random_start == 0:
            Variable = 1
        else:
            Variable = -1  

        Game_over = False
        while Count <Squares and Game_over == False:
                    
            while Variable  == 1:
                Terminator_Move(Remaining_Dict_O, Remaining_Dict_X, Key_Dictionary, Squares_to_win, List_of_X_moves, List_of_O_moves,\
                    Adjacency_Dict1)
                Coordinat = (computer_draw_customized_circle(Boardsize, Squares))
                key = (key_name(Key_Dictionary, Coordinat))
                
                # decrease_values(Remaining_dict_O, key)
                if decrease_values(Remaining_Dict_O, key, Updated_Dict) == 0:
                    print("O WINS!!!")
                    Game_over = True 
                    break
                                
                remove_dict(Key_Dictionary, Coordinat)
                                    
                Variable *= -1
                Count +=1
                
                if Count == Squares:
                    break
            
            while Variable == -1:
                if Count == Squares:
                    break 
                #TODO 
                # Figure out how to add player interaction based on keystroke    
                       
                #Need to find a way to stop the program here, until a player draws an X, 
                #Also need to find a way to make the edge restrictions better so it doesn't cut off the map,
                # redo some math, but other than that, it works great!
                
                # while True:
                    
                

                movement = (Boardsize/Squares)*1.5

                def move_left():
                    
                    x = player.xcor()
                    x -= speed      
                    
                    if x < -(Boardsize/2)+ .5*(Square_Length):
                        x = -(Boardsize/2)+ .5*(Square_Length)
                    
                    player.setx(x)
                    player.setpos(x, player.ycor())
                    print(player.pos())
                
                def move_right():
                    x = player.xcor()
                    x += speed
                    if x > (Boardsize/2) :
                        x = -(Boardsize/2) + .5*(Square_Length) + ((np.sqrt(Squares) -1) * Square_Length)
                    player.setx(x)
                    player.setpos(x, player.ycor())
                    print(player.pos())
                def move_up():
                    y = player.ycor()
                    y += speed
                    if y >  (Boardsize/2) - .5*(Square_Length):
                        y = (Boardsize/2) - .5*(Square_Length)
                    player.sety(y)
                    player.setpos(player.xcor(), y)
                    print(player.pos())
                def move_down():
                    y = player.ycor()
                    y -= speed
                    if y < -(Boardsize/2):
                        y = (Boardsize/2) - .5*(Square_Length) - ((np.sqrt(Squares) -1) * Square_Length)
                    player.sety(y)
                    player.setpos(player.xcor(), y)
                    print(player.pos())
                
                def draw_circle():
                    turtle.pensize(2.5)
                    a = player.xcor()
                    b = player.ycor()
                    
                    coord_value = [a, b]
                            
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.setpos(a, (b-movement))

                    turtle.pendown()
                    turtle.circle(movement)
                    turtle.hideturtle()

                    # print(coord_value)
                    # return coord_value 
                import keyboard 
                def draw_x():
                    turtle.pensize(2.5)
                    a = player.xcor()
                    b = player.ycor()
                    turtle.hideturtle()
                    turtle.penup()
                    
                    coord_value = [a, b]
                        
                    turtle.setposition(a-movement,b+movement)
                    turtle.pendown()
                    turtle.setposition(a+movement,b-movement)
                    turtle.penup()
                    turtle.setposition(a-movement,b-movement)
                    turtle.pendown()
                    turtle.setposition(a+movement,b+ movement)
                    # print(coord_value)
                    #This actually works haha
                    global Player_COORD 
                    Player_COORD = coord_value
                    from pynput.keyboard import Key, Controller

                    keyboard = Controller()
                    
                    #So I think it's actually pressing enter, it now has to access console first, 
                    #So that the enter key is pressed on the actual console
                    keyboard.press(Key.enter)
                    
                    
                
               

                turtle.listen()
                turtle.onkey(move_left, "Left") 
                turtle.onkey(move_right, "Right")
                turtle.onkey(move_up, "Up") 
                turtle.onkey(move_down, "Down")
                # turtle.onkey(draw_circle, "o") 
                turtle.onkey(draw_x, "x")
                    
                
                      
                   
                            
                
                
                #So basically, if we can get this Coordinat object to be set equal to 
                # the return object from the draw(x) function, this will work
                
                input("Press enter once you have finished making your play.") 
                                
                key = (key_name(Key_Dictionary, Player_COORD))
                print(key)
                List_of_X_moves.append(key)
                # decrease_values(Remaining_dict_X, key)
                if decrease_values(Remaining_Dict_X, key, Updated_Dict) == 0:
                    print("X WINS!!!")
                    Game_over = True 
                    break
                    
                remove_dict(Key_Dictionary, Player_COORD)
                    
                Variable *=-1
                Count +=1

                if Count == Squares:
                    break

                # turtle.mainloop()    









    # So the idea here is , you have the same while loop, only one computer player is replaced by a human player
    # Coordinat = Draw(x) or Draw(Circle), whatever, probably just make human player X...
    # So you set a variable = to drawing_x, which is triggered by the player actually drawing x
    
    #I need to figure out how to set statements that check player key triggers
    # Then i can say something like, If X is pressed, Coordinat = Draw(X)
    #Then run everything through the same functionality, multiply it by 1, and bam, back to the computer player,
    # The computer player will essentially not do ANYTHING until the player has moved, it will have no choice 


Play_Game(800, 361, 14, )
# Create_Board(800, 121, "white", "Tic-Tac-Toe", "black", 2.5)
# Create_Player_Custom_Commands(800, 121)
# Key_Dictionary = create_key_dict_and_coords(800, 121)
# print(player.pos())

#Game will always work if 2nd number is a square, and if 3rd number is <= np.sqrt of 2nd number
# Need to inform user of that, recommended boardsize is 800

          
delay = input("Press enter to finish.")