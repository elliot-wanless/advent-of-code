from heapq import heappush, heappop

grid = open('python/inputs.txt').read().splitlines()

# Make the grid integers instead of strings
for i, line in enumerate(grid):
    grid[i] = list(map(int, line.strip()))

queue = [(0, 0, 0, 0, 0, 0)]
visited = set()

while queue:
    heat_loss, r, c, r_dir, c_dir, count = heappop(queue)
    
    # If we are at the bottom right, we will have the lowest heat loss
    # By using a priority queue (heap) we will always get the lowest heat loss first
    if r == len(grid) - 1 and c == len(grid[0]) - 1 and count >= 4:
        print(heat_loss)
        break

    # If we've visited this tile before, skip
    if (r, c, r_dir, c_dir, count) in visited:
        continue

    visited.add((r, c, r_dir, c_dir, count))
    
    # If we haven't travelled 10 in the same direction and we aren't at the start, keep travelling
    if count < 10 and (r_dir, c_dir) != (0, 0):
        new_r = r + r_dir
        new_c = c + c_dir
        # If the new row and column aren't out of bounds, add the tile to the queue
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            extra_loss = grid[new_r][new_c]
            heappush(queue, (heat_loss + extra_loss, new_r, new_c, r_dir, c_dir, count + 1))

    # If we have travelled 4 or more or we don't have a direction (e.g. at the start), split into 4 directions
    if count >= 4 or (r_dir, c_dir) == (0, 0):
        for new_r_dir, new_c_dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # If the new direction isn't the same or doubling back on the path, add the tile to the queue
            if (new_r_dir, new_c_dir) != (r_dir, c_dir) and (new_r_dir, new_c_dir) != (-r_dir, -c_dir):
                new_r = r + new_r_dir
                new_c = c + new_c_dir
                # If not out of bounds, add the tile to the queue with count of 1 (as new direction started)
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                    extra_loss = grid[new_r][new_c]
                    heappush(queue, (heat_loss + extra_loss, new_r, new_c, new_r_dir, new_c_dir, 1))