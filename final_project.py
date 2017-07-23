
#functions that will happen in the beginning of the game

def set_up_grid():
    """This function will set up the grid and return the 2d list that is the grid"""

    #8's are corners
    #2's are edge spaces
    #1's are outside spaces
    #0's mean nothing is there.


    #top edge row
    row_0 = [8,2,2,2,2,2,2,2,8]
    #outside row
    row_1 = [2,1,1,1,1,1,1,1,2]
    #normal rows
    row_2 = [2,1,0,0,0,0,0,1,2]
    row_3 = [2,1,0,0,0,0,0,1,2]
    row_4 = [2,1,0,0,0,0,0,1,2]
    row_5 = [2,1,0,0,0,0,0,1,2]
    row_6 = [2,1,0,0,0,0,0,1,2]
    #outside row
    row_7 = [2,1,1,1,1,1,1,1,2]
    #bottom edge row
    row_8 = [8,2,2,2,2,2,2,2,8]


    grid = [row_0,row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8]


    return grid 




def instructions():
    """prints set of instructions on how to play the game"""
    print 
    print "Alright, so you wanna learn how to play the game."
    print "First we'll start with player 1:"
    print "Player 1 will choose locations in the black box (on the grid) to hide 3 marbles."
    print "Marbles are not allowed to be placed in the edge spaces, so please place them appropriately."
    print
    print "type 'next' or 'n' to see the next part of the instructions"

    see_next = raw_input("> ")
    see_next = see_next.lower()

    print "Once player 1 has successfully placed 3 marbles, player 2 will begin."
    print "Player 2's job is to try to guess where player 1 has hidden the marbles."
    print "In order to do this, player 2 will send a laser beam through the box."
    print "Lasers must be sent through the very outer edges of the box, so choose accordingly."
    print
    print "Once player 2 sends the laser through the edge of the box, "
    print "the laser will be shown in its exiting position."
    print ""
    #I need to finish writing this



def greeting():
    """prints greeting"""

    print
    print
    print
    print "~~~---------------Black Box Game---------------~~~"
    print 
    print 
    print "Welcome players!"
    print "Would you like to see instructions on how to play the game?"
    yes_or_no = raw_input("> ")
    yes_or_no = yes_or_no.lower()

    if yes_or_no == "yes" or yes_or_no == "y":
        instructions()
    else:
        print "Alright then, let's begin!"

    print
    




#functions having to do with the first player:
#will use these for all 3 marbles separately



def place_marble():
    """Asks where the player wants to place one marble, returns their potential marble coordinates"""

    print "enter the row where you would like to place your marble"
    marble_row = int(raw_input("> "))
    print "enter the column where you would like to place your marble"
    marble_column = int(raw_input("> "))

    potential_marble_location = [marble_row - 1, marble_column - 1]

    print potential_marble_location
    return potential_marble_location



def check_marble_location(potential_marble_location,grid):
    """Checks to see if the potential marble space is an available space (0) and returns True or False"""

    #-Note-maybe i should change this later into "available" or "unavailable" to stay consistent with other
    #parts of the code-
    #Marbles are not allowed in 1's, 2's, or 8's.
    #This is checking to see if where they placed a marble was a zero on the grid
    if grid[potential_marble_location[0]][potential_marble_location[1]] == 0:
        available_space = True
    else:
        available_space = False 


    return available_space




def placing_one_marble(grid):
    """obtaining appropriate marble location and return the coordinates"""

    marble_not_placed = True 

    while marble_not_placed:
        potential_marble_location = place_marble()
        available_space = check_marble_location(potential_marble_location,grid)

        if available_space == True:
                
            marble_location = potential_marble_location

            marble_not_placed = False
        else:
            print "Please pick a valid space."



    return marble_location 



def placing_marbles_in_grid(grid,marble_1,marble_2,marble_3):


    grid[marble_1[0]][marble_1[1]] = 3
    grid[marble_2[0]][marble_2[1]] = 3
    grid[marble_3[0]][marble_3[1]] = 3


    for row in grid:
        print row

    return grid 




#functions that have to do with the second player:


