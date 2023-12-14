from random import randint  # For randomization.
from itertools import chain # in order to flatten a table.

def flatten(array):  # flattening a list.
    
    '''{Flattens any array} needs:
    - Array'''
    
    return list(chain.from_iterable(array))

################################
#      DISPLAY  FUNCTIONS      #
################################


def display_table(table: list[list]) -> None: 
    
    '''{Displays a Table} in a clean format:
    - Table'''
    
    for row in table:  # Iterate through each Row.
        
        for item in row:  # Iterate through each Item.
            if item != 0:
                print(f"| {item: ^3} ", end = '')  # The Format.
            else:
                print(f"|#####", end = '')
            
        print('|', end = '\n')  # Last part.


################################
#       TABLE FUNCTIONS        #
################################


def random_table(size: int) -> list[list]:
    
    '''Provides a {Random Table} with: 
    - Table Size'''
    
    digits: list[int] = [*range(size*size)]  # a list of valid numbers.
    
    # Retrieve the Randomized Table.
    return [[digits.pop(randint(0,len(digits)-1)) for i in range(size)] for j in range(size)]
    

def turned_table(table: list[list], turns: int= 20) -> list[list]:
    
    '''Provides a {Juggled Table} from Win configuration with:
    - Table Size 
    - Number of Turns'''
    
    # Increases turns to match board size difficulty.
    turns = turns * len(table)*len(table)
    
    #  Create a list of valid numbers to possibly move.
    random_nums = [randint(1, (len(table)*len(table)-1)) for a in range(turns)]
    
    # Try to turn a number from the random list of valid numbers.
    for num in random_nums:
        table = nums_mover([num], table) # Method used to move numbers.
    
    return table # Return the Turned Table.


def winconfig(size: int) -> list[list]:
    
    '''Provides a {Winning Condition Table} with:
    - Table Size'''
    
    digits: list[int] = [*range(size*size)][1:] + [0] # The default arrangement.
    
    # Retrieve the Win Condition Table.
    return [[digits.pop(0) for i in range(size)] for j in range(size)]
    

################################
#     MODIFYING FUNCTIONS      #
################################
 
def move(table: list[list], from_index: list | tuple, to_index: list | tuple) -> list[list]:
    
    '''A Swapper Function that {Swaps an Item} from {An index with Another} needs:
    - Table to Swap in
    - From Index
    - To Index'''
    
    # From this Index To the next index, just swap.
    table[from_index[0]][from_index[1]], table[to_index[0]][to_index[1]] = \
    table[to_index[0]][to_index[1]], table[from_index[0]][from_index[1]]
    
    # Retrive the Modified Table.
    return table


################################
#       SOLVE FUNCTIONS        #
################################

def item_finder(item, table: list[list]):
    
    '''Gives the {index of the row number and item number} with:
    - The Item or Number
    - The Table to search in'''
    
    for row_index, row in enumerate(table):  # Iterate through the rows.
        
        if item in row:  # check if the item's in there.
    
            for item_index, _item in enumerate(row):  # Iterate through the items in the row.
                
                if item == _item:  # If match, the nreturn the row and item indexes.
                    return row_index, item_index
                
    else:  # Or Else return a Default False.
        return False, False


def check_empty(index: tuple[int], table: list[list]) -> tuple[tuple,bool]:
    
    '''Checks for an {Empty Spot: 0} around the index in the Table provided:
    - Index to search around
    - Table to search inside'''
    
    row_index, item_index = index  # just setting their own vars to work with.
    
    size = len(table)  # keep the length in check for remembering the borders of the table.
    
    
    # checks if the right of the item has an empty spot.
    if item_index != size-1: 
        if 0 == table[row_index][abs(item_index+1)]:
            return (row_index, abs(item_index+1)), True
        
    # checks if the left of the item has an empty spot.   
    if item_index != 0:
        if 0 == table[row_index][abs(item_index-1)]:
            return (row_index, abs(item_index-1)), True
    
    # checks if the row above the item has an empty spot.
    if row_index != size-1:
        if 0 == table[(row_index+1)][item_index]:
            return (row_index+1, item_index), True
            
    # checks if the row below the item has an empty spot.
    if row_index != 0:
        if 0 == table[(row_index-1)][item_index]:
            return (row_index-1, item_index), True
    
    # return a Default False if there are no empty spot.
    return (None, None), False
            
            

################################
#       SOLVER FUNCTION        #
################################

