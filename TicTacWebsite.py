import turtle
import os
import math
import random 
from copy import deepcopy
import numpy as np
  
sc = turtle.Screen() 
sc.setup(800, 800) 

#TODO ---make so if player hits square that is already hit, it will prompt to hit new square, and not give error

Variable8= ""
Choice3 = False
while Choice3 == False:
    list_words = ["yes", "no"]

    Variable8 = turtle.textinput("Play vs computer?",  "Enter yes, or no")
    if Variable8 in list_words:
        Choice3 = True
        Variable8 = Variable8

if Variable8 == "no":


    Variable1 = 780
    Var2 = 0
    Choice = False
    while Choice == False:
        list_nums = str([i for i in range(3,21)])
        Variable2 = turtle.textinput("Dimensions of Board ",  "Enter Rows from 3-20 inclusive")
        # Variable2 = (input("Please enter how many rows and columns you wish the board to have. Input needs to be an integer between 3 and 25, inclusive: \n"))
        #Force user input to be in list of values, while not breaking program if they type a string
        if Variable2 in list_nums:
            Variable2 = int(Variable2)    
        # if isinstance(Variable2, int):

            if Variable2 >2 and Variable2 < 21:
                Var2 = Variable2 
                Choice = True
            
    Variable3 = int(Variable2) ** 2

    Choice2 = False
    while Choice2 == False:
        if Var2 > 3:
            list_nums2 = str([i for i in range(3, (Var2 + 1))])
        if Var2 == 3:
            list_nums2 = str([i for i in range(3, 4)])
            
            
        Variable4 = turtle.textinput("Required number of tiles to win ",  "Enter consecutive squares needed to win")
        if Variable4 in list_nums2:
            Variable4 = int(Variable4)
            #Force user input to be in list of values, while not breaking program if they type a string

        if Variable4 <= Variable2 and Variable4 > (.5* Variable2):
            Choice2 = True 

if Variable8 == "yes":

        Variable1 = 780
        Var2 = 0
        Choice = False
        while Choice == False:
            list_nums = str([i for i in range(3,21,2)])
            Variable2 = turtle.textinput("Dimensions of Board ",  "Enter Rows from 3-20 inclusive, Odd #s Only")
            # Variable2 = (input("Please enter how many rows and columns you wish the board to have. Input needs to be an integer between 3 and 25, inclusive: \n"))
            #Force user input to be in list of values, while not breaking program if they type a string
            if Variable2 in list_nums:
                
                Variable2 = int(Variable2)    
            # if isinstance(Variable2, int):

                if Variable2 >2 and Variable2 < 21:
                    Var2 = Variable2 
                    Choice = True
                
        Variable3 = int(Variable2) ** 2
        #if Variable4 <= Variable2 and Variable4 > (.5* Variable2):
        Choice2 = False
        while Choice2 == False:
            
               
            if Var2 == 3:
                list_nums2 = str([3])
                # print("I am a 3")
            
            elif Var2 == 5:
                list_nums2 = str([5])
                # print("I am a 5")
            elif Var2 > 5:
                list_nums2 = str([i for i in range(3, (Var2 + 1))])
            
            
            Variable4 = turtle.textinput("Required number of tiles to win ",  "Enter consecutive squares needed to win")
            if Variable4 in list_nums2:
                Variable4 = int(Variable4)
            
            
            Variable4 = int(Variable4)
            
                #Force user input to be in list of values, while not breaking program if they type a string
            if Var2 > 5:
                if Variable4 <= Var2 and Variable4 > (.5* Var2):
                    Choice2 = True  
            if Var2 <=5:
                if Variable4 == Var2:
                    Choice2 = True
Variable10a= ""
Choice4 = False
while Choice4 == False:
    list_words = ["yes", "no"]

    Variable10 = turtle.textinput("Play game till end?",  "Enter yes, or no")
    if Variable10 in list_words:
        Choice4 = True
        Variable10a = Variable10



computer = turtle.Turtle()
computer.color("blue")
computer.shape("square")
computer.penup()
computer.speed(0)
computer.setposition(0, 0)
computer.hideturtle()