def ask_to_shoot_laser():
    """This function will ask which space the player wants to send the laser, returns chosen coordinates"""

    print "Please enter the row where you would like to shoot your laser"
    row = int(raw_input("> "))
    print "Please enter the column where you would like to shoot your laser"
    column = int(raw_input("> "))

    potential_laser_space = [row-1,column-1]

    return potential_laser_space 



def check_laser_space(potential_laser_space,grid):
    """checks to see if the space they entered was an appropriate edge space, returns verdict"""

    #-Note-to make this more consistent with the rest maybe change verdict into "good" or "not an edge" or something
    #defining some variables to make it look prittier down below
    row = potential_laser_space[0] 
    column = potential_laser_space[1]
    laser = grid[row][column]

    #The laser has to go in a 2 space otherwise it won't work.
    #The verdict is 1 for the laser space being a 2
    #the verdict is 0 for the laser space being anything else
    if laser == 2:
        laser_space_verdict = 1
    else:
        laser_space_verdict = 0


    return laser_space_verdict  



def laser_shooting_loop(grid):
    """asks to shoot laser until it is a valid space, returns the laser's position"""

    laser_space = []
    invalid_laser_space = True


    while invalid_laser_space:
        potential_laser_space = ask_to_shoot_laser()
        laser_space_verdict = check_laser_space(potential_laser_space,grid)
        row = potential_laser_space[0] 
        column = potential_laser_space[1]
        if laser_space_verdict == 1:
            laser_space = [row, column]
            invalid_laser_space = False
        else:
            print "please enter a valid space"

    print laser_space
    return laser_space



def return_first_direction(laser_space):
    """figures out the direction based on the edge-returns direction"""

    row = laser_space[0]
    column = laser_space[1]

    if row == 0: #top row
        direction = "down"
    elif row == 8: #bottom row
        direction = "up"
    elif column == 0: #left side
        direction = "right"
    elif column == 8: #right hand side
        direction = "left"

    return direction 







#These next functions are kind of like the "laser's turn:""


def move_one_space_forward(laser_space, direction):
    """will move the "laser's position" one step forward, return's the laser's space"""

    #position gets moved one space forward because there are no marbles allowed in outside spaces (1's)
    #so we want the checking and moving process to start when the laser is in the 1 space
    #because it is redundant to check the diagonals etc if we know they're just going to be 1's
    #also will just get messed up if we don't do this anyway

    if direction == "down": #row is changing down one, column isn't changing
        laser_space = [laser_space[0]+1,laser_space[1]]
    elif direction == "up": #row is changing up one, column isn't changing
        laser_space = [laser_space[0]-1, laser_space[1]]
    elif direction == "right": #row isn't changing, column is going right one
        laser_space = [laser_space[0],laser_space[1]+1]
    elif direction == "left": #row isn't changing, column is going left one
        laser_space = [laser_space[0],laser_space[1]-1]


    print laser_space
    return laser_space     


#Checking diagonals:


def produce_left_diagonal(laser_space, direction):
    """will find and return coordinates for the left diagonal"""

    if direction == "down":
        #row plus 1, column plus 1
        left_diagonal = [laser_space[0]+1, laser_space[1]+1]
    elif direction == "up":
        #row minus one, column minus 1
        left_diagonal = [laser_space[0]-1, laser_space[1]-1]
    elif direction == "right":
        #row minus 1, column plus 1
        left_diagonal = [laser_space[0]-1, laser_space[1]+1]
    elif direction == "left":
        #row plus 1, column minus 1
        left_diagonal = [laser_space[0]+1, laser_space[1]-1]

    return left_diagonal


def produce_right_diagonal(laser_space, direction):
    """this will find and return coordinates for the right diagonal"""

    if direction == "down":
        #row plus 1, column minus 1 
        right_diagonal = [laser_space[0]+1, laser_space[1]-1]
    elif direction == "up":
        #row minus 1, column plus 1
        right_diagonal = [laser_space[0]-1, laser_space[1]+1]
    elif direction == "right":
        #row plus 1, column plus 1
        right_diagonal = [laser_space[0]+1, laser_space[1]+1]
    elif direction == "left":
        #row minus 1, column minus 1
        right_diagonal = [laser_space[0]-1, laser_space[1]-1]

    return right_diagonal



