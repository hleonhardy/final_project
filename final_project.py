#in displays.py we have marble display and laser display functions:
import displays  

#******************************************************************************#
#functions that will happen in the beginning of the game (before turns)
#******************************************************************************#

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


#This function allows us to make sure they enter an actual number when they're supposed to.
def check_make_int():
    """checks to see if the input is an integer and then converts it to an integer if it is"""
    
    loop_still_going = True
    while loop_still_going:
        number = raw_input("> ")
        #checking to see if they have entered a digit or not so that we can change it to int
        if number.isdigit() == True:
            number = int(number)
            loop_still_going = False
        else:
            print "Please enter an integer. "
    
    return number


def hit_next():
    """breaks up the instructions by pausing and letting the user type n or next"""

    #This doesn't return anything and it doesn't matter what they type
    #It just helps break up the instructions so that they won't be reading a billion lines at once.
    print "type 'next' or 'n' to see the next part of the instructions"
    see_next = raw_input("> ")
    


def instructions():
    """prints set of instructions on how to play the game"""

    #Displays instructions, features some demos with marble placing and laser shooting.
    #uses the hit next function to break it up a little

    print 
    print "Alright, so you wanna learn how to play the game."
    print "First we'll start with player 1:"
    print "Player 1 will choose locations in the black box (on the grid) to hide 3 marbles."
    print "Marbles are not allowed to be placed in the edge spaces, so please place them appropriately."
    print

    hit_next()

    demo_marble_1 = [2,2]
    demo_marble_2 = [2,4]
    demo_marble_3 = [4,6]

    displays.marble_display("no", demo_marble_1, demo_marble_2, demo_marble_3)
    print "Available marble spaces are represented by the '*' symbol."
    print "Here you can see the spaces available to place marbles in."

    hit_next()

    print "The first player will be prompted to enter the (row, column) for 3 marbles."
    print "Let's pretend we entered (3,3), (3,5), and (5,7) for our marble locations."

    hit_next()

    displays.marble_display("yes",demo_marble_1, demo_marble_2, demo_marble_3)
    print "Here is where our marbles are! "

    hit_next()

    print "Once player 1 has successfully placed 3 marbles, player 2 will begin."
    print "Player 2's job is to try to guess where player 1 has hidden the marbles."
    print "In order to do this, player 2 will send a laser beam through the box."
    print "Lasers must be sent through the very outer edges of the box, so choose accordingly."

    hit_next()

    demo_laser_in_1 = [3,1]
    demo_laser_out_1 = [3,1]

    demo_laser_in_2 = [9,2]
    demo_laser_out_2 = [4,1]

    demo_laser_in_3 = [9,4]
    demo_laser_out_3 = [9,4]

    displays.laser_display(demo_laser_in_1, demo_laser_out_1, "demo")
    print "Here are the available spaces (the 'o' spaces) that you can choose to send your laser through."
    print "These spaces represent the edge of the black box."

    hit_next()

    print "The laser, after being sent into the box, will interact with the marbles and then exit the box."
    print "There are a few different ways the laser can interact with the marbles."
    print "Here are the different ways: "

    hit_next()

    print "1. Direct Reflection: "
    print "if the laser hits a marble head on, it will reflect off the marble and go back the way it came. "
    print "for example, because we have a marble placed in (row 3, column 3), "
    print " we can get a direct reflection if we send our laser into the space (row 3, column 1). "

    hit_next()
    
    displays.laser_display(demo_laser_in_1, demo_laser_out_1, "laser")  
    print "This is what it will look like when player 2 selects the space listed previously. "
    print "The laser went in, reflected off the marble in (3,3), and came out the same space. "

    hit_next()  

    print "2. Deflection: "
    print "If the laser hits the side of the marble, it will be deflected 90 degrees. "
    print "It's a little hard to visualize with this display, but "
    print "the easiest way to picture this is that the laser is hitting the corner of the box "
    print "that the marble is in and then switching its direction 90 degrees from whichever corner "
    print "of the box that it hit. "

    hit_next()   

    print "That was probably confusing, so here's an example. "
    print "Let's go back to our marble in the space (3,3). "
    print "If we send a laser into the box (via row 9, column 2), "
    print "The laser will move up column 2 until it reaches row 4. "
    print "Once there, the laser will hit the lower left corner of the marble in (3,3). "
    print "It will then be deflected 90 degrees to the left and go out of the box via row 4."

    hit_next()

    displays.laser_display(demo_laser_in_2, demo_laser_out_2, "laser")
    print "Here you can see the laser entering through (9,2) and exiting out (4,1). "
    print "We can have deflections anywere and in any direction as long as the marble is in "
    print "the upper left or right diagonal relative to the forward direction the laser is traveling. "

    hit_next() 
    
    print "3. Double Marble Reflection: "
    print "This yields the same result as the direct reflection, only is caused by 2 marbles instead of 1. "
    print "Picture the laser being deflected to the left by a marble in the upper right diagonal, as in the example before, "
    print "only this time there is also a marble in the left diagonal. "
    print "This causes the laser to be reflected back the way it came. "

    hit_next() 

    print "If that was confusing, it's ok! "
    print "Here is an example: "
    print "Let's consider the marbles in (3,3) and (3,5). "
    print "Pretend we send a laser through the bottom in column 4 (space (9,4))."   
    print "The laser will move up column 4 and get deflected by both marbles, "
    print "causing it to move back down column 4 as if it had just been reflected directly. "

    hit_next()    

    displays.laser_display(demo_laser_in_3, demo_laser_out_3, "laser")
    print "Here we can see the laser exiting out the same space we sent it in. "

    hit_next() 

    print "4. Nothing: "
    print "Lastly, if the laser does not come close to any marbles, it will just pass through. "
    print "I think this one is pretty self explanitory. "

    hit_next()

    print "Ok, now player 2 has the option to send another beam or guess where the marbles are hidden. "
    print "The object of the game is to end up with LESS points than your opponent. "
    print "Players will recieve 1 point per laser sent through the box. "
    print "If guessing marbles, the player will also recieve 2 points for every INCORRECTLY guessed marble. "

    hit_next()

    print "After guessing the marbles correctly, "
    print "the players will switch turns. "
    print "Now, player 2 will send the marbles and player 1 will guess where they are. "
    print "After each person takes a turn guessing, the game will end "
    print "and the player with the LOWEST number of points will win! "

    hit_next()

    print "Best of luck! "
    print "Let's begin the game!"

    print "type 'next' or 'n' to begin! "

    see_next = raw_input("> ")
    see_next = see_next.lower() 




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
    

