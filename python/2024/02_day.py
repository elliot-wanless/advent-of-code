input = open('python/2024/inputs.txt').read().splitlines()

reports = [[int(x) for x in line.split()] for line in input]

### Part 1 ###
def is_safe(levels):
    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return False
    
    delta = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    
    valid_delta = all(1 <= abs(d) <= 3 for d in delta)
    if not valid_delta:
        return False
    
    return all(d > 0 for d in delta) or all(d < 0 for d in delta)


safe_count = sum(1 for report in reports if is_safe(report))
print(f"Number of safe reports: {safe_count}")

### Part 2 ###
def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True
    
    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe(dampened_levels):
            return True
    
    return False

safe_count_dampener = sum(1 for report in reports if is_safe_with_dampener(report))
print(f"Number of safe reports with Problem Dampener: {safe_count_dampener}")
