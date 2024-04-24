from typing import Callable

print('\033c')


#############################################
#     DECLARATIONS OF: GLOBAL VARIABLES     #
#############################################


messages = [
    'Enter the Integer needed as mentione above for the following execution',
    'Enter the needed String to operate without further hindrance',
    'Are you Human?',
    'What is the value of pi, a mathematical constant used to find the circumference, area and volume of sperical objects'
]

types = ['int', 'str', 'bool', 'float']

S = 'S'
O = 'O'
s = '$'
o = 'Ø'
empty = ' '



players = ['X', 'Y']

ver= 'v1.0'
Table = list[list[str]]
Coordinates = tuple[int, int]

input_infolength = 52

#############################################
#       GRAPHICS AND INPUT FUNCTIONS        #
#############################################


def display_menu(
        options: list|tuple, 
        title: str = '', 
        credit: str = '', 
        version:str = ver, 
        bottomborder: bool = True, 
        clear = False, 
        size:int = 20, 
        divider:int = 1
        ) -> None:

    '''Displays a Menu or Page in a fixed format that contains: Title, Options, Credit and version with:-
    - sections: options [required], title, credit, version
    - elements: size (page size), divider (space between sections)'''

    # alligned numbers for each option
    options = [f'[{idx}] {opt}' for idx, opt in enumerate(options, start=1)] if options != [] else ['']
    
    # longest string from all the elements
    longest_complete = (sorted([version + '   ' + credit] + [title] + options, key=len))[-1]

    # longest string in the options for center allignment
    longest_options = (sorted(options, key=len))[-1]

    # the minimum size that is needed to fit all the elements.
    min_display_width = len(longest_complete) + 2
    # the display page size, if less than the minimum display width, then modify.
    size = min_display_width if size < min_display_width else size

    # a design element used to divide different sections.
    true_divider = f'o{'':-^{size}}o'
    # a design element used to give space inside sections.
    sub_divider = '\n'.join([f'|{'': ^{size}}|'] * divider if divider > 0 else '')

    # The TITLE ELEMENT:
    Title = ''.join( #this\nthat\nthere + \n
        [
            true_divider  + '\n',
            f'|{title: ^{size}}|' + '\n', 
            true_divider + '\n'
        ]
    )
    
    # space needed before an option.
    space = f'|{longest_options: ^{size}}|'.find('[') - 1
    # calculate the length for correction.
    len_diff = len(" "*space)

    # The OPTIONS ELEMENT:
    Options = ''.join( #this\nthat\nthere + \n
        [
            sub_divider + '\n' if sub_divider != '' else sub_divider,
            ('\n'.join(
                [  # each option inside the list.
                    f'|{" " * space}{opt: <{size-len_diff}}|' for opt in options
                ]) + '\n'
            ),
            sub_divider + '\n' if sub_divider != '' else sub_divider
        ]
    )
    # The LAST ELEMENT:
    Last = ''.join( 
        [
            f'|  {version} {credit: >{size - len(version) - 5}}  |' + '\n',
            sub_divider,
            ''.join([('\n' + true_divider) if bottomborder else ''])
        ]
    )

    # Combine the Pieces.
    Display = Title + Options + Last
    # Display the page.
    print('\033c' + Display if clear else Display)


