input = open('python/2024/inputs.txt').read().splitlines()

reports = [[int(x) for x in line.split()] for line in input]

### Part 1 ###
def is_safe(levels):
    # Check if the levels are strictly increasing or decreasing
    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return False
    
    # Calculate the delta between each level
    delta = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    
    # Check if the delta is between 1 and 3
    valid_delta = all(1 <= abs(d) <= 3 for d in delta)
    
    # If the delta is not valid, the report is not safe
    if not valid_delta:
        return False
    
    # Check if the delta is strictly increasing or decreasing
    return all(d > 0 for d in delta) or all(d < 0 for d in delta)

# Count the number of safe reports
safe_count = sum(1 for report in reports if is_safe(report))
print(f"Number of safe reports: {safe_count}")

### Part 2 ###
def is_safe_with_dampener(levels):
    # If the report is already safe, return True
    if is_safe(levels):
        return True
    
    # Try removing each level one by one and check if the report is safe
    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe(dampened_levels):
            return True
    
    # If no dampened report is safe, the original report is not safe
    return False


# Count the number of safe reports with the dampener
safe_count_dampener = sum(1 for report in reports if is_safe_with_dampener(report))
print(f"Number of safe reports with Problem Dampener: {safe_count_dampener}")
