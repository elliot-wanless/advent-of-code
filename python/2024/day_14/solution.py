input = open('python/2024/day_14/inputs.txt').read().splitlines()

robots = []
quadrants = [0] * 4

width, height = 101, 103
# width, height = 11, 7 # for test input

half_width = width // 2
half_height = height // 2

for line in input:
    pos, vel = line.split()
    px, py = map(int, pos[2:].split(','))
    vx, vy = map(int, vel[2:].split(','))
    robots.append(((px, py), (vx, vy)))

def simulate_robots(robots, seconds, width, height):
    new_robots = []
    for (px, py), (vx, vy) in robots:
        # Calculate new position after given seconds
        new_x = (px + vx * seconds) % width
        new_y = (py + vy * seconds) % height
        new_robots.append(((new_x, new_y), (vx, vy)))
    return new_robots

# Simulate for 100 seconds
positions = simulate_robots(robots, 100, width, height)

# For each robot position
for (x, y), _ in positions:
    # Ensure coordinates are within bounds
    x = int(x) % width
    y = int(y) % height

    # Skip robots on the middle lines
    if x == half_width or y == half_height:
        continue

    # Top left
    if x < half_width and y < half_height:
        quadrants[0] += 1
    # Top right
    elif x < half_width and y > half_height:
        quadrants[1] += 1
    # Bottom left
    elif x > half_width and y < half_height:
        quadrants[2] += 1
    # Bottom right
    elif x > half_width and y > half_height:
        quadrants[3] += 1
    
safety_factor = 1
for count in quadrants:
    if count > 0: 
        safety_factor *= count

### Part 2 (have fun scrolling) ###
for count in range(10000):
    print("Iteration: ", count)
    positions = simulate_robots(robots, count, width, height)
    grid = [['.'] * width for _ in range(height)]
    for (x, y), _ in positions:
        x = x % width
        y = y % height
        grid[y][x] = '#'

    # Print the grid and enjoy finding the tree
    for row in grid:
        print(''.join(row))
    print()

print("Part 1: ", safety_factor)