def get_input(
        display_func: Callable,
        argsforfunc: list|tuple,
        var_names: list|tuple,
        type_list: list|tuple,
        inside: list|tuple = [],
        size: int = 20
        ) -> list|tuple:

    '''Get's Input of specified variables with correct types in a fixed format of size:
    - function to start with (usually a display page: Must provide all arguments)
    - Args for the above function
    - Variable Names [list of strings]
    - Types [list of strings] (must be equal length as var_names)
    - Inside [list of types that must be in the input for specific inputs]
    - Size [int] (Format page size)'''


    func = False

    if display_func != None:
        try: 
            f_o, f_t, f_c, f_v, f_bb, f_cl, f_s, f_d = argsforfunc
            Dispfc = display_func
            func = True
            
        except ValueError:
            print('Not enough argumants for func to operate')
        



    # check if the provided type list has valid types.
    for types in type_list:
        if types not in ['int', 'str', 'bool', 'float']: return False, 'Undefined Types'

    # if the length of type list is less than return errors and warnings.
    if len(var_names) > len(type_list): return False, 'All the Types not specified'
    if len(type_list) > len(var_names): print('Warning, too many types!')

    # the result of getting input
    results: list = []

    # iterates through each variable and get's the right type of input.
    for idx, message in enumerate(var_names):
        # while the inputs are incorrect retry for input.
        while True:
            try:
                if func: Dispfc(f_o, f_t, f_c, f_v, f_bb, f_cl, f_s, f_d)
                match type_list[idx]:  # Check if type of the current variable is...
                    case 'int':  # then try to convert to int, if error try again, else break
                        out = int(input(inputformat('Integer', message, size)))
                        if inside == [None]:
                            break
                        elif out not in inside:  
                            raise ValueError()  # Raise a value error for an invalid input.
                        else:
                            break

                    case 'str':  # then try to convert to string, if empty try again, else break
                        out = str(input(inputformat('Words', message, size)))
                        if inside == [None]:
                            break
                        elif out == '' or out not in inside:  
                            raise ValueError()  # Raise a value error for an empty string or an invalid input.
                        else:
                            break

                    case 'bool':  # then try to convert to boolean, if error try again, else break
                        out = bool(input(inputformat('True/False', message, size)))
                        if inside == [None]:
                            break
                        elif out not in inside:  
                            raise ValueError()  # Raise a value error for an invalid input.
                        else:
                            break
                    
                    case 'float':  # then try to convert to float, if error try again, else break
                        out = float(input(inputformat('Decimal', message, size)))
                        if inside == [None]:
                            break
                        elif out not in inside:  
                            raise ValueError()  # Raise a value error for  an invalid input.
                        else:
                            break
            # try except if failing to convert to type, prompt Invalid Input and retry
            except ValueError:
                input(f'Invalid Input')
        # add the correct type of input into resultant variable.
        results.append(out)

    # Retrieve all the inputs.
    return results


def inputformat(input_hint: str, message: str, size = 20, centre: bool = False) -> str:

    '''Formats for input:
    - input hint
    - message to display
    - layout size
    - centre the text: T/F'''

    # declaring few variables for format calculations
    stringtoformat = message
    stringparts = []
    temp_sentence = ''

    # for every word in the sentence ...
    for word in stringtoformat.split(sep = ' '):

        # check if adding the word would result in the breaking of the page,
        # if not then add the word to the currrent string.
        if word == 'n':
            stringparts += [temp_sentence]
            temp_sentence = ''
        elif len(temp_sentence + word + ' ') < size - 2: temp_sentence += word + ' '
        else: 
            # if yes then append the current sentence to the list of strings.
            stringparts += [temp_sentence]
            # and start a new line. with the current word cycle.
            temp_sentence = word + ' '
    # attach the remaining string.
    else:
        stringparts += [temp_sentence]
    
    # Page formatting.
    page = '\n'.join(
        [
            f'o{'':-^{size}}o',
            '\n'.join(
                [
                    (f'| {strings: ^{size-2}} |' if centre else f'| {strings: <{size-2}} |') for strings in stringparts
                ]
            ),
            f'o{'':-^{size}}o',
            f'{input_hint} :: '
        ]
    )

    return page

def custom_size() -> Coordinates: # Your own table size!

    rows: int = get_input(
        display_menu, # type: ignore
        ([], 'Custom Size: Length (Min:3)', 'Positives Only', ver, False, True, 40, 1),
        [
            'Enter the size of choice:'
        ], ['int'], [None], 40
    )[0]

    rows = 3 if rows < 3 else rows

    cols: int = get_input(
        display_menu, # type: ignore
        ([], 'Custom Size: Height (Min:1)', 'Positives Only', ver, False, True, 40, 1),
        [
            'Enter the size of choice:' 
        ], ['int'], [None], 40
    )[0]

    cols = 1 if cols < 1 else cols

    return rows, cols

#############################################
#            MAINLOOP FUNCTIONS             #
#############################################