def check_diagonals(grid, laser_space, direction):
    """this function will check the diagonal spaces in the grid and return what is in them as a string"""

    #diagonals will be coordinates relative to the laser's space
    #will be in the form [row, column]
    #can check what is in that spot on the grid by grid[row][column]

    #finding the diagonal spaces:
    left_diagonal = produce_left_diagonal(laser_space, direction)
    right_diagonal = produce_right_diagonal(laser_space, direction)

    #recall marbles are 3, outside spaces are 2, edge spaces are 1, available spaces are 0
    #we should only be dealing with an outside space or a marble or available space.

    #just making things easier to write here:
    left_row = left_diagonal[0]
    left_column = left_diagonal[1]

    right_row = right_diagonal[0]
    right_column = right_diagonal[1]


    #both diagonals occupied by a marble:
    if grid[left_row][left_column] == 3 and grid[right_row][right_column] == 3:
        print "both diagonals are occupied by a marble"
        diagonal = "both_marble"

    #only the right diagonal is occupied by a marble:
    elif grid[right_row][right_column] == 3:
        print "right diagonal is occupied by a marble"
        diagonal = "right_marble"

    #only the left diagonal is occupied by a marble:
    elif grid[left_row][left_column] == 3:
        print " left diagonal is occupied by a marble"
        diagonal = "left_marble"

    #both diagonals are an outside space:
    elif grid[left_row][left_column] == 1 and grid[right_row][right_column] == 1:
        print "both diagonals are outside spaces"
        diagonal = "both_outside"

    #The same result as outside spaces is also true for if the laser is moving through the outside spaces
    #Then it will hit the diagonals as an outside space and an edge space.
    #In other words, i'm going to call it both_outside even if one is an edge space because it will have the same effect

    elif grid[left_row][left_column] == 1 or grid[right_row][right_column] == 1:
        if grid[left_row][left_column] == 2 or grid[right_row][right_column] == 2:
            print "One diagonal is an outside space and the other is an edge."
            diagonal = "both_outside"
        elif grid[left_row][left_column] == 0 or grid[right_row][right_column] == 0:
            print "one is an outside space and one is unoccupied"
            diagonal = "both_empty"
    elif grid[left_row][left_column] == 2 and grid[right_row][right_column] == 2:
        diagonal = "both_edges"

    #otherwise both of them are empty =]
    else:
        diagonal = "both_empty"        
        print "both are zeros"


    
    return diagonal





#this function will be used if only one of the diagonals is occupied by a marble:

def change_direction_one_marble(diagonals, direction):
    """uses whether it is left or right diagonal and the direction to change the direction of the laser, returns direction"""

    #note: diagonals are from "laser's point of view" 
    #e.g. left diagonal if direction is left will look like the down diagonal from user point of view

    #if the laser is going up and interacts with a left diagonal or right diagonal marble
    if direction == "up" and diagonals == "left_marble":
        new_direction = "right"

    elif direction == "up" and diagonals == "right_marble":
        new_direction = "left"

    #if the laser is going down and interacts with marble in left or right diagonal
    elif direction == "down" and diagonals == "left_marble":
        new_direction = "left"

    elif direction == "down" and diagonals == "right_marble":
        new_direction = "right"

    #if the laser is going left and interacts with marble in left or right diagonal
    elif direction == "left" and diagonals == "left_marble":
        new_direction = "up"

    elif direction == "left" and diagonals == "right_marble":
        new_direction = "down"

    #if the laser is going right and interacts with marble in left or right diagonal
    elif direction == "right" and diagonals == "left_marble":
        new_direction = "down"

    elif direction == "right" and diagonals == "right_marble":
        new_direction = "up"


    print "new direction: {}".format(new_direction)
    return new_direction


#This function will be used if both diagonals are an outside space

