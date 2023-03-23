import sys

INCREASEMEMLOC = ">"
DECREASMEMLOC = "<"
INCREASEVAL = "+"
DECREASEVAL = "-"
CWHILE = "]"
JUMPBACK = "["
GETCHAR = ","
PUTCHAR = "."
ls = []
for _ in range(255):
    ls.append(0)
chars = ">>++<+>-"
index = 0

for char in chars:
    if char == INCREASEMEMLOC:
        index += 1
    if char == DECREASMEMLOC:
        index -= 1
    if char == INCREASEVAL and ls[index] <= 255:
        ls[index] += 1
    if char == DECREASEVAL and ls[index] > 0:
        ls[index] -= 1
print(*ls[0 : len(chars)])