def main_menu() -> tuple[Coordinates, str]:

    choice: int = get_input(
        display_menu,
        (['Start', 'Exit'], 'Main Menu', 'By Plaxie', ver, False, True, 30, 1),
        [
            'Enter the option choice'
        ], ['int'], [1,2], 30   
    )[0]

    if choice == 2: exit()

    choice: int = get_input(
        display_menu,
        (['3x3', '4x4', '5x5', '10x10', 'Custom!'], 'Size', 'By Plaxie', ver, False, True, 30, 1),
        [
            'Enter the option choice'
        ], ['int'], [1,2,3,4,5], 30
    )[0]

    table_size = custom_size() if choice == 5 else [None, None]

    return [(3 ,3), (4 ,4), (5, 5), (10, 10), table_size][choice-1], \
           ['3x3', '4x4', '5x5', '10x10', f'{table_size[0]}x{table_size[1]}'][choice-1]


#############################################
#              LOGIC FUNCTIONS              #
#############################################

def valid_move(coords, size: Coordinates) -> bool:

    '''Checks if the given args are {valid for a table of size 3x3}:
    - Arguments of index position'''

    valid_row = range(size[0])  # Valid indexes (0, 1, 2, ...)
    valid_col = range(size[1])

    if coords[0] not in valid_row: return False
    if coords[1] not in valid_col: return False
    return True

def valid_position(row: int, column: int, table: Table) -> bool:

    '''Checks if the {position in the given place is empty}:
    - Row index
    - Column index
    - Table to check in'''
    
    if table[row][column] == empty:  # check if empty.
        return True # return True if empty.
    return False # else return False.

def interpretor(string: str, table_size: Coordinates) -> tuple[bool, str, str] | tuple[bool, Coordinates, str]:

    '''Interprets a given string of input to return the {correct format for input} using:
    - inputed string'''

    if string == '': return False, f"", ''

    coords_item:list = string.split()

    character:str = str(coords_item.pop())

    # if the number of coordinates is beyond 2 characters then return an error.
    if len(coords_item) != 2 or character not in ['S', 's', 'O', 'o']: return False, f"Move [{string}] is Invalid!", character

    try:  # try to make int ...
        row, column = int(coords_item[0]), int(coords_item[1])

    except ValueError:  # if not return an error.
        return False, f"Move [{coords_item[0]} {coords_item[1]} {character}] is Invalid!", character

    coordinates = (row, column)

    if valid_move(coordinates, table_size):  # check if it's a valid move to the size of the table.
        return True, (row, column), character # if valid then return in usable format.

    else:  # if not then return an error.
        return False, f"Move [{row} {column} {character}] is Invalid!", character


#############################################
#             DISPLAY FUNCTIONS             #
#############################################


def display_table(table: list[list], title: str = '', spacing: int = 8, clear:bool = False, padding:int = 0) -> None: 
    
    '''{Displays a Table} in a clean format: 
    - Table
    - Title (not required)
    - Clear: clears the terminal if set to [True]'''
    
    # Just string joins and list Comprehension Magic.
    print('\n'.join(['\033c' if clear else ''] + [f'' if title == '' else '\n'.join([f'{"": ^{padding}}o{"":-^{(spacing + 1) * len(table[0]) - 1}}o', f'{"": ^{padding}}|'+ f"{title: ^{(spacing + 1) * len(table[0]) - 1}}" +'|'])] + [f'{"": ^{padding}}' + ('o'+('-' * spacing)) * len(table[0]) + 'o'] + [''.join([f'{"": ^{padding}}'] + [f'|{f"{rdx: >{(spacing - 3) // 2}} {cdx: <{(spacing - 3) // 2}}" if row[cdx] == empty else f"{row[cdx]}": ^{spacing}}' for cdx in range(len(row)) ] + ['|\n' + f'{"": ^{padding}}' + ('o' + ('-' * spacing)) * len(table[0]) + 'o'])for rdx, row in enumerate(table)]))

#############################################
#              TABLE FUNCTIONS              #
#############################################
    
def create_empty_table(length:int, width:int) -> Table:

    return [[empty for cols in range(length)] for rows in range(width)]


