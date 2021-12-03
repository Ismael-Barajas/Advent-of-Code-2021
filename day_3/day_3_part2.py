with open("./input.txt") as f:
    data = f.read().splitlines()

# Length of binary string
N = len(data[0])

# Convert binary string to decimal
data = [int(line, 2) for line in data]

# Find oxygen rating
o2_rem = data.copy()
pos = N - 1
while pos >= 0 and len(o2_rem) > 1:
    # Find the most common bit
    print(o2_rem[pos])
    ones = sum([((x & (1 << pos)) >> pos) for x in o2_rem])
    zeros = len(o2_rem) - ones

    if zeros > ones:
        o2_rem = list(filter(lambda x: not (x & (1 << pos)), o2_rem))
    else:
        o2_rem = list(filter(lambda x: (x & (1 << pos)), o2_rem))

    pos -= 1

# Find co2 rating
co2_rem = data.copy()
pos = N - 1
while pos >= 0 and len(co2_rem) > 1:
    # Find the most common bit
    ones = sum([((x & (1 << pos)) >> pos) for x in co2_rem])
    zeros = len(co2_rem) - ones

    if zeros > ones:
        co2_rem = list(filter(lambda x: (x & (1 << pos)), co2_rem))
    else:
        co2_rem = list(filter(lambda x: not (x & (1 << pos)), co2_rem))

    pos -= 1


ans = o2_rem[0] * co2_rem[0]
print(ans)


# Done with help of https://www.youtube.com/watch?v=jTRTH5NwblU
