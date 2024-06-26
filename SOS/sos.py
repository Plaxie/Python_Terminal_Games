
print('\033c')


#############################################
#     DECLARATIONS OF: GLOBAL VARIABLES     #
#############################################


messages = [
    'Enter the Integer needed as mentioned above for the following execution',
    'Enter the needed String to operate without further hindrance',
    'Are you Human?',
    'What is the value of pi, a mathematical constant used to find the circumference, area and volume of sperical objects'
]

types = ['int', 'str', 'bool', 'float']

S = 'S'
O = 'O'
s = '$'
o = 'ɸ'
empty = ' '

players = ['X', 'Y']

possible_matches = [f'{S+O+S}', f'{s+O+s}', f'{S+o+S}', f'{s+O+S}', f'{S+O+s}', f'{S+o+s}', f'{s+o+S}']

ver= 'v1.0'

Table = list[list[str]]
Coordinates = tuple[int, int]
Coordinated_Data = tuple[str, Coordinates]
Match_Data = list[Coordinated_Data]

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
        display_func, # a callable object
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


def display_table(table: list[list], title: str = '', spacing: int = 0, clear:bool = False, padding:int = 0) -> None: 
    
    '''{Displays a Table} in a clean format: 
    - Table
    - Title (not required, can be set to '')
    - Spacing (not required, can be set to 0)
    - Clear: clears the terminal if set to [True]
    - Padding for the Table from the left side'''
    
    # Just string joins and list Comprehension Magic.
    print('\n'.join(['\033c' if clear else ''] + [f'' if title == '' else '\n'.join([f'{"": ^{padding}}o{"":-^{((spacing if spacing != 0 else (((len(f'{len(table)}') if len(f'{len(table)}') > len(f'{len(table[0])}') else len(f'{len(table[0])}')) * 2) + 3)) + 1) * len(table[0]) - 1}}o', f'{"": ^{padding}}|'+ f"{title: ^{((spacing if spacing != 0 else (((len(f'{len(table)}') if len(f'{len(table)}') > len(f'{len(table[0])}') else len(f'{len(table[0])}')) * 2) + 3)) + 1) * len(table[0]) - 1}}" +'|'])] + [f'{"": ^{padding}}' + ('o'+('-' * (spacing if spacing != 0 else (((len(f'{len(table)}') if len(f'{len(table)}') > len(f'{len(table[0])}') else len(f'{len(table[0])}')) * 2) + 3)))) * len(table[0]) + 'o'] + [''.join([f'{"": ^{padding}}'] + [f'|{f"{rdx: >{((spacing if spacing != 0 else (((len(f'{len(table)}') if len(f'{len(table)}') > len(f'{len(table[0])}') else len(f'{len(table[0])}')) * 2) + 3)) - 3) // 2}} {cdx: <{((spacing if spacing != 0 else (((len(f'{len(table)}') if len(f'{len(table)}') > len(f'{len(table[0])}') else len(f'{len(table[0])}')) * 2) + 3)) - 3) // 2}}" if row[cdx] == empty else f"{row[cdx]}": ^{(spacing if spacing != 0 else (((len(f'{len(table)}') if len(f'{len(table)}') > len(f'{len(table[0])}') else len(f'{len(table[0])}')) * 2) + 3))}}' for cdx in range(len(row)) ] + ['|\n' + f'{"": ^{padding}}' + ('o' + ('-' * (spacing if spacing != 0 else (((len(f'{len(table)}') if len(f'{len(table)}') > len(f'{len(table[0])}') else len(f'{len(table[0])}')) * 2) + 3)))) * len(table[0]) + 'o'])for rdx, row in enumerate(table)]))

#############################################
#              TABLE FUNCTIONS              #
#############################################
    
def create_empty_table(length:int, width:int) -> Table:

    '''{Creates an empty table} where empty = ' '
    - length of the table
    - width of the table
    '''

    return [[empty for cols in range(length)] for rows in range(width)]


