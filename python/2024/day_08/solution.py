input = open('python/2024/day_08/inputs.txt').read().splitlines()

height, width = len(input), len(input[0])
contains_antinode = [[False] * width for _ in range(height)]
contains_extended_antinode = [[False] * width for _ in range(height)]
positions = {}

# Make a dictionary of all the positions of the characters
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char != '.':
            if char not in positions:
                positions[char] = [(x, y)]
            else:
                positions[char].append((x, y))

# Check if position is in bounds
def check_out_of_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

def find_antinodes(x, y, dx, dy):
    # Part 1 - Check if the antinode is within the bounds of the input
    if check_out_of_bounds(x - dx, y - dy):
        contains_antinode[y - dy][x - dx] = True

    # Part 2 - Extrapolate the antinode directionally
    while check_out_of_bounds(x, y):
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
