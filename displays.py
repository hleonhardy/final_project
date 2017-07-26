#******************************************************************************#
#                             MARBLE DISPLAY
#******************************************************************************#



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
#                               LASER DISPLAY
#******************************************************************************#

#Laser space displays!!

def laser_display(in_laser, out_laser, laser_or_demo):

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




    if laser_or_demo == "laser":

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












