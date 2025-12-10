input = open('python/2025/day_03/inputs.txt').read().strip().splitlines()

def find_max_joltage(bank, num_batteries):
    n = len(bank)
    result = []
    start = 0

    for i in range(num_batteries):
        end = n - num_batteries + i

        max_digit = '0'
        max_pos = start
        for pos in range(start, end + 1):
            if bank[pos] > max_digit:
                max_digit = bank[pos]
                max_pos = pos

        result.append(max_digit)
        start = max_pos + 1

    return int(''.join(result))

# Part 1: Select 2 batteries
total_part1 = 0
for bank in input:
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    total_part1 += max_joltage

print("Part 1:", total_part1)

# Part 2: Select 12 batteries
total_part2 = 0
for bank in input:
    joltage = find_max_joltage(bank, 12)
    total_part2 += joltage

print("Part 2:", total_part2)
