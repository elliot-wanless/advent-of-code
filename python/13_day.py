import time

input = open('python/inputs.txt').read().split('\n\n')
section = [section.split('\n') for section in input]
total = 0

def find_reflections(grid):
    for i in range(1, len(grid)):
        up = grid[:i]
        down = grid[i:]
        up = up[::-1]

        minimum_length = min(len(up), len(down))
        differences = 0

        # Part 2
        # for zipped_up, zipped_down in zip(up, down):
        #     for char1, char2 in zip(zipped_up, zipped_down):
        #         if(char1 != char2):
        #             differences += 1

        # if differences == 1:
        #     return i

        # Part 1
        up = up[:minimum_length]
        down = down[:minimum_length]
        
        if up == down:
            return i
        
    return 0

for grid in section:
    rotated_grid = list(zip(*grid))
    horizontal = find_reflections(grid)
    vertical = find_reflections(rotated_grid)
    total += (horizontal*100 + vertical)

print(total)