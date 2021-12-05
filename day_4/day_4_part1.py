with open("./input.txt") as f:
    data = f.read()

draw, *boards = data.split("\n\n")

array = []
for board in boards:
    array.append(board.split("\n"))

print(array)
print(draw)
