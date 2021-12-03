with open("./input.txt") as f:
    data = f.read().splitlines()

# Length of binary string
N = len(data[0])

# preallocate list with None & length of N
gamma = [None] * N  # if greater
epsilon = [None] * N  # if less

for position in range(N):
    # Iterates through each line of data and sums total of zeros and ones at position
    zeros = sum([data[line][position] == "0" for line in range(len(data))])
    ones = sum([data[line][position] == "1" for line in range(len(data))])

    # If zeros is greater in position than set gamma to 0 and epsilon 1 else invert
    if zeros > ones:
        gamma[position] = "0"
        epsilon[position] = "1"
    else:
        gamma[position] = "1"
        epsilon[position] = "0"

# Join gamma & epsilon array to string and convert from base 2 to base 10 then multiply for solution
solution = int("".join(gamma), 2) * int("".join(epsilon), 2)
print(solution)


# Done with help of https://www.youtube.com/watch?v=jTRTH5NwblU
