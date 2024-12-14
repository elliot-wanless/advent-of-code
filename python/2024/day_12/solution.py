import math

input = open('python/2024/day_12/test.txt').read().splitlines()

def find_regions(grid):
    height = len(grid)
    width = len(grid[0])
    visited = set()
    regions = []
    
    def get_region(r, c, letter):
        # Check if out of bounds or already visited
        if (r < 0 or r >= height or c < 0 or c >= width or 
            grid[r][c] != letter or (r, c) in visited):
            return set()
        
        # Add current cell to region
        region = {(r, c)}
        visited.add((r, c))
        
        # Check all 4 directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            region.update(get_region(r + dr, c + dc, letter))
            
        return region
    
    # Find all regions
    for r in range(height):
        for c in range(width):
            # Check if cell has not been visited
            if (r, c) not in visited:
                region = get_region(r, c, grid[r][c])
                if region:
                    regions.append((grid[r][c], region))
    
    return regions

def calculate_perimeter(region, grid):
    perimeter = []
    sides = set()

    for r, c in region:
        # Check all 4 directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc

            # If out of bounds or different letter, add to perimeter
            if (new_r < 0 or new_r >= len(grid) or 
                new_c < 0 or new_c >= len(grid[0]) or 
                grid[new_r][new_c] != grid[r][c]):
                perimeter.append((r, c))
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in perimeter:
                print("#", end="")
            else:
                print(".", end="")
        print()  # New line after each row

    return perimeter, sides

# Usage example:
total_price = 0
total_edge_price = 0
regions = find_regions(input)

for letter, region in regions:
    area = len(region)
    perimeter, sides = calculate_perimeter(region, input)
    price = area * len(perimeter)
    print(len(sides))
    total_price += price
    total_edge_price += area * len(sides)

print("Part 1:", total_price)
print("Part 2:", total_edge_price)