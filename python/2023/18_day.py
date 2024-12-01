input = [line.split(" ") for line in open('python/2023/inputs.txt').read().splitlines()]

visited = list()
length, current = 0, (0, 0)
mapping = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

for line in input:
    r, c = current
    # Strip the hexa out of the input
    hexa = line[2][2:-1]
    # Get the direction
    direction = "RDLU"[int(hexa[-1])]
    # Get the number from hexadecimals
    n = int(hexa[:-1], 16)
    # Get the direction from the mapping
    r_dir, c_dir = mapping[direction]
    # Increase length of outer loop
    length += n
    # Set current to the end of the instruction
    current = (r + r_dir*n, c + c_dir*n)
    # Add the whole edge to the visited list
    visited.append(current)

# Area of a polygon = 1/2 * abs(sum(x[i]*y[i+1] - x[i+1]*y[i]))
A = abs(sum(visited[i][0] * (visited[i - 1][1] - visited[(i + 1) % len(visited)][1]) for i in range(len(visited)))) // 2
i = A - length // 2 + 1

# Inner-area plus the outer loop
print(i + length)