def move_forward_two(laser_space, direction):
    """his function will move the laser space forward two spaces-returns laser's space"""


    if direction == "down": #row is changing down two, column isn't changing
        laser_space = [laser_space[0]+2,laser_space[1]]
    elif direction == "up": #row is changing up two, column isn't changing
        laser_space = [laser_space[0]-2, laser_space[1]]
    elif direction == "right": #row isn't changing, column is going right two
        laser_space = [laser_space[0],laser_space[1]+2]
    elif direction == "left": #row isn't changing, column is going left two
        laser_space = [laser_space[0],laser_space[1]-2]

    print laser_space
    return laser_space 
    


#This function will be used if neither diagonal is occupied by a marble (and also not by two outside spaces)

def produce_forward_space(laser_space, direction):
    """checks to see what is in the forward space, returns the number that is the forward space"""

    #This is VERY similar to the move one space forward function
    #The difference is we aren't moving the laser, we are creating a new forward space to check in another function.

    if direction == "down": #row is down one, column isn't changing
        forward_space = [laser_space[0]+1, laser_space[1]]

    elif direction == "up": #row is up one, column isn't changing
        forward_space = [laser_space[0]-1, laser_space[1]]

    elif direction == "right": #row isn't changing, column is right one
        forward_space = [laser_space[0],laser_space[1]+1]

    elif direction == "left": #row isn't changing, column is left one
        forward_space = [laser_space[0],laser_space[1]-1]

    print "forward_space is {}".format(forward_space)
    return forward_space



def check_foward_space(forward_space, grid):
    """This will check to see if forward space is a marble or available space-returns a string of marble or unnocupied"""

    forward_row = forward_space[0]
    forward_column = forward_space[1]

    if grid[forward_row][forward_column] == 3:
        print "There's a marble in the forward space"
        forward_space = "marble"

    else:
        print "Theres nothing in the forward space"
        forward_space = "unoccupied"


    return forward_space



#This function will be used if there is a marble in a forward space or if both diagonals are occupied

def reflection(first_laser_space):
    """This function will make laser_space into the the original laser space-returns final laser space"""

    final_laser_space = first_laser_space 


    return final_laser_space



#Putting the checking and moving actions together:

def checking_moving_loop(laser_space, first_laser_space, grid, direction):
    """This will loop through checking spaces and moving accordingly-returns the final laser space"""

    #we start one space forward from the original laser space.

    laser_still_moving = True

    while laser_still_moving:

        #Check diagonals
        diagonals = check_diagonals(grid, laser_space, direction)

        if diagonals == "both_marble":
            #reflection will cause the laser to go back to the initial space, the loop will end
            final_laser_space = reflection(first_laser_space)
            print final_laser_space
            laser_still_moving = False

        elif diagonals == "right_marble" or diagonals == "left_marble":
            #change direction accordingly, then this will go back to check diagonals
            direction = change_direction_one_marble(diagonals,direction)
            print "We have changed direction"
            print "laser space is {}".format(laser_space)

        elif diagonals == "both_outside":
            #This will first move forward two spaces and that will be the final laser space
            final_laser_space = move_forward_two(laser_space, direction)
            print "final laser space is {}".format(final_laser_space)
            laser_still_moving = False

        elif diagonals == "both_edges":
            #since both of the diagonals are edges the laser space has to move forward one space only
            final_laser_space = move_one_space_forward(laser_space, direction)
            print "final_laser_space is {}".format(final_laser_space)
            laser_still_moving = False

        elif diagonals == "both_empty":
            #if both of them are empty, laser wil check the forward space
            forward_space = produce_forward_space(laser_space, direction)
            forward_space = check_foward_space(forward_space, grid)
            #if forward space is marble, reflect
            #if forward space is unoccupied, move one forward and check diagonals again
            if forward_space == "marble":
                final_laser_space = reflection(first_laser_space)
                print "final laser space is {}".format(final_laser_space)
                laser_still_moving = False

            elif forward_space == "unoccupied":
                laser_space = move_one_space_forward(laser_space, direction)
                print "new laser space is {}".format(laser_space)


    return final_laser_space







def show_ending_location(final_laser_space):
    """this function will tell the user the final space of the laser"""

    #for now...

    print final_laser_space



