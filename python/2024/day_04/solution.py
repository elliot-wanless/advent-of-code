input = open('python/2024/day_04/inputs.txt').read().splitlines()

directions = [
    (-1, 0),  # up
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (0, 1),   # right
    (0, -1),  # left
    (1, 1),   # down-right
    (1, -1),  # down-left
    (1, 0),   # down
]

rows = len(input)
cols = len(input[0])    

### Part 1 ###
count = 0
for i in range(rows):
    for j in range(cols):
        for dx, dy in directions:
            # Check out of bounds (multiply by  dx/dy to get the direction)
            if not (0 <= i + 3*dx < rows and 0 <= j + 3*dy < cols):
                continue
            # Check if the pattern is XMAS
            if (input[i][j] == 'X' and input[i + dx][j + dy] == 'M' and input[i + 2 * dx][j + 2 * dy] == 'A' and input[i + 3 * dx][j + 3 * dy] == 'S'):
                count += 1

print(count)

### Part 2 ###
count = 0
for i in range(rows):
    for j in range(cols):
        # Find an 'A'
        if input[i][j] == 'A':
            # Check out of bounds
            if not (0 <= i-1 < rows and 0 <= i+1 < rows and 
                0 <= j-1 < cols and 0 <= j+1 < cols):
                continue
            

            # Create the diagonals at each A point
            diagonal_1 = input[i-1][j-1] + input[i][j] + input[i+1][j+1] # up-left
            diagonal_2 = input[i+1][j+1] + input[i][j] + input[i-1][j-1] # down-right
            diagonal_3 = input[i-1][j+1] + input[i][j] + input[i+1][j-1] # down-left
            diagonal_4 = input[i+1][j-1] + input[i][j] + input[i-1][j+1] # up-right
            
            # Check all combinations of diagonals (e.g. up-left goes with down-left and up-right etc)
            combos = [
                (diagonal_1, diagonal_3),
                (diagonal_1, diagonal_4),
                (diagonal_2, diagonal_3),
                (diagonal_2, diagonal_4),
            ]

            # Check if BOTH diagonal combos are 'MAS' or 'SAM'
            if any((d1 in ['MAS', 'SAM'] and d2 in ['MAS', 'SAM']) for d1, d2 in combos):
                count += 1

print(count)