def find_middle(table_size:int, find_middle_of:int, spacing: int) -> int:
    global input_infolength

    total_length = table_size*(spacing+1)

    mid = find_middle_of-total_length

    if mid > 1: return (mid//2)

    else: 
        input_infolength = total_length-1
        return 0


def find_space(rows:int, cols:int) -> int:
    rows = len(f'{rows}')
    cols = len(f'{cols}')

    return ((rows if rows > cols else cols)*2)+3


def place(table: Table, move: Coordinates, character:str) -> Table:
    table[move[0]][move[1]] = character.upper()
    return table


################################
#       CHECK FUNCTIONS        #
################################


def HORIZONTALS(table: Table) -> list[str]:

    '''Gets all possible horizontal lines in the table'''

    result = []

    for row in table:
        result.append(''.join(row))

    return result

    
def VERTICALS(table: Table) -> list[str]:

    '''Gets all possible vertical lines in the table'''

    result = []
    cols = len(table[0])
    onecol = []

    for idx in range(cols):

        for row in table:
            onecol.append(row[idx])

        result.append(''.join(onecol))
        onecol = []
        
    return result    


def RCROSS(table: Table) -> list[str]:
    
    '''Gets the cross in the table'''

    result = []
    
    # Calculate number of rows and columns
    rows = len(table)
    cols = len(table[0])

    # Iterate over each diagonal starting from the top-right corner
    for i in range(cols):
        word = ''
        row = 0
        col = i
        while row < rows and col >= 0:
            word += table[row][col]
            row += 1
            col -= 1
        result.append(word)

    # Iterate over each diagonal starting from the top-left corner (excluding the main diagonal)
    for i in range(1, rows):
        word = ''
        row = i
        col = cols - 1
        while row < rows and col >= 0:
            word += table[row][col]
            row += 1
            col -= 1
        result.append(word)

    return sorted(result, key=len)[2:]


def LCROSS(table: Table) -> list[str]:
    
    '''Gets the cross in the table'''

    result = []
    
    # Calculate number of rows and columns
    rows = len(table)
    cols = len(table[0])

    # Iterate over each diagonal starting from the top-right corner
    for i in range(cols - 1, -1, -1):
        word = ''
        row = 0
        col = i
        while row < rows and col >= 0:
            word += table[row][col]
            row += 1
            col -= 1
        result.append(word)

    # Iterate over each diagonal starting from the top-left corner (excluding the main diagonal)
    for i in range(1, rows):
        word = ''
        row = i
        col = cols - 1
        while row < rows and col >= 0:
            word += table[row][col]
            row += 1
            col -= 1
        result.append(word)

    return sorted(result, key=len)[2:]



def checkfor_sos(table: Table) -> tuple[bool, tuple[tuple[str, Coordinates], tuple[str, Coordinates], tuple[str, Coordinates]] | None]: # type: ignore

    # Horizontal Check
    data = HORIZONTALS(table)

    for idx, line in enumerate(data):
        match_ = line.find('SOS')
        if match_ != -1: 
            return True, ((s, (match_, idx)), (o, (match_, idx + 1)), (s, (match_, idx + 2)))
    
    # Vertical Check

    data = VERTICALS(table)

    for idx, line in enumerate(data):
        match_ = line.find('SOS')
        if match_ != -1: 
            return True, ((s, (match_, idx)), (o, (match_, idx + 1)), (s, (match_, idx + 2)))
    
    # Right Across Check # LATER

    # Left Across Check # LATER

    return False, None

if __name__ == '__main__':

    # Main game loop
    while True:

        turn = False

        input_infolength = 52

        # get the size for the table from main menu.
        size, label = main_menu()  # tuple[size:int,int, size_label:str]

        space = find_space(size[0], size[1])
        points = [0, 0]


        # create two empty tables of selected size.
        table = create_empty_table(size[0], size[1])  # what the player can see
        # point_table = create_empty_table(size[0], size[1])  # what the point logic sees 

        padding_table = find_middle(size[0], input_infolength, space)
        print('\033c')


        while True:
            # display current table.
            print(f'Player X: {points[0]} | Player Y: {points[1]}\n')

            display_table(table, f'SOS : {label} Table', space, False, padding_table)

            # input for Player X:
            valid, move, character = interpretor(input(inputformat('Double-Integer-String : "0 0 X"',
                                        f'Player [{players[turn]}]: Select Position to drop your letter',
                                        input_infolength, True)), size)
            
            if valid: 
                if valid_position(move[0], move[1], table): # type: ignore
                    table = place(table, move, character) # type: ignore
                    turn = not turn
                else: 
                    input(f"Move [{move[0]} {move[1]} {character}] is Invalid!")
            else: input(move)

            check = checkfor_sos(table)
            if check[0]:
                for coords in check[1]: # type: ignore
                    place(table, (coords[1]), coords[0])
                input(f"Player {players[not turn]} get's a point")
                points[not turn] += 1
            print('\033c')