def Create_Player_Custom_Commands(Boardsize, Squares):
    '''
    Setting up custom size movement and x,o drawings to implement player versus computer matches
    Need to test further
    '''
    global is_done_with_player_move
    is_done_with_player_move = False
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
        # print(player.pos())
    def move_right():
        x = player.xcor()
        x += speed
        if x > (Boardsize/2) - .5*(Square_Length):
            x = (Boardsize/2) - .5*(Square_Length)
        player.setx(x)
        player.setpos(x, player.ycor())
        # print(player.pos())
    def move_up():
        y = player.ycor()
        y += speed
        if y >  (Boardsize/2) - .5*(Square_Length):
            y = (Boardsize/2) - .5*(Square_Length)
        player.sety(y)
        player.setpos(player.xcor(), y)
        # print(player.pos())
    def move_down():
        y = player.ycor()
        y -= speed
        if y < -(Boardsize/2)+ .5*(Square_Length):
            y = -(Boardsize/2)+ .5*(Square_Length)
        player.sety(y)
        player.setpos(player.xcor(), y)
        # print(player.pos())
    
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

        global Player_COORD 
        Player_COORD = coord_value
               
        is_done_with_player_move = True
        # print(is_done_with_player_move)
                
        
        

             
    
    turtle.listen()
    turtle.onkey(move_left, "Left") 
    turtle.onkey(move_right, "Right")
    turtle.onkey(move_up, "Up") 
    turtle.onkey(move_down, "Down")
    # turtle.onkey(draw_circle, "o") 
    turtle.onkey(draw_x, "x") 


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
    # print(Key_Dict)
    return Key_Dict 

def create_remaining_dict(Squares, Squares_to_win):
    
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
     
    
    Keys_Remaining = len(Remaining_Keys)
    Winning_Line_Count = []
    Winning_lines_Containers = []
    Count = 0
    index = 0
    Special_Case_Count = 0
    Opp_winning_lines = []
    Your_winning_lines = []
    Opp_Adjacency_list = []
    Your_Adjacency_list = []
    while Keys_Remaining > 0:
        
        key = Remaining_Keys[index]
        #value winning lines highly to stop opponent, value count highly, super highly in the beginning, this is only
        #to block winning lines
        for Winning_lines, valuess in Your_Dictionary.items():
            for Winning_linez, valuezz in Opponent_Dictionary.items():
                if Winning_lines == Winning_linez:
                    if valuezz < Starting_count and valuess == Starting_count:
                        if key in Winning_lines:
                            Opp_winning_lines.append(key)
                            Special_Case_Count +=1
                            if valuess - valuezz <= .5 * Starting_count:
                                #Make incentive on smaller board to block quicker, as one slip up early can cost game
                                #Notice it is to the 8th power here, again bigger than continuing winning line, which is 
                                # only raised to the 6th power
                                if Starting_count <= 6:
                                    Count +=  (valuess - valuezz)**8
                                #Disincentivize blocking early on big boards, no need, better to expand
                                elif Starting_count > 6:
                                    Count +=  (valuess - valuezz)**2

                            elif valuess - valuezz > .5 * Starting_count:
                                #Not as important to block once it's too late in small games, by that point, it should have 
                                #already blocked, but still more value than adjacency moves
                                if Starting_count < 6:
                                    Count +=  (valuess - valuezz)**7
                                #Make the incentive on a bigger board, to wait until blocks are >half the amount to win
                                #Before you force the block, allow for more expansion...notice its to the 7th power here,
                                # which makes it more important than continuing your original line, which is only raised to 6th
                                elif Starting_count > 6:
                                    Count +=  (valuess - valuezz)**7

        #improve your winning line if possible, value count highly, this is only to improve existing winning lines
        for Winning_lines, values in Opponent_Dictionary.items():
            for Winning_linez, valuez in Your_Dictionary.items():
                if Winning_lines == Winning_linez:
                    if valuez < Starting_count and values == Starting_count:
                        if key in Winning_lines:
                            Your_winning_lines.append(key)
                            Special_Case_Count +=1
                            #incentivizing continuing the winning lines in progress on any board size, 
                            #This incentivizes expanding on early winning lines
                            if values - valuez < .5 * Starting_count:
                                Count += (valuess - valuezz)**6
                            #After blocking opponents early lines in small games, or late lines in big games, 
                            # raising to the power of 4 here trumps the 3rd and 2nd power in the other games, 
                            # meaning this will take precendence over blocking in those situations
                            elif values - valuez >= .5 * Starting_count:
                                Count +=  (values - valuez)**4
        #We need something to implement finding new winning lines
        for Winning_lines, values in Opponent_Dictionary.items():
            for Winning_linez, valuez in Your_Dictionary.items():
                if Winning_lines == Winning_linez:
                    if values == Starting_count and valuez == Starting_count:
                        if key in Winning_lines:
                            Special_Case_Count +=1
                            count += Starting_count        
        
        #Value 2nd highly if spot is in adjacency Dict of opponent moves
        for keys, adjacency_list in Adjacency_Dict.items():
            for keyz in List_of_Opponent_Moves:
                if keyz == keys:
                    if key in adjacency_list:
                        Opp_Adjacency_list.append(key)
                        Special_Case_Count +=1

                        Count +=len(adjacency_list)
        #Value 2nd highly if spot is in adjacency Dict of your moves
        for ky, adj_list in Adjacency_Dict.items():
            for kyz in List_of_your_moves:
                if kyz == ky:
                    if key in adj_list:
                        Your_Adjacency_list.append(key)
                        Special_Case_Count +=1
                        Count +=len(adjacency_list)              
        
        #Added bonuses, exponential bonus, based on how many of the previous conditions it meets          
        Count += (Special_Case_Count**2)
        #Most of the time, this special case count will not matter, until winning lines and blocking come to an end,
        # At which case you will see players only playing adjacent, because of the small added incentive      
        
        #Append the count, clear all the containers, repeat
        Winning_Line_Count.append(Count)
        Count = 0
        Special_Case_Count = 0 
        Opp_winning_lines.clear()
        Your_winning_lines.clear()
        Opp_Adjacency_list.clear()
        Your_Adjacency_list.clear()
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
    # print(max_val)
        
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