def add_one_to_score(player_total):
    """will add one to player_total and return the total score"""

    player_total = player_total + 1

    return player_total 


def guess_or_send():
    """asks the player if they would like to guess or send another beam-returns user input"""


    while True:

        print "Would you like to send another beam or guess where the mables are? "
        send_or_guess = raw_input("> ")
        send_or_guess = send_or_guess.lower()

        if send_or_guess != "guess":
        
            if send_or_guess != "send":
                print "please enter either send or guess"
            else:
                break
        else:
            break


    return send_or_guess



#this function will be used if they choose to guess the locations of the marbles

def guess_marble_locations(grid):
    """asks user where the guesses are and checks to see if there are marbles there-returns number of inccorectly placed marbles"""

    #I could have done this better
    #Fix this later to catch if they enter an invalid number 

    #gathering the coordinates for the marble guesses
    print "First marble: "
    print "Enter the row of your first marble"
    first_marble_row = int(raw_input("> "))
    print "Enter the column of your first marble"
    first_marble_column = int(raw_input("> "))
    print "Second marble: "
    print "Enter the row of your second marble"
    second_marble_row = int(raw_input("> "))
    print "Enter the column of your second marble"
    second_marble_column = int(raw_input("> "))
    print "Third marble: "
    print "Enter the row of your third marble "
    third_marble_row = int(raw_input("> "))
    print "Enter the column of your third marble"
    third_marble_column = int(raw_input("> "))

    num_incorrect_marbles = 0

    if grid [first_marble_row-1][first_marble_column-1] != 3:
        num_incorrect_marbles += 1
    if grid[second_marble_row-1][second_marble_column-1]!= 3:
        num_incorrect_marbles += 1
    if grid[third_marble_row-1][third_marble_column-1] != 3:
        num_incorrect_marbles += 1

    print "num incorrect marbles = {}".format(num_incorrect_marbles)    
    return num_incorrect_marbles

    



def players_turn (player_total):
    """first player places marbles, second player guesses where marbles are-returns first player total"""


    marble_1 = []
    marble_2 = []
    marble_3 = []


    #Set up the grid:
    grid = set_up_grid()
    marble_display("no", marble_1, marble_2, marble_3)
    

    #first player places marbles:
    marble_1 = placing_one_marble(grid)
    marble_2 = placing_one_marble(grid)
    marble_3 = placing_one_marble(grid)

    grid = placing_marbles_in_grid(grid, marble_1, marble_2, marble_3) 

    marble_display("yes", marble_1, marble_2, marble_3)


    #Player 2's turn:
    #This while loop, player_turn, is sending lasers until player_turn is turned to False 
    #(includes guessing, you can still send lasers after you guess)
    player_turn = True
    while player_turn:

        #The first space player 2 chooses to send the laser
        first_laser_space = laser_shooting_loop(grid)

        #Initial direction determined by the first laser space
        direction = return_first_direction(first_laser_space)

        #After determining the direction, we will move one space forward to make everything easier.        
        # print "laser space = {}".format(first_laser_space)
        laser_space = move_one_space_forward(first_laser_space, direction)
        # print "new laser_space = {}".format(laser_space)

        #This is the entire process of the laser moving through the black box, becoming the final space
        final_laser_space = checking_moving_loop(laser_space, first_laser_space, grid, direction)

        first_laser_display = [first_laser_space[0] + 1, first_laser_space[1] + 1]
        final_laser_display = [final_laser_space[0] + 1, final_laser_space[1] + 1]
        laser_display(first_laser_display,final_laser_display)
        #Adding one point per laser sent to the player's total.
        player_total += 1
        

        #Guessing process: This loop will allow the player to guess as many times as they want
        #It adds two points per incorrectly guessed marble to their score
        guessing = True
        while guessing:
            #Determines whether or not the player wants to guess or send
            send_or_guess = guess_or_send()
            if send_or_guess == "guess":
                #figures out how many marbles have been guessed incorrectly
                num_incorrect_marbles = guess_marble_locations(grid)
                #if they have guessed all the marbles correctly then the whole turn is over
                if num_incorrect_marbles == 0:
                    print player_total
                    player_turn = False  
                    guessing = False

                else:
                    #This is the part that adds the points gained from incorrectly guessing marbles to the score
                    added_points = num_incorrect_marbles*2
                    player_total = player_total + added_points
 
                    print player_total

            #If they didn't choose to guess, setting guess = False will allow the "send laser" loop to begin again.
            else:
                guessing = False


    return player_total




