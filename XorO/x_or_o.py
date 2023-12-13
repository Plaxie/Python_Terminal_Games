from random import randint as rdi
Table = list[list[str]]


def display_table(table:Table) -> None:
    
    '''{Displays a Table} in a clean format:
    - Table'''
    

    print(f'\no-----o-----o-----o\
            \n| {"0 0" if table[0][0] == empty else f" {table[0][0]} "} | {"0 1" if table[0][1] == empty else f" {table[0][1]} "} | {"0 2" if table[0][2] == empty else f" {table[0][2]} "} |\
            \n| {"1 0" if table[1][0] == empty else f" {table[1][0]} "} | {"1 1" if table[1][1] == empty else f" {table[1][1]} "} | {"1 2" if table[1][2] == empty else f" {table[1][2]} "} |\
            \n| {"2 0" if table[2][0] == empty else f" {table[2][0]} "} | {"2 1" if table[2][1] == empty else f" {table[2][1]} "} | {"2 2" if table[2][2] == empty else f" {table[2][2]} "} |\
            \no-----o-----o-----o\
          ')  # Last part.


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

    data = HORIZONTALS(table) + VERTICALS(table) + CROSS(table)

    for line in data:
        value = determine_value(line)
        if value in [264, 237]:
            return True
    return False


def HORIZONTALS(table:Table) -> list[str]:

    result = []
    for row in table:
        result.append(''.join(row))
    return result
    
def VERTICALS(table:Table) -> list[str]:

    result = []
    for idx in range(3):
        result.append(table[0][idx]+table[1][idx]+table[2][idx])
    return result
    

def CROSS(table:Table) -> list[str]:
    return [table[0][0] + table[1][1] + table[2][2], \
        table[0][2] + table[1][1] + table[2][0]]


def determine_value(string:str) -> int:
    result = 0
    for char in string: result += ord(char)
    return result


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
        exit()
    
    return turn  # return the current starting turn for the game to begin

if __name__ == '__main__':  # Main Run

    # Game Variables
    X, O, empty = 'X', 'O', ' '


    # Players X and O assigned to turns 1 and 0
    positions = [O, X]


    while True:  # main game loop

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

        turn = main_menu()  # gets the starting turn of the player 1.
        input(
            "\033cINSTRUCTIONS:\
             \nInput your position to place \
             \nas in index 00 or 13 where 1 \
             \nis the row number and 3 is the\
             \ncolumn number.\
           \n\nAny mistakes cannot be undone.\
           \n\nYou can type at any time: \
             \nQUIT: exits the game. \
             \nMENU: returns to main menu.\
           \n\nPress Enter to continue :: "
           )
        while True:
            print('\033c')
            display_table(table)
            
            user_input = input(f"it's {positions[turn]}'s turn :: ")

            interpretted = interpretor(user_input)
            if interpretted[0] == True:
                table_data = placer(turn, interpretted[1], table)

                if table_data[0] == False:
                    input(f"There is no empty space on {interpretted[1]} :: ")
                else:
                    table = table_data[1]
                    if checkfortriples(table):
                        print('\033c')
                        display_table(table)
                        input(f"\n{positions[turn]} has won the Game!")
                        break
                    turn = not turn
                    
                
            else:
                input(interpretted[1])
        usrinp = input(f"Do you want to [QUIT] or continue :: ").lower()
        if usrinp == 'quit':exit()






    
