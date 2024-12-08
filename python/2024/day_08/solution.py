input = open('python/2024/day_08/inputs.txt').read().splitlines()

contains_antinode = [[False] * len(input[0]) for _ in range(len(input))]
contains_extended_antinode = [[False] * len(input[0]) for _ in range(len(input))]
positions = {}

# Make a dictionary of all the positions of the characters
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char != '.':
            if char not in positions:
                positions[char] = [(x, y)]
            else:
                positions[char].append((x, y))

def find_antinodes(x, y, dx, dy):
    # Part 1 - Check if the antinode is within the bounds of the input
    if 0 <= x - dx < len(input[0]) and 0 <= y - dy < len(input):
        contains_antinode[y - dy][x - dx] = True

    # Part 2 - Extrapolate the antinode directionally
    while 0 <= x < len(input[0]) and 0 <= y < len(input):
        contains_extended_antinode[y][x] = True
        y -= dy
        x -= dx

# For each character, find the antinodes
for _, coords in positions.items():
    for i, (x1, y1) in enumerate(coords):
        for x2, y2 in coords[i+1:]:  
            # Find the difference in x and y
            dx, dy = x2 - x1, y2 - y1

            # Find the antinodes
            find_antinodes(x1, y1, dx, dy)
            find_antinodes(x2, y2, -dx, -dy)

print("Part 1: ", sum(sum(line) for line in contains_antinode))
print("Part 2: ", sum(sum(line) for line in contains_extended_antinode))
