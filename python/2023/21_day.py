from collections import deque

input =  open('python/2023/inputs.txt').read().splitlines()

grid, step_queue, queue = list(), deque(), deque()
steps, start = 0, (0, 0)
visited = set()

# Make a grid and find the start "S"
for i, line in enumerate(input):
    split_line = list(line)
    grid.append(split_line)
    # Set the start coordinates to "S"
    if "S" in split_line:
        start = (i, split_line.index("S"))

# Append the starting coordinates and 64 steps to a tuple
queue.append((*start, 64))
visited.add(start)
ans = set()

while queue:
    i, j, steps = queue.popleft()

    # If the steps are 0, we are done here
    if steps == 0:
        continue

    # If the steps are even, add the coordinates to the set as it can land back on itself in a loop
    if steps % 2 == 0:
        ans.add((i, j))
    
    # For each direction in the grid, check if it is a valid move and add it to the queue
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "#" and (x, y) not in visited:
            # Decrease the step
            queue.append((x, y, steps - 1 ))
            visited.add((x, y))

print(len(ans))