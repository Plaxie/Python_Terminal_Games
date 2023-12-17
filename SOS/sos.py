
print('\033c')

title = 'Main Menu'

options = ['Start', 'Exit']

ver= 'v1.0'

def display_menu(options: list|tuple, title: str = '', credit: str = '', version:str = ver, size:int = 20, divider:int = 1) -> None:

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
            sub_divider + '\n' if sub_divider != '' else sub_divider,
            true_divider + '\n'
        ]
    )

    # Combine the Pieces.
    Display = Title + Options + Last
    # Display the page.
    print(Display)




