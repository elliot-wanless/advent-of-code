input = open('python/2024/day_15/inputs.txt').read()

parts = input.strip().split('\n\n')
warehouse = [list(row) for row in parts[0].split('\n')]
moves = ''.join(parts[1].split('\n'))
directions = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }

def find_robot(warehouse):  
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == '@':
                robot_pos = (y, x)
                return robot_pos
    return None

def try_move(warehouse, robot_pos, direction):
    y, x = robot_pos
    dy, dx = directions[direction]
    
    new_y, new_x = y + dy, x + dx
    
    # Check if new position is within bounds
    if new_y < 0 or new_y >= len(warehouse) or new_x < 0 or new_x >= len(warehouse[0]):
        return warehouse
    
    # If moving into a wall, do nothing
    if warehouse[new_y][new_x] == '#':
        return warehouse
    
    # If moving into a box
    if warehouse[new_y][new_x] == 'O':
        # Find all boxes that need to be pushed
        boxes_to_push = []
        check_y, check_x = new_y, new_x
        
        while warehouse[check_y][check_x] == 'O':
            boxes_to_push.append((check_y, check_x))
            check_y, check_x = check_y + dy, check_x + dx
            
            # Check if we hit a wall or went out of bounds
            if (check_y < 0 or check_y >= len(warehouse) or 
                check_x < 0 or check_x >= len(warehouse[0]) or
                warehouse[check_y][check_x] == '#'):
                return warehouse
        
        # Move is valid - push all boxes and move robot
        # Move boxes from back to front to prevent overwriting
        for box_y, box_x in reversed(boxes_to_push):
            warehouse[box_y + dy][box_x + dx] = 'O'
            warehouse[box_y][box_x] = '.'
        
        warehouse[new_y][new_x] = '@'
        warehouse[y][x] = '.'
    else:
        # Just move robot
        warehouse[new_y][new_x] = '@'
        warehouse[y][x] = '.'
    
    return warehouse

def print_warehouse(current_warehouse):
    for row in current_warehouse:
        print(''.join(row))
    print()

for move in moves:
    print(f"Move: {move}")
    robot_pos = find_robot(warehouse)
    warehouse = try_move(warehouse, robot_pos, move)
    # print_warehouse(warehouse)

gps_sum = 0
for y in range(len(warehouse)):
    for x in range(len(warehouse[y])):
        if warehouse[y][x] == 'O':
            gps_sum += (y * 100 + x)

print(gps_sum)
# print(f"The sum of all boxes' GPS coordinates is: {result}")
