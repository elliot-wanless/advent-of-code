from collections import deque

input = open('python/2024/day_18/inputs.txt').read().splitlines()
# input = open('python/2024/day_18/test.txt').read().splitlines()


bytes = [tuple(map(int, line.split(','))) for line in input]

start = (0, 0)

min_bytes = 1024
grid_size = 70
# min_bytes = 12
# grid_size = 6

def build_grid(bytes, grid_size):
    grid = [['.' for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]
    for y, x in bytes:
        grid[x][y] = '#'
    return grid

def find_shortest_path(grid, start, grid_size):
    queue = deque([(start, 0)])  # (position, steps)
    visited = {start}
    target = (grid_size, grid_size)
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
    
    while queue:
        (x, y), steps = queue.popleft()
        
        if (x, y) == target:
            return steps
            
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (0 <= new_x <= grid_size and 
                0 <= new_y <= grid_size and 
                grid[new_x][new_y] != '#' and
                (new_x, new_y) not in visited):
                
                queue.append(((new_x, new_y), steps + 1))
                visited.add((new_x, new_y))
    
    return -1  # No path found

# Part 1 - Find shortest path with all bytes
grid = build_grid(bytes[:min_bytes], grid_size)
result = find_shortest_path(grid, start, grid_size)
print("Part 1:", result)

# Part 2 - Binary search to find first blocking byte
def can_reach_target(num_bytes):
    grid = build_grid(bytes[:num_bytes], grid_size)
    return find_shortest_path(grid, start, grid_size) != -1

left, right = 1, len(bytes)
blocking_byte = (0, 0)

while left <= right:
    mid = (left + right) // 2
    if can_reach_target(mid):
        left = mid + 1
    else:
        blocking_byte = (bytes[mid-1][0], bytes[mid-1][1])
        right = mid - 1

print("Part 2:", blocking_byte)

