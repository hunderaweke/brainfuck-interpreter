import sys
import msvcrt


def evaluate(code):
    bracemap = map(code)
    cellptr, codeprt, cells = 0, 0, [0]
    while codeprt < len(code):
        command = code[codeprt]
        if command == '>':
            cellptr += 1
            if cellptr == len(cells):
                cells.append(0)
        if command == "<":
            cellptr -= 1

        if command == '+':
            cells[cellptr] += 1 if cells[cellptr < 255] else 0
        if command == '-':
            cells[cellptr] -= 1 if cells > 0 else 255
        if command == '[' and cells[cellptr] == 0:
            codeprt = bracemap[codeprt]
        if command == ']' and cells[cellptr] != 0:
            codeprt = bracemap[codeprt]
        if command == ',':
            cells[cellptr] = ord(msvcrt.getch())
        if command == '.':
            sys.stdout.write(chr(cells[cellptr]))


def map(code):
    temp, brace = [], {}
    for position, command in enumerate(code):
        if command == '[':
            temp.append(position)
        if command == ']':
            start = temp.pop(position)
            brace[start] = position
            brace[position] = start
    return brace
