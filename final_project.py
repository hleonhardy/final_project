
#functions that will happen in the beginning of the game

def set_up_grid():
    """This function will set up the coordinates"""

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



def greeting():
    """prints greeting"""

    #Add code
    #prints greeting 
    #prints instructions

    print
    




#functions having to do with the first player:
#will use these for all 3 marbles separately


def place_marble():
    """Asks where the player wants to place one marble, returns marble coordinates"""

    print "enter the row where you would like to place your marble"
    marble_row = int(raw_input("> "))
    print "enter the column where you would like to place your marble"
    marble_column = int(raw_input("> "))

    potential_marble_location = [marble_row, marble_column]


    return potential_marble_location



def check_marble_location(potential_marble_location,grid):
    """Checks to see if a marble can be placed and returns True or False"""

    #Marbles are not allowed in 1's, 2's, or 8's.
    #This is checking to see if where they placed a marble was a zero on the grid
    if grid[potential_marble_location[0]][potential_marble_location[1]] == 0:
        available_space = True
    else:
        available_space = False 


    return available_space



def marble_placing_loop(grid):
    """checks to see whether the marble space is available then places/asks to place another marble"""

    #until they input 3 total marbles, this loop will keep asking where they want to place a marble.
    i = 0
    while i < 3:
        #Getting the marble location, place_marble will return row and column
        potential_marble_location = place_marble()
        #check_marble_location returns True for if the space is available and false for if its not.
        available_space = check_marble_location(potential_marble_location,grid)
        
        if available_space == True:
            grid[potential_marble_location[0]][potential_marble_location[1]] = 3
            i += 1
        else:
            print "Please pick a valid space."


    return grid 





#functions that have to do with the second player:


def ask_to_shoot_laser():
    """This function will ask which space the player wants to send the laser, returns chosen coordinates"""

    print "Please enter the row where you would like to shoot your laser"
    row = int(raw_input("> "))
    print "Please enter the column where you would like to shoot your laser"
    column = int(raw_input("> "))

    potential_laser_space = [row,column]

    return potential_laser_space 


def check_laser_space(potential_laser_space,grid):
    """checks to see if the space they entered was an appropriate edge space"""

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
    """returns direction"""

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







#These next functions are kind of like the laser's turn


def move_one_space_forward(laser_space, direction):
    """will move the "laser's position" one step forward"""

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
    """will return coordinates for the left diagonal"""

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
    """this will give coordinates for the right diagonal"""

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
    """this function will check the diagonal spaces in the grid"""

    #diagonals will be coordinates relative to the laser's space
    #will be in the form [row, column]
    #can check what is in that spot on the grid by grid[row][column]

    left_diagonal = produce_left_diagonal(laser_space, direction)
    right_diagonal = produce_right_diagonal(laser_space, direction)

    #recall marbles are 3, outside spaces are 2, edge spaces are 1, available spaces are 0
    #we should only be dealing with an outside space or a marble or available space.

    left_row = left_diagonal[0]
    left_column = left_diagonal[1]

    right_row = right_diagonal[0]
    right_column = right_diagonal[1]


    if grid[left_row][left_column] == 3 and grid[right_row][right_column] == 3:
        print "both diagonals are occupied by a marble"
        diagonal = "both_marble"

    elif grid[right_row][right_column] == 3:
        print "right diagonal is occupied by a marble"
        diagonal = "right_marble"

    elif grid[left_row][left_column] == 3:
        print " left diagonal is occupied by a marble"
        diagonal = "left_marble"


    elif grid[left_row][left_column] == 1 and grid[right_row][right_column] == 1:
        print "both diagonals are outside spaces"
        diagonal = "both_outside"

    #The same result as outside spaces is also true for if the laser is moving through the outside spaces
    #Then it will hit the diagonals as an outside space and an edge space.

    elif grid[left_row][left_column] == 1 or grid[right_row][right_column] == 1:
        if grid[left_row][left_column] == 2 or grid[right_row][right_column] == 2:
            print "One diagonal is an outside space and the other is an edge."
            diagonal = "both_outside"
        elif grid[left_row][left_column] == 0 or grid[right_row][right_column] == 0:
            print "one is an outside space and one is unoccupied"
            diagonal = "both_empty"


    else:
        diagonal = "both_empty"        
        print "both are zeros"

        

    # elif grid[left_row][left_column] == 0 and grid[right_row][right_column] == 0:
    #     print "both diagonals are empty"
    #     diagonal = "both_empty"

    
    return diagonal






#this function will be used if only one of the diagonals is occupied by a marble:

def change_direction_one_marble(diagonals, direction):
    """uses whether it is left or right diagonal and the direction to change the direction of the laser"""

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
    """if both are outside spaces, this function will move the laser space forward two spaces"""


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
    """checks to see if there is a marble in a forward space"""

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
    """This will check to see if forward space is a marble or available space"""

    forward_row = forward_space[0]
    forward_column = forward_space[1]

    if grid[forward_row][forward_column] == 3:
        print "There's a marble in the forward space"
        forward_space = "marble"

    # elif grid[forward_row][forward_column] == 0:
    else:
        print "Theres nothing in the forward space"
        forward_space = "unoccupied"


    return forward_space


#This function will be used if there is a marble in a forward space or if both diagonals are occupied

def reflection(first_laser_space):
    """This function will make laser_space into the the original laser space"""

    final_laser_space = first_laser_space 


    return final_laser_space



#Putting the checking and moving actions together:

def checking_moving_loop(laser_space, first_laser_space, grid, direction):
    """This will loop through checking spaces and moving accordingly"""

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
    """asks the player if they would like to guess or send another beam"""

    print "Would you like to send another beam or guess where the mables are? "
    send_or_guess = raw_input("> ")
    send_or_guess = send_or_guess.lower()

    return send_or_guess



#this function will be used if they choose to guess the locations of the marbles

def guess_marble_locations(grid):
    """asks user where the guesses are and checks to see if there are marbles there"""

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

    if grid [first_marble_row][first_marble_column] != 3:
        num_incorrect_marbles += 1
    if grid[second_marble_row][second_marble_column]!= 3:
        num_incorrect_marbles += 1
    if grid[third_marble_row][third_marble_column] != 3:
        num_incorrect_marbles += 1

        
    return num_incorrect_marbles



#this function will be used if they guess incorrectly(if num_incorrect_marbles = 1,2,or 3)

def add_two(grid, player_total):
    """will add two times the number of incorrectly guessed marbles to the total"""

    num_incorrect_marbles = guess_marble_locations(grid)
    added_points = num_incorrect_marbles*2
    player_total = player_total + added_points


    return player_total




def game_over(player1_total, player2_total):
    """says game over, shows who won, then asks if you want to play again"""

    #add code, prints game over and shows who won

    return play_again




grid = set_up_grid()
greeting()
for row in grid:
    print row

grid = marble_placing_loop(grid)
for row in grid:
    print row



player_total = 0

while True:

    first_laser_space = laser_shooting_loop(grid)

    direction = return_first_direction(first_laser_space)
    print direction

    print "laser space = {}".format(first_laser_space)
    laser_space = move_one_space_forward(first_laser_space, direction)
    print "new laser_space = {}".format(laser_space)

    final_laser_space = checking_moving_loop(laser_space, first_laser_space, grid, direction)
    player_total += 1
    send_or_guess = guess_or_send()
    if send_or_guess == "guess":
        player_total = add_two(grid,player_total)
        print player_total
        break













