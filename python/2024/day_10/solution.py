input = open('python/2024/day_10/inputs.txt').read().splitlines()

def find_trail(grid, y, x, current_num, visited, nines):
    # Out of bounds
    if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):  
        return 0
    
    # Already visited
    if (y, x) in visited:  
        return 0
    
    current_value = int(grid[y][x])

    # Must increment by exactly 1
    if current_value != current_num:  
        return 0
    
    # Found a complete path
    if current_value == 9:  
        nines.add((y, x))
        return 1
        
    # Add current position to visited
    visited.add((y, x))
    
    # Try all directions, looking for an increment of 1
    paths = 0
    paths += find_trail(grid, y-1, x, current_value + 1, visited.copy(), nines)  # Up
    paths += find_trail(grid, y+1, x, current_value + 1, visited.copy(), nines)  # Down
    paths += find_trail(grid, y, x-1, current_value + 1, visited.copy(), nines)  # Left
    paths += find_trail(grid, y, x+1, current_value + 1, visited.copy(), nines)  # Right
    
    return paths

# Main code
part_1_total = 0
part_2_total = 0
for i, line in enumerate(input):
    for j in range(len(line)):
        # Start from zeros
        if int(line[j]) == 0:  
            reachable_nines = set()
            paths = find_trail(input, i, j, 0, set(), reachable_nines)
            distinct_paths = len(reachable_nines)
            part_1_total += distinct_paths
            part_2_total += paths

print("Part 1:", part_1_total)
print("Part 2:", part_2_total)
