input = open('python/2025/day_04/inputs.txt').read().strip().splitlines()

grid = [list(line) for line in input]
rows = len(grid)
cols = len(grid[0])

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def count_accessible(grid, rows, cols):
    """Count and return positions of accessible rolls."""
    accessible = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent_rolls = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent_rolls += 1

                if adjacent_rolls < 4:
                    accessible.append((r, c))

    return accessible

# Part 1: Count rolls accessible by forklift (initial state)
accessible_part1 = count_accessible(grid, rows, cols)
print("Part 1:", len(accessible_part1))

# Part 2: Remove rolls iteratively until none are accessible
grid_copy = [list(line) for line in input]
total_removed = 0

while True:
    accessible = count_accessible(grid_copy, rows, cols)
    if not accessible:
        break

    for r, c in accessible:
        grid_copy[r][c] = '.'

    total_removed += len(accessible)

print("Part 2:", total_removed)
