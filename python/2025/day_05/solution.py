input = open('python/2025/day_05/inputs.txt').read().strip()

parts = input.split('\n\n')
ranges_text = parts[0].split('\n')
ids_text = parts[1].split('\n')

ranges = []
for line in ranges_text:
    start, end = map(int, line.split('-'))
    ranges.append((start, end))

available_ids = [int(line) for line in ids_text]

# Part 1: Count fresh IDs from available list
fresh_count = 0
for id_num in available_ids:
    is_fresh = False
    for start, end in ranges:
        if start <= id_num <= end:
            is_fresh = True
            break

    if is_fresh:
        fresh_count += 1

print("Part 1:", fresh_count)

# Part 2: Count total unique IDs considered fresh
sorted_ranges = sorted(ranges)

merged = []
for start, end in sorted_ranges:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

total_fresh = 0
for start, end in merged:
    total_fresh += end - start + 1

print("Part 2:", total_fresh)
