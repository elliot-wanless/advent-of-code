input = open('python/2025/day_01/inputs.txt').read().splitlines()

# Part 1: Count how many times we land directly on 0
total = 50
count_part1 = 0

for line in input:
    if (line[0] == 'L'):
        total -= int(line[1:])
    elif (line[0] == 'R'):
        total += int(line[1:])

    total = total % 100

    if (total == 0):
        count_part1 += 1

print("Part 1:", count_part1)

# Part 2: Count how many times we pass through 0 (including landing on it)
total = 50
count_part2 = 0

for line in input:
    if (line[0] == 'L'):
        delta = -int(line[1:])
    elif (line[0] == 'R'):
        delta = int(line[1:])

    if delta >= 0:
        passes = (total + delta) // 100
    else:
        passes = (total - 1) // 100 - (total + delta - 1) // 100
    count_part2 += passes

    total = (total + delta) % 100

print("Part 2:", count_part2)