input = open('python/inputs.txt').read().splitlines()

galaxies, extra_rows, extra_columns = [], [], []
sum = 0;

# Set to '1' for Part 1
space = 999999

def get_added_rows(galaxy, other_galaxy):
    added_rows = 0
    # Find the rows inbetween the two galaxies
    for i, row in enumerate(extra_rows):
        # If the row is inbetween the two galaxies, add the space
        if (row > galaxy and row < other_galaxy) or (row < galaxy and row > other_galaxy):
            added_rows += (1 * space)
    return added_rows

def get_added_columns(galaxy, other_galaxy):
    added_columns = 0
    # Find the columns inbetween the two galaxies
    for column in extra_columns:
        # If the column is inbetween the two galaxies, add the space
        if (column > galaxy and column < other_galaxy) or (column < galaxy and column > other_galaxy):
            added_columns += (1 * space)
    return added_columns

# Find which rows have no galaxies
for i, line in enumerate(input):
    is_galaxy = False
    for j, c in enumerate(line):
        if c == "#":
            is_galaxy = True
            # Store the index of the galaxy
            galaxies.append((i, j))
    if not is_galaxy:
        # Add the i-index of the empty row
        extra_rows.append(i)

# Find which columns have no galaxies
for j in range(len(input[0])):
    is_galaxy = False
    for i, line in enumerate(input):
        if line[j] == "#":
            is_galaxy = True
    if not is_galaxy:
        # Add the j-index of the empty column
        extra_columns.append(j)

# For each galaxy, find the distance to every other galaxy
for i, galaxy in enumerate(galaxies):
    # Add all the galaxies after the current one to a queue
    queue = galaxies[i+1:]
    for other_galaxy in queue:
        # Get number of rows and columns between the two galaxies
        added_rows = get_added_rows(galaxy[0], other_galaxy[0])
        added_columns = get_added_columns(galaxy[1], other_galaxy[1])

        # Calculate the distance, plus the space inbetween
        distance = abs(galaxy[1] - other_galaxy[1]) + abs(galaxy[0] - other_galaxy[0]) + added_rows + added_columns
        sum += distance

print(sum)