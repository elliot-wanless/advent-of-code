input_grid = open('python/2024/day_06/inputs.txt').read().splitlines()

def find_guard_position(grid):
    for i, line in enumerate(grid):
        if '^' in line:
            y, x = i, line.index('^')
            return y, x

### Part 1 ###
y, x = find_guard_position(input_grid)    
height, width = len(input_grid), len(input_grid[0])

visited = [[False] * width for _ in range(height)]
dx, dy = 0, -1
visited[y][x] = True

while 0 <= y + dy < height and 0 <= x + dx < width:
    next_y = y + dy
    next_x = x + dx
    
    if input_grid[next_y][next_x] == '#':
        dx, dy = -dy, dx
    else:
        y, x = next_y, next_x
        visited[y][x] = True

total = sum(sum(1 for cell in line if cell) for line in visited)
print("Part 1:", total)

### Part 2 ###
grid = [list(row) for row in input_grid]
start_y, start_x = find_guard_position(grid)

def check_makes_loop(grid, start_y, start_x):
    seen = set()
    y, x = start_y, start_x

    # Start going up
    dx, dy = 0, -1  
    
    while True:
        state = (y, x, dy, dx)
        if state in seen:
            return True
        seen.add(state)
        
        next_y = y + dy
        next_x = x + dx
        
        if not (0 <= next_y < height and 0 <= next_x < width):
            return False
            
        if grid[next_y][next_x] == '#':
            dx, dy = -dy, dx
        else:
            y, x = next_y, next_x

count = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] != '.':
            continue
        grid[y][x] = '#'
        if check_makes_loop(grid, start_y, start_x):
            count += 1
        grid[y][x] = '.'

print("Part 2:", count)
