
from pyclbr import Function
from types import FunctionType


print('\033c')

ver= 'v1.0'

#############################################
#       GRAPHICS AND INPUT FUNCTIONS        #
#############################################



def display_menu(options: list|tuple, title: str = '', credit: str = '', version:str = ver, bottomborder: bool = True, clear = False, size:int = 20, divider:int = 1) -> None:

    '''Displays a Menu or Page in a fixed format that contains: Title, Options, Credit and version with:-
    - sections: options [required], title, credit, version
    - elements: size (page size), divider (space between sections)'''

    # alligned numbers for each option
    options = [f'[{idx}] {opt}' for idx, opt in enumerate(options, start=1)]
    
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
        display_func: Function,
        var_names: list|tuple,
        type_list: list|tuple,
        inside: list|tuple = [],
        size: int = 20, 
        argsforfunc = (None,)
        ) -> list|tuple:

    '''Get's Input of specified variables with correct types in a fixed format of size:
    - Variable Names [list of strings]
    - Types [list of strings] (must be equal length as var_names)
    - Inside [list of types that must be in the input for specific inputs]
    - Size [int] (Format page size)
    - Clear: To clear the terminal
    - function to start with (usually a display page: Must provide all arguments)''' 

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
                if func: Dispfc(f_o, f_t, f_c, f_v, f_bb, f_cl, f_s, f_d) # unbound: ignore
                match type_list[idx]:  # Check if type of the current variable is...
                    case 'int':  # then try to convert to int, if error try again, else break
                        out = int(input(inputformat('Integer', message, size)))
                        if out == '0': out = 0
                        if out not in inside:  
                            raise ValueError()  # Raise a value error for an invalid input.
                        else:
                            break

                    case 'str':  # then try to convert to string, if empty try again, else break
                        out = str(input(inputformat('Words', message, size)))
                        if out == '' or out not in inside:  
                            raise ValueError()  # Raise a value error for an empty string or an invalid input.
                        else:
                            break

                    case 'bool':  # then try to convert to boolean, if error try again, else break
                        out = bool(input(inputformat('True/False', message, size)))
                        if out not in inside:  
                            raise ValueError()  # Raise a value error for an invalid input.
                        else:
                            break
                    
                    case 'float':  # then try to convert to float, if error try again, else break
                        out = float(input(inputformat('Decimal', message, size)))
                        if out not in inside:  
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




def inputformat(input_hint: str, message: str, size = 20) -> str:

    '''Formats for input:
    - input hint
    - message to display
    - layout size'''

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
                    f'| {strings: <{size-2}} |' for strings in stringparts
                ]
            ),
            f'o{'':-^{size}}o',
            f'{input_hint} :: '
        ]
    )

    return page


messages = [
    'Enter the Integer needed as mentione above for the following execution',
    'Enter the needed String to operate without further hindrance',
    'Are you Human?',
    'What is the value of pi, a mathematical constant used to find the circumference, area and volume of sperical objects'
]

types = ['int', 'str', 'bool', 'float']


# display_menu(options, title, 'By Plaxie', ver, False, 30)
# choice = get_input(
#     display_menu, # type: ignore

#     [
#         'Enter the option choice'
#     ], ['int'], [1,2], 30,

#     (options, title, 'By Plaxie', ver, False, True, 30, 1)
# )

#############################################
#            MAINLOOP FUNCTIONS             #
#############################################

def main_menu():

    choice = get_input(
        display_menu, # type: ignore
        [
            'Enter the option choice'
        ], ['int'], [1,2], 30, 

        (['Start', 'Exit'], 'Main Menu', 'By Plaxie', ver, False, True, 30, 1)
    )

    if choice == [2]: exit()

    choice = get_input(
        display_menu, # type: ignore
        [
            'Enter the option choice'
        ], ['int'], [1,2], 30, 

        (['3x3', '4x4', '5x5', '10x10', 'Custom!'], 'Size', 'By Plaxie', ver, False, True, 30, 1)
    )


#############################################
#              LOGIC FUNCTIONS              #
#############################################




#############################################
#              TABLE FUNCTIONS              #
#############################################

def display_table(table: list[list], title: str = '', clear:bool = False) -> None: 
    
    '''{Displays a Table} in a clean format:
    - Table
    - Title (not required)
    - Clear: clears the terminal if set to [True]'''
    
    # Just string joins and list Comprehension Magic.
    print('\n'.join(['\033c' if clear else ''] + [f'' if title == '' else '\n'.join([f'o{"":-^{6*len(table)-1}}o', f'|'+ f"{title: ^{6*len(table)-1}}" +'|'])]+ ['o-----'*len(table)+'o'] + [''.join([f'|#####' if row[cdx] == 0 else f'|{row[cdx]: ^5}' for cdx in range(len(row)) ] + ['|\n' + 'o-----'*len(table)+'o'])for rdx, row in enumerate(table)]))


if __name__ == '__main__':
    main_menu()