def find_middle(table_size:int, find_middle_of:int, spacing: int) -> int:

    '''Finds the middle of a line copared to a table.
    - number of columns the table has
    - the line of which you want to find the middle of
    - defined spacing
    '''

    # The input field length 
    global input_infolength

    # actual length of the table size with columns
    total_length = table_size*(spacing+1)

    
    mid = find_middle_of-total_length

    if mid > 1: return (mid//2)

    else: 
        # match the input length with the table length
        input_infolength = total_length-1
        return 0


def find_space(rows:int, cols:int) -> int:

    '''Finds the space needed for a column to fit the indices
    - number of rows of the table
    - number of columns in the table
    '''

    return ((len(f'{rows}') if len(f'{rows}') > len(f'{cols}') else len(f'{cols}')) * 2) + 3


def place(table: Table, move: Coordinates, character:str) -> Table:

    '''Places a character on a table with select coordinates'''

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


def RCROSS(table: Table) -> list[Coordinated_Data]:
    
    '''Gets the cross in the table'''

    if len(table) < 3 or len(table[0]) < 3: return []

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
        result.append((word, (col + 1, row - 1)))

    # Iterate over each diagonal starting from the top-left corner (excluding the main diagonal)
    for i in range(1, rows):
        word = ''
        row = i
        col = cols - 1
        while row < rows and col >= 0:
            word += table[row][col]
            row += 1
            col -= 1
        result.append((word, (col + 1, row - 1)))

    return result[2:-2] if len(result) > 3 else result[1]

def LCROSS(table: Table) -> list[Coordinated_Data]:
    
    '''Gets the cross in the table'''

    if len(table) < 3 or len(table[0]) < 3: return []

    diagonals = []
    num_rows = len(table)
    num_cols = len(table[0])

    # Iterate over each starting position in the first column
    for i in range(num_rows):
        row, col = i, 0
        diagonal = []
        while row < num_rows and col < num_cols:
            diagonal.append(table[row][col])
            row += 1
            col += 1
        diagonals.append((''.join(diagonal), (row - 1, col- 1)))

    # Iterate over each starting position in the first row (excluding the first element which has already been visited)
    for j in range(1, num_cols):
        row, col = 0, j
        diagonal = []
        while row < num_rows and col < num_cols:
            diagonal.append(table[row][col])
            row += 1
            col += 1
        diagonals.append((''.join(diagonal), (row - 1, col- 1)))

    return diagonals


def checkfor_sos(table: Table) -> Match_Data:

    # MAX points at a time is EIGHT!!!
    matches_found = []

    # Check DATA

    H_data = HORIZONTALS(table)   
    V_data = VERTICALS(table)
    Rcross_data = RCROSS(table)
    Lcross_data = LCROSS(table)

    # Horizontal Check

    for idx, line in enumerate(H_data):

        # check if the board has any point matches
        for win_match in possible_matches:
            match_ = line.find(win_match)

            if match_ != -1: # if the match is found then: 
                try: 
                    x = table[match_][idx]; y = table[match_][idx + 1]; z = table[match_][idx + 2]
                    matches_found.append(((s, (match_, idx)), (o, (match_, idx + 1)), (s, (match_, idx + 2))))
                except IndexError:
                    matches_found.append(((s, (idx, match_)), (o, (idx, match_ + 1)), (s, (idx, match_ + 2))))
    
    # Vertical Check

    for idx, line in enumerate(V_data):
        
        # check if the board has any point matches
        for win_match in possible_matches:
            match_ = line.find(win_match)

            if match_ != -1: # if the match is found then:
                try: 
                    x = table[idx][match_]; y = table[idx + 1][match_]; z = table[idx + 2][match_]
                    matches_found.append(((s, (idx, match_)), (o, (idx + 1, match_)), (s, (idx + 2, match_))))
                except IndexError:
                    matches_found.append(((s, (match_, idx)), (o, (match_ + 1, idx)), (s, (match_ + 2, idx))))

    # Right Across Check

    for info, coords in Rcross_data:

        for win_match in possible_matches:
            match_ = info.find(win_match)

            if match_ != -1:
                x = (s, (coords[0] + match_    , coords[1] - match_    ))
                y = (o, (coords[0] + match_ + 1, coords[1] - match_ - 1))
                z = (s, (coords[0] + match_ + 2, coords[1] - match_ - 2))

                matches_found.append((x, y, z))

    # Left Across Check

    for info, coords in Lcross_data:
        

        for win_match in possible_matches:
            match_ = info.find(win_match)

            diff = len(info) - match_ - 1

            if match_ != -1:
                x = (s, (coords[0] - diff, coords[1] - diff))
                y = (o, (coords[0] - diff + 1, coords[1] - diff + 1))
                z = (s, (coords[0] - diff + 2, coords[1] - diff + 2))

                matches_found.append((x, y, z))

    return matches_found


def remove_won_matches(table: Table, list_of_cords: Match_Data) -> tuple[Table, int]:

    points_won = 0

    for remover in list_of_cords:
        for each in remover:
            table = place(table, each[1], each[0]) # type: ignore
        points_won += 1
    
    return table, points_won
    

def check_endgame(table: Table) -> bool:

    for row in table:
        if empty in row:
            break
    else:
        return True
    return False

            
                



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

        padding_table_size = find_middle(size[0], input_infolength, space)

        while True:
            # display current table.
            print(f'\033c\nPlayer X: {points[0]} | Player Y: {points[1]}\n')

            display_table(table, f'SOS : {label} Table', 0, False, padding_table_size)

            if check_endgame(table):
                end_string = f'| Player {players[points[0] < points[1]]} has WON! with points -- {players[0]}: {points[0]} | {players[1]}: {points[1]} |\n'
                des_string = f'o{"":=^{(len(end_string) - 2)}}o\n'
                input(''.join([des_string, end_string, des_string]))
                break

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

            # checking for matches

            check = checkfor_sos(table)
            if len(check) > 0: table, points_won = remove_won_matches(table, check)

            # double checking for possible double match

            check = checkfor_sos(table)
            if len(check) > 0:
                cache = remove_won_matches(table, check)
                table = cache[0]
                points_won += cache[1]

            try:
                input(f"Player {players[not turn]} get's {points_won} point{'s' if points_won > 1 else ''}")
                points[not turn] += points_won
            except NameError:
                continue

            print('\033c')

            
                



