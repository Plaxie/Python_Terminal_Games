
print('\033c')

title = 'Main Menu'

options = ['Start', 'Exit']

ver= 'v1.0'


def display_menu(options: list|tuple, title: str = '', credit: str = '', version:str = ver, bottomborder: bool = True, size:int = 20, divider:int = 1) -> None:

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
    print(Display)


def get_input(var_names: list|tuple, type_list: list|tuple, inside: list|tuple = [], size: int = 20) -> tuple:

    '''Get's Input of specified variables with correct types in a fixed format of size:
    - Variable Names [list of strings]
    - Types [list of strings] (must be equal length as var_names)
    - Size [int] (Format page size)'''

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
                match type_list[idx]:  # Check if type of the current variable is...
                    case 'int':  # then try to convert to int, if error try again, else break
                        out = int(input(inputformat('Integer', message, size)))
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
    for word in stringtoformat.split():

        # check if adding the fword would result in the breaking of the page,
        # if not then add the word to the currrent string.
        if len(temp_sentence + word + ' ') < size - 2: temp_sentence += word + ' '
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


display_menu(options, title, 'By Plaxie', ver, False, 30)
choice = get_input([
    'Enter the option of choice testing for longer formatting'
], ['int'], [1,2], 30
)