def main_menu() -> tuple[tuple[int, str]]:
    
    '''A Main Menu function to get the {inputs of difficulty and size} of the board.'''
    
    while True:  # For invalid input.
        choice = input(

'''\033c
Solving Sequence [MENU]
        
1. Start
2. Exit       By PLAXIE

Enter Option >> '''

        )  # Display Menu panel
        
        if choice in tuple('12'):  # if choice is valid.
            break
        else:
            input('Wrong Value ::')  # else prompt invalid.
    
    if choice == '1':  # if choice is Start.
        size_choice = input(

'''\033c
Solving Sequence [SIZE]

1. 3x3   [ Easy  ]
2. 5x5   [ Normal]
3. 10x10 [ Hard  ]
4. 15x15 [Extreme]
5. 30x30 [Madness]

![Madness] May not
render properly...

Enter Option >> '''

        ) # Display Size Difficulty Panel.
        
        if size_choice in tuple('12345'):  # if size choice is valid.
            size_choice = int(size_choice) - 1  # Correct the index.
            
            # Set the difficulty accordingly for later usage.
            size_, size_text = difficulty(1, size_choice)  
            
            input(f'Setting Size to {size_text}, Press Enter to continue ::')  # Prompt.
                
        else:  # or if they mis-type.
            size_choice = 1  # Set to default 1: Normal Size.
            size_, size_text = difficulty(1, size_choice)   # Set Accordingly.
            
            # Prompt the default and continue.
            input(f'Wrong Value, Setting Size to {size_text}, Press Enter to continue ::')   

        diff_choice = input(
            
'''\033c
Solving Sequence [TURNS]

1. 30     [  Easy  ]
2. 100    [ Normal ]
3. 300    [  Hard  ]
4. 900    [Extreme ]
5. 2000   [Madness ]
6. Random [Possible]

# These are Proportional
# To Board Sizing.

![Madness] Might
take a while ...

Enter Option >> '''

        )  # Display the Turns Difficulty Panel.
        
        if diff_choice in tuple('123456'):  # if the difficulty choice is valid.
            diff_choice = int(diff_choice) - 1  # Correct the index.
            
            # Set the difficulty accordingly for later usage.
            diff_, diff_text = difficulty(2, diff_choice)
            
            input(f'Setting turns to {diff_text}, Press Enter to continue ::') # Prompt.
            
        else:  # or if they mis-type.
            diff_choice = 1  # Set to default 1: Normal Turns.
            diff_, diff_text = difficulty(2, diff_choice)  # Set Accordingly.
            
            # Prompt the default and continue.
            input(f'Wrong Value, Setting turns to {diff_text}, Press Enter to continue ::')  
            
    else: # if the user chose to Exit.
        exit()
    
    return (size_, size_text), (diff_, diff_text) # Retrieve the difficulty settings.
    
    
def difficulty(type_:int, index: int) -> tuple[int,str]:
    
    '''Provides the {difficulty for the set option}
    - if size type or turn type: 0 or 1
    - the option index.'''
    
    if type_ == 1:  # If it's Size
        return [3, 5, 10, 15, 30][index], \
            ['Easy', 'Normal', 'Hard', 'Extreme', 'Madness'][index]
            
    else: # If it's Turns Difficulty
        return [30, 100, 300, 900, 2000, 0][index], \
            ['Easy', 'Normal', 'Hard', 'Extreme', 'Madness', 'Possible'][index]


def multiply(numstring: str) -> str:
    
    '''A sub function for get_input() to add multiplication to input:
    - the string to multiply'''

    result = ''  # nums before the '*'.
    multiplier = ''  # nums after the '*'.
    
    flag = False  # indicator that char has hit '*'.
    
    for char in numstring:  # iterating through each char of the numstring.
        
        # if the char is not '*' and has not hit a '*'.
        if char != '*' and flag == False:  
            # then add the char to result.
            result += char

        # if the char is '*' then set flag to True, which means it has hit '*'.
        elif char == '*': flag = True

        # after flag = True, only add numericals to multiplier.
        else:
            if char.isnumeric():
                multiplier += char
        
    # result the multiplied string.
    return result * int(multiplier)
       

