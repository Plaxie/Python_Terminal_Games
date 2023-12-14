Table = list[list[str]]


################################
#      DISPLAY  FUNCTIONS      #
################################


def display_table(table:Table) -> None:
    
    '''{Displays a Table} in a clean format:
    - Table'''
    
    # Just string joins and list Comprehension Magic.
    print(''.join(['o-----'*len(table)+'o\n'] + [''.join([f'| {rdx} {cdx} ' if row[cdx] == empty else f'|  {row[cdx]}  ' for cdx in range(len(row)) ] + ['|\n'+'o-----'*len(table)+'o\n'])for rdx, row in enumerate(table)]))
    

################################
#     INPUT FIXED FUNCTION     #
################################


def interpretor(string: str) -> tuple[bool, str | tuple[int]]:

    '''Interprets a given string of input to return the {correct format for input} using:
    - inputed string'''

    string = "".join(string.split())  # Removes any spaces if given.

    # if the len of the string is beyond 2 characters then return an error.
    if len(string) != 2: return False, f"Move [{string}] is Invalid!"   

    try:  # try to make int ...
        row, column = int(string[0]), int(string[1])

    except ValueError:  # if not return an error.
        return False, f"Move [{string[0]}][{string[1]}] are Invalid!"

    if valid_move(row, column):  # check if it's a valid move to the size of the 3x3 table.
        return True, (row, column) # if valid then return in usable format.

    else:  # if not then return an error.
        return False, f"Move [{row}][{column}] are Invalid!"


################################
#       TABLE FUNCTIONS        #
################################


def placer(current_turn: bool, coords: tuple[int], table: Table) -> tuple[bool, Table]:

    '''{Places the current turn's selected position} on the table:
    - Current turn set in the beginning [0,1]
    - Coordinates of the position
    - Table the game's running on'''

    character = positions[current_turn]  # turn's character.
    ro, co = coords  # set coordinates to rows and columns variable.
    
    if valid_position(ro, co, table):  # if the selected position is valid.

        table[ro][co] = character  # then place the turn's character
        return True, table  #  And return the modified Table with no errors.

    else:  # return the unmodified table with False as error indicator.
        return False, table


################################
#       LOGIC FUNCTIONS        #
################################


def valid_move(*args) -> bool:

    '''Checks if the given args are {valid for a table of size 3x3}:
    - Arguments of index position'''

    valid = range(3)  # Valid indexes (0,1,2)

    for move in args:  # check each argument.
        if move not in valid:  # if not valid then return False.
            return False
    else:  # if all are valid then return True.
        return True


def valid_position(row: int, column: int, table: Table) -> bool:

    '''Checks if the {position in the given place is empty}:
    - Row index
    - Column index
    - Table to check in'''
    
    if table[row][column] == empty:  # check if empty.
        return True # return True if empty.
    return False # else return False.


def checkfortriples(table:Table) -> bool:

    '''Checks if X or O has done any triples.
    - Table to check in'''

    # Collects every possible triple config.
    data = HORIZONTALS(table) + VERTICALS(table) + CROSS(table)

    # Checks if any line is 'XXX' or 'OOO'
    for line in data:
        if line in ['XXX', 'OOO']:
            return True
    # return False if not
    return False


################################
#       CHECK FUNCTIONS        #
################################


def HORIZONTALS(table:Table) -> list[str]:

    '''Gets all possible horizontal lines in a 3x3'''

    result = []
    for row in table:
        result.append(''.join(row))
    return result
    
def VERTICALS(table:Table) -> list[str]:

    '''Gets all possible vertical lines in a 3x3'''

    result = []
    for idx in range(3):
        result.append(table[0][idx]+table[1][idx]+table[2][idx])
    return result
    

def CROSS(table:Table) -> list[str]:
    
    '''Gets the cross in a 3x3'''

    return [table[0][0] + table[1][1] + table[2][2], \
        table[0][2] + table[1][1] + table[2][0]]