#******************************************************************************#
#functions having to do with the first player turn:
#******************************************************************************#


#will use these for all 3 marbles separately
def place_marble():
    """Asks where the player wants to place one marble, returns their potential marble coordinates"""


    print "enter the row where you would like to place your marble"
    marble_row = check_make_int()
    print "enter the column where you would like to place your marble"
    marble_column = check_make_int()
    #since the index starts at 0 but our display starts at 1,
    #This is to make the number they entered match the actual grid (not display)
    potential_marble_location = [marble_row - 1, marble_column - 1]



    return potential_marble_location



def check_marble_location(potential_marble_location,grid):
    """Checks to see if the potential marble space is an available space (0) and returns True or False"""

    #Marbles are not allowed in 1's, 2's, or 8's (or 3's-which is a space occupied by a marble).
    #This is checking to see if where they placed a marble was a zero on the grid

    if potential_marble_location[0] < 9 and potential_marble_location[1] < 9:

        if grid[potential_marble_location[0]][potential_marble_location[1]] == 0:
            available_space = True
        else:
            available_space = False
    else:
        available_space = False 


    return available_space



def placing_one_marble(grid):
    """obtaining appropriate marble location and return the coordinates"""

    marble_not_placed = True 
    #Checks to make sure that the user is inputting a valid location.
    while marble_not_placed:
        #User inputs location of marble they want to place:
        potential_marble_location = place_marble()
        #program checks to see if there is a zero (True) or anything else(False)
        available_space = check_marble_location(potential_marble_location,grid)

        #if the space is available, marble will be placed there and the grid will be updated with a 3
        if available_space == True:
                
            marble_location = potential_marble_location
            #note: even though this doesn't return the grid it is still able to update it 
            #because grid is returned inside the function placing_marbles_in_grid
            grid = placing_marbles_in_grid(grid, marble_location)

            marble_not_placed = False
        else:
            print "Please pick a valid space."


    return marble_location 



def placing_marbles_in_grid(grid,marble):
    """Replaces the 0's in the grid with 3's so they can be identified as marbles later, returns grid"""

    grid[marble[0]][marble[1]] = 3

    return grid 



#******************************************************************************#
#functions that have to do with the second player:
#******************************************************************************#



def ask_to_shoot_laser():
    """This function will ask which space the player wants to send the laser, returns chosen coordinates"""

    while True:

        print "Please enter the row where you would like to shoot your laser"
        row = check_make_int()
        print "Please enter the column where you would like to shoot your laser"
        column = check_make_int()

        if row < 10 and column < 10:
            #-1 on both because display starts at 1 and grid index starts at 0
            potential_laser_space = [row-1,column-1]
            break
        else:
            print "Please enter a valid space. "

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

    #Makes sure the user has picked a valid space for the laser
    while invalid_laser_space:
        potential_laser_space = ask_to_shoot_laser()
        laser_space_verdict = check_laser_space(potential_laser_space,grid)

        #creating variables to make it look better:

        row = potential_laser_space[0] 
        column = potential_laser_space[1]

        #if the space for the laser is available it will return the coordinates
        if laser_space_verdict == 1:
            laser_space = [row, column]
            invalid_laser_space = False
        else:
            print "please enter a valid space"


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



