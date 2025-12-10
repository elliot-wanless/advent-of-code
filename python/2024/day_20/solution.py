from collections import defaultdict, deque
from typing import List, Tuple, Set, Dict

input = open('python/2024/day_20/inputs.txt').read().splitlines()

def parse_map(lines):
    grid = [list(line) for line in lines]
    start = end = None
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i,j)
                grid[i][j] = '.'
            elif grid[i][j] == 'E': 
                end = (i,j)
                grid[i][j] = '.'
                
    return grid, start, end

def get_neighbors(pos, grid):
    i, j = pos
    neighbors = []
    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '.':
            neighbors.append((ni, nj))
    return neighbors

def build_distance_map(grid, start):
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        pos = queue.popleft()
        curr_dist = distances[pos]
        
        for next_pos in get_neighbors(pos, grid):
            if next_pos not in distances:
                distances[next_pos] = curr_dist + 1
                queue.append(next_pos)
                
    return distances

def find_cheats(grid, start, end, max_cheat_dist = 2):
    # Pre-compute distances from start and end
    start_distances = build_distance_map(grid, start)
    end_distances = build_distance_map(grid, end)
    
    if end not in start_distances:
        return {}  # No valid path exists
        
    base_time = start_distances[end]
    savings = defaultdict(int)
    
    # Find all empty spaces
    empty_spaces = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) 
                   if grid[i][j] == '.']
    
    # Try all possible cheat combinations
    for pos1 in empty_spaces:
        if pos1 not in start_distances:
            continue
            
        time_to_pos1 = start_distances[pos1]
        
        for pos2 in empty_spaces:
            manhattan_dist = abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])
            if manhattan_dist > max_cheat_dist or pos2 not in end_distances:
                continue
                
            time_from_pos2 = end_distances[pos2]
            total_time = time_to_pos1 + manhattan_dist + time_from_pos2
            
            if total_time < base_time:
                savings[base_time - total_time] += 1
                
    return savings

grid, start, end = parse_map(input)

# Part 1 - Short range cheats
savings = find_cheats(grid, start, end, max_cheat_dist=2)
total = sum(count for time_saved, count in savings.items() if time_saved >= 100)
print("Part 1:", total)

def find_cheats_v2(grid, start, end):
    # Pre-compute distances from start and end
    start_distances = build_distance_map(grid, start)
    end_distances = build_distance_map(grid, end)
    
    if end not in start_distances:
        return {}  # No valid path exists
        
    base_time = start_distances[end]
    savings = defaultdict(int)
    
    # Find all empty spaces
    empty_spaces = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) 
                   if grid[i][j] == '.']
    
    # Try all possible cheat combinations
    for pos1 in empty_spaces:
        if pos1 not in start_distances:
            continue
            
        time_to_pos1 = start_distances[pos1]
        
        # Check positions within 20 moves of pos1
        for pos2 in empty_spaces:
            manhattan_dist = abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])
            if manhattan_dist > 20 or pos2 not in end_distances:
                continue
                
            time_from_pos2 = end_distances[pos2]
            total_time = time_to_pos1 + manhattan_dist + time_from_pos2
            
            if total_time < base_time:
                savings[base_time - total_time] += 1
                
    return savings

# For part 2
savings_v2 = find_cheats_v2(grid, start, end)
total_v2 = sum(count for time_saved, count in savings_v2.items() if time_saved >= 100)
print("Part 2:", total_v2)
