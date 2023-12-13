from random import randint as rdi
Table = list[list[str]]

X, O, empty = 'X', 'O', ' '

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

positions = [O, X]

def interpretor(string: str, current_turn: int) -> tuple[bool, str | tuple[int]]:

    string = "".join(string.split())  # Removes any spaces if given.

    try:
        row, column = int(string[1]), int(string[2])
    except ValueError:
        return False, f"Move [{string[1]}][{string[2]}] are Invalid!"

    if valid_move(row, column):
        return True, (row, column)

    else:
        return False, f"Move [{row}][{column}] are Invalid!"

def valid_move(*args) -> bool:
    for move in args:
        if move not in [0,1,2]:
            return False
    else:
        return True

def valid_position(row: int, column: int, table: Table) -> bool:
    
    if table[row][column] == empty:
        return True
    return False

def placer(current_turn: int, coords: tuple[int], table: Table) -> Table:

    character = positions[abs(current_turn)]
    ro, co = coords
    
    if valid_position(ro, co, table):
        table[ro][co] = character
        return table, True

    else:
        return table, False
    
def main_menu():

    while True:
        choice = input(
            "\033c                  \
              o===---[X or O]---===o\
            \n|                    |\
            \n|      1. Start      |\
            \n|      2. Exit       |\
            \n|                    |\
            \no=======------=======o\
            \n      Input :: "
            )
        if choice in list('12'): break
        else: input('Incorrect Option! :: ')

    if choice in ['1']:
        turn = input(
            "\033c                  \
              o==--[Start with]--==o\
            \n|                    |\
            \n|        1. X        |\
            \n|        2. O        |\
            \n|                    |\
            \no=======------=======o\
            \n      Input :: "
            )
        if turn in list('12'):
            turn = abs(int(turn) - 2)
        else: input('Invalid Choice! Defaulting to X :: ')

    return turn

if __name__ == '__main__':

    turn = main_menu()



    
