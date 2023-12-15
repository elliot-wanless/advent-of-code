input = open('python/inputs.txt').read().splitlines()

grid = list(map("".join, zip(*input)))
total = 0

for i, row in enumerate(grid):
    sorted_row = []
    # For each row, split it on every "#"
    for group in row.split("#"):
        # Sort each group so all the Os are at the end
        sorted_array = sorted(list(group), reverse=True)
        sorted_array = "".join(sorted_array)
        sorted_row += sorted_array + '#'
    # Remove the last "#" from the row from the line above
    grid[i] = sorted_row[:-1]


for sorted_row in grid:  
    # Count all the Os and get the position - add it to total!
    for j, char in enumerate(sorted_row):
        if char == 'O':
            total += len(grid)-j

print(total)