#******************************************************************************#
#These next functions are kind of like the "laser's turn:""
#******************************************************************************#



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
        # print "both diagonals are occupied by a marble"
        diagonal = "both_marble"

    #only the right diagonal is occupied by a marble:
    elif grid[right_row][right_column] == 3:
        # print "right diagonal is occupied by a marble"
        diagonal = "right_marble"

    #only the left diagonal is occupied by a marble:
    elif grid[left_row][left_column] == 3:
        # print " left diagonal is occupied by a marble"
        diagonal = "left_marble"

    #both diagonals are an outside space:
    elif grid[left_row][left_column] == 1 and grid[right_row][right_column] == 1:
        # print "both diagonals are outside spaces"
        diagonal = "both_outside"

    #The same result as outside spaces is also true for if the laser is moving through the outside spaces
    #Then it will hit the diagonals as an outside space and an edge space.
    #In other words, i'm going to call it both_outside even if one is an edge space because it will have the same effect

    elif grid[left_row][left_column] == 1 or grid[right_row][right_column] == 1:
        if grid[left_row][left_column] == 2 or grid[right_row][right_column] == 2:
            # print "One diagonal is an outside space and the other is an edge."
            diagonal = "both_outside"
        elif grid[left_row][left_column] == 0 or grid[right_row][right_column] == 0:
            # print "one is an outside space and one is unoccupied"
            diagonal = "both_empty"
    elif grid[left_row][left_column] == 2 and grid[right_row][right_column] == 2:
        diagonal = "both_edges"

    #otherwise both of them are empty =]
    else:
        diagonal = "both_empty"        
        # print "both are zeros"


    
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


    # print "new direction: {}".format(new_direction)
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

    # print laser_space
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

    # print "forward_space is {}".format(forward_space)
    return forward_space



def check_foward_space(forward_space, grid):
    """This will check to see if forward space is a marble or available space-returns a string of marble or unnocupied"""

    forward_row = forward_space[0]
    forward_column = forward_space[1]

    if grid[forward_row][forward_column] == 3:
        # print "There's a marble in the forward space"
        forward_space = "marble"

    elif grid[forward_row][forward_column] == 2:
        # print "This is an edge space."
        forward_space = "edge"

    else:
        # print "Theres nothing in the forward space"
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
            # print final_laser_space
            laser_still_moving = False

        elif diagonals == "right_marble" or diagonals == "left_marble":
            #change direction accordingly, then this will go back to check diagonals
            direction = change_direction_one_marble(diagonals,direction)
            # print "We have changed direction"
            # print "laser space is {}".format(laser_space)

        elif diagonals == "both_outside":
            #This will first move forward two spaces and that will be the final laser space
            final_laser_space = move_forward_two(laser_space, direction)
            # print "final laser space is {}".format(final_laser_space)
            laser_still_moving = False

        elif diagonals == "both_edges":
            #since both of the diagonals are edges the laser space has to move forward one space only
            final_laser_space = move_one_space_forward(laser_space, direction)
            # print "final_laser_space is {}".format(final_laser_space)
            laser_still_moving = False

        elif diagonals == "both_empty":
            #if both of them are empty, laser wil check the forward space
            forward_space = produce_forward_space(laser_space, direction)
            forward_space = check_foward_space(forward_space, grid)
            #if forward space is marble, reflect
            #if forward space is unoccupied, move one forward and check diagonals again
            if forward_space == "marble":
                final_laser_space = reflection(first_laser_space)
                # print "final laser space is {}".format(final_laser_space)
                laser_still_moving = False

            elif forward_space == "edge":
                final_laser_space = move_one_space_forward(laser_space, direction)
                laser_still_moving = False 

            elif forward_space == "unoccupied":
                laser_space = move_one_space_forward(laser_space, direction)
                # print "new laser space is {}".format(laser_space)


    return final_laser_space




#******************************************************************************#
#After the laser has taken its turn:
#******************************************************************************#


def add_one_to_score(player_total):
    """will add one to player_total and return the total score"""

    player_total = player_total + 1

    return player_total 


