input = open('python/2023/inputs.txt').read().splitlines()

pipes = {}
start = None

# All directions a pipe can take
map_arr = [(-1,0),(0,1),(0,-1),(1,0)]

# Array of valid pipes
valid_pipes = ['|', '-', 'L', 'J', '7', 'F']

def pipe_type(pipe, i, j):
    # Map the pipe type
    match pipe:
        case '|': return (i-1,j), (i+1,j)
        case '-': return (i,j-1), (i,j+1)
        case 'L': return (i-1,j), (i,j+1)
        case 'J': return (i-1,j), (i,j-1)
        case '7': return (i+1,j), (i,j-1)
        case 'F': return (i+1,j), (i,j+1)
    return None

def connected(pos):
    # Return connected pipe
    current_pipe = pipes[*pos]
    dir1, dir2 = pipe_type(current_pipe, *pos)
    return {dir1, dir2}

def get_next(next):
    return (connected(next) - visited).pop()

for i, line in enumerate(input):
    for j, c in enumerate(line):
        # Find start point or add it to pipes matrix
        if c == 'S': start = (i,j)
        elif c != '.': pipes[i,j] = c

next1, next2 = None, None

for i,j in map_arr:
    # Find each next point
    current_pipe = (start[0]+i, start[1]+j)
    if current_pipe in pipes and start in connected(current_pipe):
        if next1 == None: next1 = current_pipe
        else: next2 = current_pipe

for c in valid_pipes:
    # Find the pipe type
    if {pipe_type(c, *start)} == {next1, next2}:
        pipes[start] = c

visited = {start, next1, next2}
steps = 1

while next1 != next2:
    next1 = get_next(next1)
    next2 = get_next(next2)

    # Set visited back to itself, unless it's the first time
    visited = {*visited, next1, next2}
    steps += 1

print("Part 1: ", steps)

count = 0
# Measure the polarity of the path by using the vertical pipes |LJ
for i in range(len(input)):
    polarity = False
    for j in range(len(input[0])):
        # Visited contains all the pipes we've visited (i.e. the original path)
        if (i,j) in visited:
            # If we hit a vertical pipe that faces north, change polarity
            # This is because we technically 'start' at the south facing ones
            if pipes.get((i,j), '') in '|LJ':
                polarity = not polarity
            continue
        # Whilst in a 'positive' polarity, add it!
        if polarity: count += 1


print("Part 2: ", count)