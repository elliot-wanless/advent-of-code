from collections import deque

input =  open('python/inputs.txt').read().splitlines()

grid, step_queue, queue = list(), deque(), deque()
steps = 0
start = (0, 0)
visited = set()

for i, line in enumerate(input):
    split_line = list(line)
    grid.append(split_line)
    if "S" in split_line:
        start = (i, split_line.index("S"))

queue.append((*start, 64))
visited.add(start)
ans = set()

while queue:
    i, j, steps = queue.popleft()
    if steps % 2 == 0:
        ans.add((i, j))
    if steps == 0:
        continue
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "#" and (x, y) not in visited:
            queue.append((x, y, steps - 1 ))
            visited.add((x, y))

print(len(ans))