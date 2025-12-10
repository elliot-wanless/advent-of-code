input_lines = open('python/2025/day_06/inputs.txt').read().splitlines()

max_width = max(len(line) for line in input_lines)
lines = [line.ljust(max_width) for line in input_lines]

non_empty_cols = []
for col_idx in range(max_width):
    col_chars = [line[col_idx] for line in lines]
    if any(c != ' ' for c in col_chars):
        non_empty_cols.append(col_idx)

problems = []
if non_empty_cols:
    current = [non_empty_cols[0]]
    for col_idx in non_empty_cols[1:]:
        if col_idx == current[-1] + 1:
            current.append(col_idx)
        else:
            problems.append(current)
            current = [col_idx]
    if current:
        problems.append(current)

grand_total = 0
for prob_cols in problems:
    prob_lines = []
    for line in lines:
        prob_line = ''.join(line[c] for c in prob_cols).strip()
        if prob_line:
            prob_lines.append(prob_line)

    numbers = []
    operator = None

    for pl in prob_lines:
        if pl in ['+', '*']:
            operator = pl
        else:
            try:
                numbers.append(int(pl))
            except:
                pass

    if operator == '+':
        result = sum(numbers)
    elif operator == '*':
        result = 1
        for n in numbers:
            result *= n
    else:
        result = 0

    grand_total += result

print("Part 1:", grand_total)

# Part 2: Read problems right-to-left
grand_total_part2 = 0

for prob_cols in problems:
    prob_cols_rtl = prob_cols[::-1]

    numbers = []
    operator = None

    for col_idx in prob_cols_rtl:
        col_chars = [line[col_idx] for line in lines]

        digit_str = ''.join(c for c in col_chars if c.isdigit())

        for c in col_chars:
            if c in ['+', '*']:
                operator = c
                break

        if digit_str:
            numbers.append(int(digit_str))

    if operator == '+':
        result = sum(numbers)
    elif operator == '*':
        result = 1
        for n in numbers:
            result *= n
    else:
        result = 0

    grand_total_part2 += result

print("Part 2:", grand_total_part2)
