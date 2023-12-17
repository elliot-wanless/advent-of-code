grid = [list(row) for row in open('python/inputs.txt').read().splitlines()]

max_path = 0;

def setTile(tile, visited, queue):
    r, c, r_dir, c_dir = tile
    if (r, c, r_dir, c_dir) not in visited:
        visited.add(tile)
        queue.append(tile)

def energise(r, c, r_dir, c_dir):
    visited = set()
    queue = [(r, c, r_dir, c_dir)]

    while queue:
        r, c, r_dir, c_dir = queue.pop(0)
        
        r += r_dir
        c += c_dir

        # If we're out of bounds, skip
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        # Set the current tile
        tile = grid[r][c]

        # If the tile is empty, or the same direction as a mirror, keep travelling
        if tile == "." or (tile == "-" and c_dir != 0) or (tile == "|" and r_dir != 0):
            # If we've not visited this tile before, add it to the queue
            if (r, c, r_dir, c_dir) not in visited:
                setTile((r, c, r_dir, c_dir), visited, queue)
        elif tile == "/":
            # If we hit a mirror, change direction 90 degrees
            r_dir, c_dir = -c_dir, -r_dir
            if (r, c, r_dir, c_dir) not in visited:
                setTile((r, c, r_dir, c_dir), visited, queue)
        elif tile == "\\":
            # If we hit a mirror, change direction 90 degrees
            r_dir, c_dir = c_dir, r_dir
            if (r, c, r_dir, c_dir) not in visited:
                setTile((r, c, r_dir, c_dir), visited, queue)
        else:
            if tile == '|':
                # If the tile is a veritcal pipe, split into two directions, up and down
                for r_dir, c_dir in [(1, 0), (-1, 0)]:
                    if (r, c, r_dir, c_dir) not in visited:
                        setTile((r, c, r_dir, c_dir), visited, queue)
            else:
                # If the tile is a horizontal pipe, split into two directions, left and right
                for r_dir, c_dir in [(0, 1), (0, -1)]:
                    if (r, c, r_dir, c_dir) not in visited:
                        setTile((r, c, r_dir, c_dir), visited, queue)

    coords = {(r, c) for (r, c, _, _) in visited}

    return len(coords)

for r in range(len(grid)):
    # Get energised paths from the left and right of the grid
    energise_left = energise(r, -1, 0, 1)
    energise_right = energise(r, len(grid[0]), 0, -1)

    # Get the max path for these sides
    max_path = max(max_path, energise_left)
    max_path = max(max_path, energise_right)
    
for c in range(len(grid[0])):
    # Get energised paths from the top and bottom of the grid
    energise_up = energise(-1, c, 1, 0)
    energise_down = energise(len(grid), c, -1, 0)

    # Get the max path for these sides
    max_path = max(max_path, energise_up)
    max_path = max(max_path, energise_down)

print(max_path)

