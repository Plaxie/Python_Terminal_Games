
print('\033c')

title = 'Main Menu'

options = ['Start', 'Exit', 'Testing for spacing']

creds = 'By PLAXIE'

version= '1.0'

def display_menu(options: list|tuple, title: str = '', credit: str = '', version:str = '', size:int = 20, divider:int = 1) -> None:

    options = [f'[{idx}] {opt}' for idx, opt in enumerate(options, start=1)]

    longest = (sorted([credit] + [title] + options, key=len))[-1]

    min_display_width = len(longest) + 2

    size = min_display_width if size < min_display_width else size

    true_divider = f'o{'':-^{size}}o'

    sub_divider = f'|{'': ^{size}}|' * divider if divider > 0 else ''

    


    Title = '\n'.join(
        [
            true_divider,
            f'o{title: ^{size}}o',
            true_divider + '\n'
        ]
    )
    
    space = f'|{longest: ^{size}}|'.find('[') - 1
    len_diff = len(" "*space)

    Options = '\n'.join(
        [
            sub_divider,
            '\n'.join(
                [
                    f'|{" "*space}{opt: <{size-len_diff}}|' for opt in options
                ]
            ),
            sub_divider + '\n'
        ]
    )

    Credit = '\n'.join(
        [
            sub_divider,
            f'|  v{version}{credit: >{size - len(version) - 5}}  |',
            sub_divider,
            true_divider + '\n'
        ]
    )

    print(Options, Credit, sep ='')

    



display_menu(options, title, creds, version)



