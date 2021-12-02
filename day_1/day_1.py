with open("./input.txt") as f:
    data = [int(line.rstrip()) for line in f]

# Part 1
## if true its 1 if false 0, then list is summed
count = sum(data[i] > data[i - 1] for i in range(1, len(data)))
print(f"Part 1: {count}")

# Part 2
count = sum(data[i] > data[i - 3] for i in range(3, len(data)))
print(f"Part 2: {count}")
