input = [line.split(" ") for line in open('python/inputs.txt').read().splitlines()]

queue, updated_queue = [], []
visited_list = list()
current = (0, 0)
length = 0

for line in input:
    # Strip the hexa out of the input
    hexa = line[2][2:-1]

    # Get the direction
    direction = hexa[-1]
    if direction == "0":
        direction = "R"
    elif direction == "1":
        direction = "D"
    elif direction == "2":
        direction = "L"
    elif direction == "3":
        direction = "U"

    n = int(hexa[:-1], 16)

    updated_queue.append([direction, n])

# Parse the queue - change 'updated_queue' to 'queue' for part 1
for line in updated_queue:
    match line[0]:
        case "U":
            queue.append((-1, 0, int(line[1])))
        case "D":
            queue.append((1, 0, int(line[1])))
        case "L":
            queue.append((0, -1, int(line[1])))
        case "R":
            queue.append((0, 1, int(line[1])))

for instruction in queue:
    # Increase length of outer loop
    length += n
    r_dir, c_dir, n = instruction
    r, c = current

    # Set current to the end of the instruction
    current = (r + r_dir*n, c + c_dir*n)

    # Add the whole edge to the visited list
    visited_list.append(current)

# Area of a polygon = 1/2 * abs(sum(x[i]*y[i+1] - x[i+1]*y[i]))
A = abs(sum(visited_list[i][0] * (visited_list[i - 1][1] - visited_list[(i + 1) % len(visited_list)][1]) for i in range(len(visited_list)))) // 2
i = A - length // 2 + 1

# Print the answer - area plus the outer loop
print(i + length)