def get_input(table: list[list], size: str, diff: str) -> list[int]:
    
    '''Gets the {input as a string of seperated integers} and returns a list of nums:
    - The Table to know only possible nums and display the table.
    - Size Name.
    - Difficulty Name.'''
    
    possibles = flatten(table)  # list of possible items.
    des_len = 6*len(table)-1
    des_char = '-'*des_len
    
    # Display the table.
    print(f'\033cSize [{size}]: Difficulty [{diff}]: Table:\n')
    
    print(f'o{des_char}o')
    display_table(table)
    print(f'o{des_char}o')
    
    move_nums = input("\nEnter the number(s) you want to move: ")  
    
    if move_nums.lower() == 'quit':  # if the user decides to quit.
        exit()
    elif move_nums.lower() == 'menu':
        return 'MENU'
        
    if '*' in move_nums:
        move_nums = multiply(move_nums)

    
    while True:  # While the turns are not valid get correct input.
        
        nums = list(move_nums.split(sep=' '))  # split to a list of integer items.
        nums_list = []  # Valid numbers.
        
        for num in nums:  # iterate through the inputed numbers.
            
            try:  # Try to convert to int type and add to valid.
                num = int(num)  
                if num in possibles:  # if the integer is in the valid items
                    nums_list.append(num)  # add it to the Valid list of items.
            
            # catch any Value errors for failing to convert to int.
            except ValueError: pass 
        
        # If there are valid items then, get out of the loop.
        if len(nums_list) != 0:
            break
        
        # Or if there are None, then prompt the user for their failed input.
        else:  # and continue the loop.
            
            # Display the table.
            print(f'\033cSize [{size}]: Difficulty [{diff}]: Table:\n')
            
            print(f'o{des_char}o')
            display_table(table)
            print(f'o{des_char}o')
            
            # Ask for re-input.
            move_nums = input("\nError: Correctly enter the number(s) you want to move: ")
            
            if move_nums.lower() == 'quit':  # if the user decides to quit.
                exit()
            elif move_nums.lower() == 'menu':
                return 'MENU'
    
    return nums_list # Retrieve the valid integers.
        
            
def nums_mover(nums: list[int], table: list[list]) -> list[list]:
    
    '''Moves a number from a list of numbers on a table:
    - A Sequence of Numbers, Invalid ones will be rejected.
    - The Table to move in'''
    
    for num in nums:  # Iterate through each number.
        
        # get the row and index of the number.
        row_idx, item_idx = item_finder(num, table)
        
        # combine in a tuple.
        num_pos = row_idx, item_idx
        
        # pass it to the checker to find valid empty spot with the table.
        zero_pos, flag = check_empty(num_pos, table)
        
        # if it finds an empty spot, then move it over.
        if flag:
            table = move(table, num_pos, zero_pos)

        # else break off of the whole remainder of items
        # to save proccessing of invalid moves.
        else:break
    
    return table  # Retrieve the modified table.
    
    

if __name__ == "__main__":
        
    while True: # The Game Loop.
        
        ####################
        #    MAIN  MENU    #
        ####################
        
        # returns table size, it's name, the table turns number and the difficulty name.
        size_p, diff_p = main_menu() 
        
        # winning condition of a table.
        win_Table = winconfig(size_p[0])
        
        if diff_p[0] == 0:  # if Random board chosen.
            Table = random_table(size_p[0])

        else:  # if Set turns chosen.
            Table = turned_table(winconfig(size_p[0]), diff_p[0])

        ####################
        #   INSTRUCTIONS   #
        ####################

        # Display the One time Winning state and Current State.
        des_len:int = (6*len(win_Table))-1
        des_char = '-'*des_len
        
        win = 'Winning_State'
        print('\033c')
    
        print(f'o{win:-^{des_len}}o')
        display_table(win_Table)
        print(f'o{des_char}o')
        
        input('\nINSTRUCTIONS: You can type: 5 7 15 1           \
                \nTo move all those numbers together.           \
                \nIf the move is valid.                         \
                \n\nYou can also multiply like: 1 2 * 3         \
                \nWhich is intepreted as: 1 2 1 2 1 2           \
                \n\nHint only shown once every game.            \
                \nAlso type "quit" to exit                      \
                \nAnd type "menu" to return to main menu.       \
                \n\nPress Enter to continue.'
            )
        
        ####################
        #   SOLVE   GAME   #
        ####################
        
        # Get Input - Solve the puzzle.
        while True:  # While the user is still playing.
        
            nums = get_input(Table, size_p[1], diff_p[1])  # Get the input.
            if nums == 'MENU':
                break

            Table = nums_mover(nums, Table)  # Move the moves

            if Table == win_Table:  # If the Table is in win condition state.
                
                # Prompt That the user Won.
                print("\nYou Solved it!")
                break
        
        # Ask if they want to Re-play.
        if nums == 'MENU' or input('Press Enter to Return to Main Menu or type anything to leave :: ') == '': 
            pass
        else: break
        
    
    
    

        
    
    
    
        
    