def guess_or_send():
    """asks the player if they would like to guess or send another beam-returns user input"""


    while True:

        print "Would you like to send another beam or guess where the marbles are? (send/guess) "
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

    while True:
        #gathering the coordinates for the marble guesses
        print "First marble: "
        print "Enter the row of your first marble"
        first_marble_row = check_make_int()
        print "Enter the column of your first marble"
        first_marble_column = check_make_int()

        if first_marble_row < 10 and first_marble_column < 10:
            break
        else:
            print "Please enter a valid location. "
    
    #Checking to make sure that the user enters 3 different spaces:

    while True:

        print
        print "Second marble: "
        print "Enter the row of your second marble"
        second_marble_row = check_make_int()
        print
        print "Enter the column of your second marble"
        second_marble_column = check_make_int()

        if first_marble_row == second_marble_row and first_marble_column == second_marble_column:
            print "You have already chosen this space. Please choose a different space. "
        elif second_marble_row < 10 and second_marble_column < 10:
            break
        else:
            print "please enter a valid location."



    while True: 

        print
        print "Third marble: "
        print "Enter the row of your third marble "
        third_marble_row = check_make_int()
        print
        print "Enter the column of your third marble"
        third_marble_column = check_make_int()

        if third_marble_row == second_marble_row and third_marble_column == second_marble_column:
            print "You have already chosen this space. Please choose a different space. "
        elif first_marble_row == third_marble_row and first_marble_column == third_marble_column:
            print "You have already chosen this space. Please choose a different space. "
        elif third_marble_row < 10 and third_marble_column < 10:
            break
        else:
            print "Please enter a valid location." 



    #Starting off with no marbles guessed incorrectly. because they haven't guessed yet.
    num_incorrect_marbles = 0

    #If their first marble space isn't occupied by a marble (3):
    if grid [first_marble_row-1][first_marble_column-1] != 3:
        num_incorrect_marbles += 1
    if grid[second_marble_row-1][second_marble_column-1]!= 3:
        num_incorrect_marbles += 1
    if grid[third_marble_row-1][third_marble_column-1] != 3:
        num_incorrect_marbles += 1

    print
    print "You have guessed {} marbles incorrectly.".format(num_incorrect_marbles)    
    print 
    return num_incorrect_marbles

    
#******************************************************************************#
#Function for one player's turn:
#******************************************************************************#


def players_turn (player_total, whose_turn_marble, whose_turn_laser):
    """first player places marbles, second player guesses where marbles are-returns first player total"""

    #These are for the display grid.
    #Since we aren't actually using any marble positions (the "no" part),
    #There doesn't have to be anything here, just a variable.
    marble_1 = []
    marble_2 = []
    marble_3 = []


    #Set up the grid:
    grid = set_up_grid()
    #This sets the marble display with no marbles placed.
    displays.marble_display("no", marble_1, marble_2, marble_3)
    
    #printing greatings
    print "Ok {}! Time to place your marbles! ".format(whose_turn_marble)
    print "Please select a space marked with a '*' to place your marbles. "




    #first player places marbles:
    #placing_one_marble also changes the grid space to a '3' so that they can't place a marble there again.
    marble_1 = placing_one_marble(grid)
    marble_2 = placing_one_marble(grid)
    marble_3 = placing_one_marble(grid)

    # grid = placing_marbles_in_grid(grid, marble_1, marble_2, marble_3) 
    # #displays the marbles as M's in the display grid
    displays.marble_display("yes", marble_1, marble_2, marble_3)


    #Player 2's turn:
    #This while loop, player_turn, is sending lasers until player_turn is turned to False 
    #(includes guessing, you can still send lasers after you guess)
    player_turn = True
    while player_turn:

        #This will display the grid with available laser spaces
        no_laser_in = []
        no_laser_out = []

        displays.laser_display(no_laser_in, no_laser_out, "demo")

        print "Ok {}. If you would like to see a picture of where your marbles are, ".format(whose_turn_marble)
        print "scroll up to the previous display. "
        print "Now, {}! It is your turn to shoot the laser into the box! ".format(whose_turn_laser)
        print "Please select an edge space (marked by an 'o') to shoot your laser.  "




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
        displays.laser_display(first_laser_display,final_laser_display, "laser")
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
                    # print player_total
                    player_turn = False  
                    guessing = False

                else:
                    #This is the part that adds the points gained from incorrectly guessing marbles to the score
                    added_points = num_incorrect_marbles*2
                    player_total = player_total + added_points
 
                    # print player_total

            #If they didn't choose to guess, setting guess = False will allow the "send laser" loop to begin again.
            else:
                guessing = False


    return player_total



#******************************************************************************#
#                             PLAYING GAME LOOP
#******************************************************************************#
#Putting together the player's turn function so that both players play
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

        # print "Player one places marbles and player 2 shoots laser"

        player_1_total = players_turn(player_1_total, "player 1", "player 2")
        
        #Player 2 goes, same process as player one. (each person only goes once)

        # print "Switch turns now!"
        # print "Player 2 place marbles and player 1 shoots lasers"
        player_2_total = players_turn(player_2_total, "player 2", "player 1")

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

        if will_you_continue == "no" or will_you_continue == "n":
            print "see you next time!"
            keep_playing = False



#******************************************************************************#
#******************************************************************************#
#******************************************************************************#


#ACTUAL GAME PLAY!

play_game()









