input = tuple(open('python/2023/inputs.txt').read().splitlines())

grid = input
previous = {grid}
array = [grid]
total, i = 0, 0

def rotate():
    # Had to rewrite Part 2 because Part 1 didn't rotate correctly.
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

# If we find a pattern, we can use the pattern to find the answer.
for _ in range(1000000000):
    rotate()
    i+=1
    if grid in previous:
        break
    previous.add(grid)
    array.append(grid)
    
first = array.index(grid)
cycle_length = i - first

# Find the remaining cycles
remaining_cycles = (1000000000 - first) % cycle_length

# Find the grid that matches the state after the remaining cycles
grid = array[remaining_cycles + first]

# Count 'em up!
for r, row in enumerate(grid):
    total += row.count("O") * (len(grid) - r)

print(total)