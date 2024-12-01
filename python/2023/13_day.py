input = open('python/2023/inputs.txt').read().split('\n\n')
section = [section.split('\n') for section in input]
total = 0

def find_reflections(grid):
    for i in range(1, len(grid)):
        # Split the grid into two parts
        # Up are the rows above the reflection (reversed for easier comparison)
        up = grid[:i][::-1]
        # Down are the rows below the reflection
        down = grid[i:]

        # Part 2
        differences = 0
        # Look at  each  character in the up/down rows
        for zipped_up, zipped_down in zip(up, down):
            for char1, char2 in zip(zipped_up, zipped_down):
                # If they're different, increment differences
                if(char1 != char2):
                    differences += 1

        # We only want to change one 'smudge'
        if differences == 1:
            return i

        # # Part 1
        # minimum_length = min(len(up), len(down))
        # up = up[:minimum_length]
        # down = down[:minimum_length]
        
        # if up == down:
        #     return i
        
    return 0

for grid in section:
    # Rotate the grid so I can reuse my function above
    rotated_grid = list(zip(*grid))

    # Get horizontal and vertical reflections
    horizontal = find_reflections(grid)
    vertical = find_reflections(rotated_grid)

    # Add to the total
    total += horizontal*100 + vertical

print(total)