#*******************************************************************************#

#This is the display for the marbles!

def marble_display(marble_available, marble_1, marble_2, marble_3):
    """prints available marble spaces"""



    top_one = []
    top_two = []
    top_three = []
    top_four = []
    top_five = []

    row_0 = []

    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []
    row_5 = []
    row_6 = []
    row_7 = []
    row_8 = []
    row_9 = []

    row_10 = []

    bottom_five = []
    bottom_four = []
    bottom_three = []
    bottom_two = []
    bottom_one = []


    column_space = "    "
    marble_spaces = "  * "
    marble_in_space = "  M "

    grid = [top_one, top_two, top_three, top_four, top_five, \
            row_0, row_1, row_2, row_3, row_4, row_5, \
            row_6, row_7, row_8, row_9, row_10, \
            bottom_five, bottom_four, bottom_three, bottom_two, bottom_one]



    top_rows = [top_one, top_two, top_three, top_four, top_five]

    main_rows = [row_1, row_2, row_3, row_4, row_5, \
                 row_6, row_7, row_8, row_9]

    upper_two = [row_1, row_2]
    marble_rows = [row_3,row_4,row_5,row_6,row_7]
    main_bottom_row = [row_8,row_9]

    bottom_rows = [bottom_five, bottom_four, bottom_three, bottom_two, bottom_one]



    #Divider row:

    divider = "-----"
    divider_row = []

    i = 0
    while i < 11:
        divider_row.append(divider)
        i += 1

    #adding an extra dash between the side and the first divider because it works
    divider_display = "  {}-{}{}{}{}{}{}{}{}{}{} " \
                        .format(column_space,divider_row[1],divider_row[2],\
                         divider_row[3],divider_row[4],divider_row[5],divider_row[6],\
                         divider_row[7], divider_row[8], divider_row[9],column_space)





    #Making every list in the top and bottom sections a list of spaces (column side)
    for row in top_rows:
        i = 0
        while i < 12:
            row.append(column_space)
            i += 1
         

    for row in bottom_rows:
        i = 0
        while i < 12:
            row.append(column_space)
            i += 1
          


    #making the rows:

    #row_0 and row_10:

    row_0 = range(11)
    row_10 = range(11)


    #main rows (1-9)
    #top two rows:
    
    for row in upper_two:
        i = 0
        while i < 12:
            row.append(column_space)
            i += 1

    #2-7:

    
    for row in marble_rows:
        i = 0
        while i < 12:
            if i < 3:
                row.append(column_space)
                i += 1
            elif i > 2 and i < 8:
                row.append(marble_spaces)
                i += 1
            else:
                row.append(column_space)
                i += 1

    if marble_available == "yes":

        marble_1_row = marble_1[0]
        marble_1_column = marble_1[1]

        marble_2_row = marble_2[0]
        marble_2_column = marble_2[1]

        marble_3_row = marble_3[0]
        marble_3_column = marble_3[1]


        main_rows[marble_1_row ][marble_1_column + 1] = marble_in_space
        main_rows[marble_2_row ][marble_2_column + 1] = marble_in_space
        main_rows[marble_3_row ][marble_3_column + 1] = marble_in_space




    #bottom two rows:


    for row in main_bottom_row:
        i = 0
        while i < 12:
            row.append(column_space)
            i += 1


    #Displaying the rows:


    for item in top_rows:
        display_row = "  {}   {}   {}   {}   {}   {}   {}   {}  {}  {}  {}" \
                       .format(item[0],item[1],item[2],\
                        item[3],item[4],item[5],item[6],\
                        item[7], item[8], item[9], item[10] )
        print display_row 




    row_0_display = "         {}    {}    {}    {}    {}    {}    {}    {}    {}   " \
                       .format(row_0[1],row_0[2],\
                        row_0[3],row_0[4],row_0[5],row_0[6],\
                        row_0[7], row_0[8], row_0[9])

    print row_0_display
    print divider_display

    i = 1

    for item in main_rows:

        display_row = "    {} |{}|{}|{}|{}|{}|{}|{}|{}|{}| {}" \
                        .format(i,item[1],item[2],\
                        item[3],item[4],item[5],item[6],\
                        item[7], item[8], item[9], i)
        print display_row
        if i < 11:
            print divider_display
            i += 1


    row_10_display = "         {}    {}    {}    {}    {}    {}    {}    {}    {}   " \
                       .format(row_10[1],row_10[2],\
                        row_10[3],row_10[4],row_10[5],row_10[6],\
                        row_10[7], row_10[8], row_10[9])
    print row_10_display



    for item in bottom_rows:
        display_row = "  {}   {}   {}   {}   {}   {}   {}   {}  {}  {}  {}" \
                       .format(item[0],item[1],item[2],\
                        item[3],item[4],item[5],item[6],\
                        item[7], item[8], item[9], item[10] )
        print display_row 


    return main_rows



