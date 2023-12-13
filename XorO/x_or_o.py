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

pieces = [O, X]

def interpretor(string: str, turn: int) -> Table:

    string = "".join(string.split())  # Removes any spaces if given.

    if turnfind(string[0]) != turn:
        return False, f"Not {pieces[abs(turn-1)]}'s Turn!"
    else:
        try:
            row, column = int(string[1]), int(string[2])
        except ValueError:
            return False, f"Move [{string[1]}][{string[2]}] are Invalid!"

        if valid(row, column):
            pass

        else:
            return False, f"Move [{row}][{column}] are Invalid!"

def turnfind(character: str) -> int:
    match character:
        case 'X': return 1
        case 'O': return 0
    return 2

def valid(*args):
    for move in args:
        if move not in [0,1,2]:
            return False
    else:
        return True