################################
#       MAIN MENU INPUT        #
################################


def main_menu() -> bool:

    '''Main Menu of the Game that returns the {starting turn}:'''

    while True:  # Until the user takes the right option
        # show them this string
        choice = input(  
            "\033co===---[X or O]---===o\
                \n|                    |\
                \n|      1. Start      |\
                \n|      2. Exit       |\
                \n|                    |\
                \no=======------=======o\
                \n      Input :: "
            )
        # if cchoice is valid: break of the loop.
        if choice in list('12'): break

        # else prompt the user being incorrect.
        else: input('Incorrect Option! :: ')

    # if Start:
    if choice == '1':
        turn = input(
            "\033co==--[Start with]--==o\
                \n|                    |\
                \n|        1. X        |\
                \n|        2. O        |\
                \n|                    |\
                \no=======------=======o\
                \n      Input :: "
            )
        if turn in list('12'):
            turn = bool(abs(int(turn) - 2))
        else: 
            input('Invalid Choice! Defaulting to X :: ')
            turn = True
    # else exit for option 2
    else:
        exit('\033c\no========-----========o\n| Hope you had fun :> |\no========-----========o\n\n')
    
    return turn  # return the current starting turn for the game to begin


################################
#       RUN STARTS HERE        #
################################


if __name__ == '__main__':  # Main Run

    # Game Variables
    X, O, empty = 'X', 'O', ' '


    # Players X and O assigned to turns 1 and 0
    positions = [O, X]

    ####################
    #    GAME  LOOP    #
    ####################

    while True:  

        # Table layout by default every game
        table = [
            [
                empty, empty, empty
            ],
            [
                empty, empty, empty
            ],
            [
                empty, empty, empty
            ]
        ]
        
        ####################
        #    MAIN  MENU    #
        ####################

        turn = main_menu()  # gets the starting turn of the player.

        ####################
        #   INSTRUCTIONS   #
        ####################

        # Prompt Instructions of the game.
        input(
            "\033cINSTRUCTIONS:\
             \nInput your position to place \
             \nas in index 00 or 12 where 1 \
             \nis the row number and 2 is the\
             \ncolumn number.\
           \n\nAny mistakes cannot be undone.\
           \n\nYou can type at any time: \
             \nQUIT: exits the game. \
             \nMENU: returns to main menu.\
           \n\nPress Enter to continue :: "
           )
        
        ####################
        #    GAME START    #
        ####################

        while True:

            # Display the table.
            print('\033c')
            display_table(table)
            
            # Get user input.
            user_input = input(f"it's {positions[turn]}'s turn :: ")

            match user_input.lower():
                case 'quit': exit('\033c\no========-----========o\n| Hope you had fun :> |\no========-----========o\n\n')
                case 'menu': break

            # Get input to usable format: Boolean, error or coordinates.
            interpretted = interpretor(user_input)

            # if input is correct, then try placing the given coords on the table.
            if interpretted[0] == True:
                table_data = placer(turn, interpretted[1], table)

                # if there's no space ie False is returned for first item.
                if table_data[0] == False:
                    input(f"There is no empty space on {interpretted[1]} :: ")
                # else if there is free space.
                else:

                    # Overwrite current table with modified table.
                    table = table_data[1]

                    # Check if anyone Won.
                    if checkfortriples(table):

                        # if won then display for the last move and prompt win.
                        print('\033c')
                        display_table(table)
                        input(f"\n{positions[turn]} has won the Game!")
                        break  # leave the start loop.

                    # swtich turn.
                    turn = not turn
                    
            else:  # show error for poor input.
                input(interpretted[1])
        
        # Prompt user if they want to leave or continue.
        if user_input.lower() != 'menu':
            usrinp = input(f"Do you want to [QUIT] or continue :: ").lower()
            if usrinp == 'quit':exit('\033c\no========-----========o\n| Hope you had fun :> |\no========-----========o\n\n')






    