#******************************************************************************#

#Laser space displays!!
def laser_display(in_laser, out_laser):

    """Prints the display for showing available laser spaces"""


    laser_mark = "  o "
    column_space = "    "

    right_arrow =  " -> "

    vertical_dash = " |  "

    top_point = " v  "

    left_arrow =  " <- "

    bottom_point = " ^  "



    top_one = []
    top_two = []
    top_three = []
    top_four = []
    top_five = []

    row_0 = []

    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []
    row_5 = []
    row_6 = []
    row_7 = []
    row_8 = []
    row_9 = []

    row_10 = []

    bottom_five = []
    bottom_four = []
    bottom_three = []
    bottom_two = []
    bottom_one = []






    grid = [top_one, top_two, top_three, top_four, top_five, \
            row_0, row_1, row_2, row_3, row_4, row_5, \
            row_6, row_7, row_8, row_9, row_10, \
            bottom_five, bottom_four, bottom_three, bottom_two, bottom_one]



    top_rows = [top_one, top_two, top_three, top_four, top_five]


    main_rows = [row_2, row_3, row_4, row_5, \
                 row_6, row_7, row_8]

    grid_rows = [row_1,row_2, row_3, row_4, row_5, \
                 row_6, row_7, row_8, row_9]

    marble_rows = [row_3,row_4,row_5,row_6,row_7]

    end_two_rows = [row_1, row_9]


    

    bottom_rows = [bottom_five, bottom_four, bottom_three, bottom_two, bottom_one]






    divider = "-----"
    divider_row = []

    i = 0
    while i < 11:
        divider_row.append(divider)
        i += 1

    divider_display = "  {}-{}{}{}{}{}{}{}{}{}{} " \
                        .format(column_space,divider_row[1],divider_row[2],\
                         divider_row[3],divider_row[4],divider_row[5],divider_row[6],\
                         divider_row[7], divider_row[8], divider_row[9],column_space)




