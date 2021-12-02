with open("./input.txt") as f:
    data = f.readlines()

# Part 1
horizontal_positions = 0
depth = 0
for line in data:
    command, unit = line.split()
    units = int(unit)
    if command == "forward":
        horizontal_positions += units
    if command == "down":
        depth += units
    if command == "up":
        depth -= units

print(f"Part 1: {horizontal_positions * depth}")

# Part 2
horizontal_positions = 0
depth = 0
aim = 0
for line in data:
    command, unit = line.split()
    units = int(unit)
    if command == "forward":
        horizontal_positions += units
        depth += aim * units
    if command == "down":
        aim += units
    if command == "up":
        aim -= units

print(f"Part 2: {horizontal_positions * depth}")
