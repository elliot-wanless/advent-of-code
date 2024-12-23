from collections import deque
import heapq

MOVE_COST = 1
TURN_COST = 1000

def parse_input(grid):
    start = None
    end = None
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return grid, start, end

def get_turns(direction):
    if direction == (0, 1):    # East
        return [(1, 0), (-1, 0)]   # South, North
    elif direction == (1, 0):  # South
        return [(0, -1), (0, 1)]   # West, East
    elif direction == (0, -1): # West
        return [(-1, 0), (1, 0)]   # North, South
    else:                      # North
        return [(0, 1), (0, -1)]   # East, West

def find_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, (start[0], start[1], (0, 1)))]  # Start facing east
    seen = set()
    
    while pq:
        cost, (row, col, direction) = heapq.heappop(pq)
        
        if (row, col) == end:
            return cost
            
        state = (row, col, direction)
        if state in seen:
            continue
            
        seen.add(state)
        
        # Try moving forward
        new_row = row + direction[0]
        new_col = col + direction[1]
        
        if (0 <= new_row < rows and 0 <= new_col < cols and 
            grid[new_row][new_col] != '#'):
            heapq.heappush(pq, (cost + MOVE_COST, (new_row, new_col, direction)))
        
        # Try turning
        for new_dir in get_turns(direction):
            heapq.heappush(pq, (cost + TURN_COST, (row, col, new_dir)))
    
    return float('inf')

def find_optimal_tiles(grid, start, end, target_cost):
    rows, cols = len(grid), len(grid[0])
    
    # Forward pass to find states that can reach end with target cost
    forward_costs = {}  # (row, col, direction) -> cost
    pq = [(0, (start[0], start[1], (0, 1)))]
    
    while pq:
        cost, (row, col, direction) = heapq.heappop(pq)
        state = (row, col, direction)
        
        if cost > target_cost:
            continue
            
        if state in forward_costs:
            continue
            
        forward_costs[state] = cost
        
        # Try moving forward
        new_row = row + direction[0]
        new_col = col + direction[1]
        
        if (0 <= new_row < rows and 0 <= new_col < cols and 
            grid[new_row][new_col] != '#'):
            heapq.heappush(pq, (cost + MOVE_COST, (new_row, new_col, direction)))
        
        # Try turning
        for new_dir in get_turns(direction):
            heapq.heappush(pq, (cost + TURN_COST, (row, col, new_dir)))
    
    # Backward pass to find tiles that are part of optimal paths
    optimal_tiles = {start}
    to_process = [(end[0], end[1], d) for d in [(0,1), (0,-1), (1,0), (-1,0)]
                 if (end[0], end[1], d) in forward_costs 
                 and forward_costs[(end[0], end[1], d)] == target_cost]
    
    seen = set()
    while to_process:
        state = to_process.pop()
        if state in seen:
            continue
            
        seen.add(state)
        row, col, direction = state
        optimal_tiles.add((row, col))
        
        # Check previous move
        prev_row = row - direction[0]
        prev_col = col - direction[1]
        if (0 <= prev_row < rows and 0 <= prev_col < cols):
            prev_state = (prev_row, prev_col, direction)
            if (prev_state in forward_costs and 
                forward_costs[prev_state] == forward_costs[state] - MOVE_COST):
                to_process.append(prev_state)
        
        # Check previous turns
        for prev_dir in get_turns(direction):
            prev_state = (row, col, prev_dir)
            if (prev_state in forward_costs and 
                forward_costs[prev_state] == forward_costs[state] - TURN_COST):
                to_process.append(prev_state)
    
    return len(optimal_tiles)

def solve(input):
    grid, start, end = parse_input(input)
    part_1 = find_shortest_path(grid, start, end)
    part_2 = find_optimal_tiles(grid, start, end, part_1)
    return part_1, part_2

input = open('python/2024/day_16/inputs.txt').read().strip().splitlines()
part_1, part_2 = solve(input)
print("Part 1: ", part_1)
print("Part 2: ", part_2)