#Making every list in the top and bottom sections a list of spaces (column side)
    for row in top_rows:
        i = 0
        while i < 12:
            row.append(column_space)
            i += 1
         

    for row in bottom_rows:
        i = 0
        while i < 12:
            row.append(column_space)
            i += 1
          


    #making the rows:

    #row_0 and row_10:

    row_0 = range(11)
    row_10 = range(11)


    #main rows (1-9)
    #Edges

    left_side_numbers = "    "
    right_side_numbers = "    "

    for row in end_two_rows:
        i = 0
        while i < 11:
            if i == 0:
                row.append(left_side_numbers)
                i += 1
            if i < 2:
                row.append(column_space)
                i += 1
            elif i > 1 and i < 9:
                row.append(laser_mark)
                i += 1
            elif i == 10:
                row.append(right_side_numbers)
                i += 1
            else:
                row.append(column_space)
                i += 1

    for row in main_rows:
        i = 0
        while i < 11:
            if i == 1 or i == 9:
                row.append(laser_mark)
                i += 1
            else:
                row.append(column_space)
                i += 1






    #going in:

    
    if in_laser[0] == 1:
        top_four[in_laser[1]] = vertical_dash
        top_five[in_laser[1]] = top_point
    elif in_laser[0] == 9:
        bottom_four[in_laser[1]] = vertical_dash
        bottom_five[in_laser[1]] = bottom_point
    elif in_laser[1] == 1:
        grid_rows[in_laser[0]-1][0] = right_arrow
    elif in_laser[1] == 9:
        grid_rows[in_laser[0]-1][10] = left_arrow

    #going out:


    if out_laser[0] == 1:
        top_four[out_laser[1]] = bottom_point
        top_five[out_laser[1]] = vertical_dash
    elif out_laser[0] == 9:
        bottom_four[out_laser[1]] = top_point
        bottom_five[out_laser[1]] = vertical_dash
    elif out_laser[1] == 1:
        grid_rows[out_laser[0]-1][0] = left_arrow
    elif out_laser[1] == 9:
        grid_rows[out_laser[0]-1][10] = right_arrow


    for item in top_rows:
        display_row = "   {} {} {} {} {} {} {} {} {} {} {} " \
                       .format(item[0],item[1],item[2],\
                        item[3],item[4],item[5],item[6],\
                        item[7], item[8], item[9], item[10] )
        print display_row 



    row_0_display = "         {}    {}    {}    {}    {}    {}    {}    {}    {}   " \
                       .format(row_0[1],row_0[2],\
                        row_0[3],row_0[4],row_0[5],row_0[6],\
                        row_0[7], row_0[8], row_0[9])

    print row_0_display
    print divider_display

    



    i = 0
    for item in grid_rows:

        display_row = "{}{} |{}|{}|{}|{}|{}|{}|{}|{}|{}| {}{}" \
                        .format(item[0],i+1,item[1],item[2],\
                        item[3],item[4],item[5],item[6],\
                        item[7], item[8], item[9], i+1,item[10])
        print display_row
        if i < 11:
            print divider_display
            i += 1


    row_10_display = "         {}    {}    {}    {}    {}    {}    {}    {}    {}   " \
                       .format(row_10[1],row_10[2],\
                        row_10[3],row_10[4],row_10[5],row_10[6],\
                        row_10[7], row_10[8], row_10[9])
    print row_10_display



    for item in bottom_rows:
        display_row = "   {} {} {} {} {} {} {} {} {} {} {} " \
                       .format(item[0],item[1],item[2],\
                        item[3],item[4],item[5],item[6],\
                        item[7], item[8], item[9], item[10] )
        print display_row 


#******************************************************************************#


#The function that plays the game:

def play_game():
    """PLaying the game!"""
 
    #prints greeting and instructions:
    greeting()

    #after the game is over, they can choose to play again
    #keep_playing is if they continue to play

    keep_playing = True
    while keep_playing:      

        #start with both player's scores at zero
        player_1_total = 0
        player_2_total = 0

        #First player goes. 
        #Players turn returns the total score, this is assigned to player 1's score

        print "Player one places marbles and player 2 shoots laser"
        player_1_total = players_turn(player_1_total)
        
        #Player 2 goes, same process as player one. (each person only goes once)

        print "Switch turns now!"
        print "Player 2 place marbles and player 1 shoots lasers"
        player_2_total = players_turn(player_2_total)

        #printing the total scores

        print "Player 1's total adds up to {}".format(player_1_total)
        print "And player 2's total adds up to {}".format(player_2_total)

        #lower score is the winner!

        if player_1_total < player_2_total:
            print "Player 1 is the winner! Congratulations player 1!"
        elif player_1_total > player_2_total:
            print "Player 2 is the winner! Congratulations player 2!"
        else:
            print "Looks like you two have tied."


        #asking if they want to play again:

        print "Would you like to play again?"
        will_you_continue = raw_input("> ")
        will_you_continue = will_you_continue.lower()

        if will_you_continue == "no":
            print "see you next time!"
            keep_playing = False



#******************************************************************************#



#ACTUAL GAME PLAY!

play_game()