import time
global PLAYER_TURN
PLAYER_TURN = True
def Play_Game(Boardsize, Squares, Squares_to_win, Player=False,):
    '''
    Function to play entire game using all other functions. One ring, to rule them all!
    '''
    # Create_Player_Custom_Commands(Boardsize, Squares)
    Create_Board(Boardsize, Squares, "white", "Tic-Tac-Toe", "black", 2.5)
    Key_Dictionary = create_key_dict_and_coords(Boardsize, Squares)
    # print(Key_Dictionary)
    # print('-------------------------')
    Remaining_Dict_O = create_remaining_dict(Squares, Squares_to_win)
    # print(Remaining_Dict_O)
    # print('-------------------------')
    Remaining_Dict_X = create_remaining_dict(Squares, Squares_to_win)
    Adjacency_Dict1 = Adjacency_Dict(Squares)
    # print(Adjacency_Dict1)
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
    import sys 
    
    if Player==True:
        
        # Create_Player_Custom_Commands(Boardsize, Squares)
        Count = 0

        random_start = random.randint(0,1)
        if random_start == 0:
            Player=False
        else:
            Player=True  

        Game_over = False
        # global is_done_with_player_move
              
        while Game_over == False:
            
            # if Game_over == True:
                # print("shouldnt i be quitting?")
                # break        
            
            while Player==False:
                Terminator_Move(Remaining_Dict_O, Remaining_Dict_X, Key_Dictionary, Squares_to_win, List_of_X_moves, List_of_O_moves,\
                    Adjacency_Dict1)
                Coordinat = (computer_draw_customized_circle(Boardsize, Squares))
                key = (key_name(Key_Dictionary, Coordinat))
                
                # decrease_values(Remaining_dict_O, key)
                if decrease_values(Remaining_Dict_O, key, Updated_Dict) == 0:
                    print("O WINS!!!")
                    Game_over = True
                                           
                remove_dict(Key_Dictionary, Coordinat)
                Count +=1                   
                Player=True
                          
            
            while Player==True:
                
                def switch_players():
                    # This function allows the player to use the prompt to finish their loop, go through the computers loop
                    # And end up back at their loop again :)
                    #This will simulate the computer moving, but it won't create this loop
                    # print(Key_Dictionary)
                    # print(Player_COORD)
                                        
                                       
                    key = (key_name(Key_Dictionary, Player_COORD))
                    # print(key)
                    List_of_X_moves.append(key)
                    # decrease_values(Remaining_dict_X, key)
                    if decrease_values(Remaining_Dict_X, key, Updated_Dict) == 0:
                        turtle.textinput("X has won! ",  "Press Enter to quit")
                        turtle.bye()
                                    
                                        
                    remove_dict(Key_Dictionary, Player_COORD)
                   
                    #Check to see if game can no longer be won by either player  
                    if Variable10a == "no":

                        Winning_line_O_counts= []
                        Winning_line_X_counts = []    
                        for value in Remaining_Dict_O.values():
                            Winning_line_O_counts.append(value)
                        for value in Remaining_Dict_X.values():
                            Winning_line_X_counts.append(value)    
                        # print(Random_Best_Choice) 
                        max_val_O = max(Winning_line_O_counts)
                        max_val_X = max(Winning_line_X_counts)
                        # print(Remaining_Dict_O)
                        if max_val_O < Squares_to_win and max_val_X < Squares_to_win:
                            turtle.textinput("The game can no longer be won! ",  "Press Enter to quit")
                            turtle.bye()

                    Len_list = []
                    for key in Key_Dictionary.keys():
                        Len_list.append(key)
                    if len(Len_list) == 0:
                        turtle.textinput("Thanks for playing! ",  "Press Enter to quit")
                        turtle.bye()    
                    
                    #We want to test manually the size of the key dictionary here , if it is 0, or empty, we want to force
                    # close the screen                   

                    Terminator_Move(Remaining_Dict_O, Remaining_Dict_X, Key_Dictionary, Squares_to_win, List_of_X_moves, List_of_O_moves,\
                    Adjacency_Dict1)
                    Coordinat = (computer_draw_customized_circle(Boardsize, Squares))
                    
                     

                    key = (key_name(Key_Dictionary, Coordinat))
                    
                    # decrease_values(Remaining_dict_O, key)
                    if decrease_values(Remaining_Dict_O, key, Updated_Dict) == 0:
                        turtle.textinput("O has won! ",  "Press Enter to quit")
                        turtle.bye()
                    
                    list_o_keys = []                  
                    remove_dict(Key_Dictionary, Coordinat)
                    
                    
                    #Check to see if game can no longer be won by either player
                    if Variable10a == "no":
                    
                        Winning_line_O_counts= []
                        Winning_line_X_counts = []    
                        for value in Remaining_Dict_O.values():
                            Winning_line_O_counts.append(value)
                        for value in Remaining_Dict_X.values():
                            Winning_line_X_counts.append(value)    
                        # print(Random_Best_Choice) 
                        max_val_O = max(Winning_line_O_counts)
                        max_val_X = max(Winning_line_X_counts)
                        # print(Remaining_Dict_X)

                        if max_val_O < Squares_to_win and max_val_X < Squares_to_win:
                            turtle.textinput("The game can no longer be won! ",  "Press Enter to quit")
                            turtle.bye()
                    
                    #implement function that tests to see if game can not be won by anyone, and quits 

                    for key in Key_Dictionary.keys():
                        list_o_keys.append(key)
                    if (len(list_o_keys)) == 0:
                        turtle.textinput("Thanks for playing! ",  "Press Enter to quit")
                        turtle.bye()

                    # import time
                    global PLAYER_TURN
                    PLAYER_TURN = True    

                    

                    #Do we want to pause the time here


                Square_Length = round((Boardsize / np.sqrt(Squares)))
    
                speed = Square_Length

                player = turtle.Turtle()
                player.color("green")
                player.shape("square")
                player.penup()
                player.speed(7)
                player.shapesize(.5, .5, .5)
                    
                Starting_pos_x = -(Boardsize/2) + .5*(Square_Length) + (((np.sqrt(Squares)-1)/2) * Square_Length)
                Starting_pos_y = (Boardsize/2) - .5*(Square_Length) - (((np.sqrt(Squares)-1)/2) * Square_Length)
                
                player.setposition(Starting_pos_x , Starting_pos_y )
                player.setheading(90)
                
                movement = (Boardsize/Squares)*1.5
                
                
                    # print(player.pos())
                
                # def draw_circle():
                #     turtle.pensize(2.5)
                #     a = player.xcor()
                #     b = player.ycor()
                    
                #     coord_value = [a, b]
                            
                #     turtle.hideturtle()
                #     turtle.penup()
                #     turtle.setpos(a, (b-movement))

                #     turtle.pendown()
                #     turtle.circle(movement)
                #     turtle.hideturtle()

                    # print(coord_value)
                    # return coord_value 
                
                def draw_x():
                    turtle.pensize(2.5)
                    a = player.xcor()
                    b = player.ycor()
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.color("blue")
                    coord_value = [a, b]
                    
                    
                    list_of_Coords = []
                    
                    for key, coordinate in Key_Dictionary.items():
                        list_of_Coords.append(coordinate)
                    if coord_value in list_of_Coords:

                        #Forcing player to be in proper spot when making the X, or it will simply not draw
                        # And they will be forced to choose new spot...Fixing all potential mischief online    
                    
                        turtle.setposition(a-movement,b+movement)
                        turtle.pendown()
                        turtle.setposition(a+movement,b-movement)
                        turtle.penup()
                        turtle.setposition(a-movement,b-movement)
                        turtle.pendown()
                        turtle.setposition(a+movement,b+ movement)
                    
                        global Player_COORD 
                        Player_COORD = coord_value
                        global PLAYER_TURN
                        PLAYER_TURN = False
                        switch_players()
                
                def move_left():
                    
                    if PLAYER_TURN == True:

                        x = player.xcor()
                        x -= speed      
                        
                        if x < -(Boardsize/2)+ .5*(Square_Length):
                            x = -(Boardsize/2)+ .5*(Square_Length)
                        
                        player.setx(x)
                        player.setpos(x, player.ycor())
                    # print(player.pos())
                
                def move_right():
                    if PLAYER_TURN == True:
                        x = player.xcor()
                        x += speed
                        if x > (Boardsize/2) - .5*(Square_Length):
                            x = (Boardsize/2) - .5*(Square_Length)
                        player.setx(x)
                        player.setpos(x, player.ycor())
                    # print(player.pos())
                
                def move_up():
                    if PLAYER_TURN == True:

                        y = player.ycor()
                        y += speed
                        if y >  (Boardsize/2) - .5*(Square_Length):
                            y = (Boardsize/2) - .5*(Square_Length)
                        player.sety(y)
                        player.setpos(player.xcor(), y)
                    # print(player.pos())
                
                def move_down():
                    if  PLAYER_TURN == True:
                        y = player.ycor()
                        y -= speed
                        if y < -(Boardsize/2)+ .5*(Square_Length):
                            y = -(Boardsize/2)+ .5*(Square_Length)
                        player.sety(y)
                        player.setpos(player.xcor(), y)
                
                def quit_game():
                    turtle.textinput("See you later friend! ",  "Press Enter to quit")
                    turtle.bye()            
                    
                    

                        
                
                turtle.listen()
                
                
                turtle.onkey(move_left, "Left") 
                turtle.onkey(move_right, "Right")
                turtle.onkey(move_up, "Up") 
                turtle.onkey(move_down, "Down")
                # turtle.onkey(draw_circle, "o") 
                turtle.onkey(draw_x, "x")
                turtle.onkey(quit_game, "Escape")     

        

                
                
                # delay = input("Press enter to finish.")    
                
                # if Player==False:
                #     break

                
                if Count == Squares:
                    break

                turtle.mainloop()     
                            

                    
                  
if Variable8 == "yes":
    Play_Game(Variable1, Variable3, Variable4, Player=True)
if Variable8 == "no":
    Play_Game(Variable1, Variable3, Variable4, Player=False)
         #Player=True) #Player=True)
# Create_Board(800, 121, "white", "Tic-Tac-Toe", "black", 2.5)
# Create_Player_Custom_Commands(800, 121)
# Key_Dictionary = create_key_dict_and_coords(800, 121)
# print(player.pos())

#Game will always work if 2nd number is a square, and if 3rd number is <= np.sqrt of 2nd number
# Need to inform user of that, recommended boardsize is 800

          
# delay = input("Press enter to finish.")                



