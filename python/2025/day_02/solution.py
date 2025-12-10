input = open('python/2025/day_02/inputs.txt').read().strip()

ranges = []
for range_str in input.split(','):
    start, end = map(int, range_str.split('-'))
    ranges.append((start, end))

def is_invalid_part1(id_num):
    s = str(id_num)

    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]

    if first_half[0] == '0':
        return False

    return first_half == second_half

def is_invalid_part2(id_num):
    s = str(id_num)
    n = len(s)

    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = n // pattern_len
            if pattern * repetitions == s:
                if repetitions >= 2:
                    if pattern[0] != '0':
                        return True

    return False

# Part 1: Find all invalid IDs (repeated exactly twice)
total_part1 = 0
for start, end in ranges:
    for id_num in range(start, end + 1):
        if is_invalid_part1(id_num):
            total_part1 += id_num

print("Part 1:", total_part1)

# Part 2: Find all invalid IDs (repeated at least twice)
total_part2 = 0
for start, end in ranges:
    for id_num in range(start, end + 1):
        if is_invalid_part2(id_num):
            total_part2 += id_num

print("Part 2:", total_part2)
