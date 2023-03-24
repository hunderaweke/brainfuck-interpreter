import sys
from msvcrt import getch


def execute(filename):
    file = open(filename, "r")
    evaluate(file.read())


def evaluate(code):
    code = cleanup(list(code))
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
            if cells[cellptr] < 255:
                cells[cellptr] += 1
            else:
                cells[cellptr] = 0
        if command == '-':
            if cells[cellptr] > 0:
                cells[cellptr] -= 1
            else:
                cells[cellptr] = 255
        if command == '[' and cells[cellptr] == 0:
            codeprt = bracemap[codeprt]
        if command == ']' and cells[cellptr] != 0:
            codeprt = bracemap[codeprt]
        if command == ',':
            cells[cellptr] = ord(getch())
        if command == '.':
            sys.stdout.write(chr(cells[cellptr]))
        codeprt += 1


def map(code):
    temp, brace = [], {}
    for position, command in enumerate(code):
        if command == '[':
            temp.append(position)
        if command == ']':
            start = temp.pop()
            brace[start] = position
            brace[position] = start
    return brace


def cleanup(code):
    return ''.join(filter(lambda x: x in [
        '[', '>', '<', ',', '.', '+', '-', ']'], code))


def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        print("Usage: ", sys.argv[0], "filename")


if __name__ == "__main__":
    main()
