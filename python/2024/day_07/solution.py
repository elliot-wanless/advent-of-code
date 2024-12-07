input = open('python/2024/day_07/inputs.txt').read().splitlines()

p1_count, p2_count = 0, 0

def calculate(numbers, total, running_total, with_concat):
    if len(numbers) == 1:
        # For single numbers, we can try addition, multiplication, or concatenation
        if running_total + numbers[0] == total or running_total * numbers[0] == total or (with_concat and int(str(running_total) + str(numbers[0])) == total):
            return True
        return False

    # Try concatenation
    if with_concat and calculate(numbers[1:], total, int(str(running_total) + str(numbers[0])), with_concat):
        return True
    
    # Try addition
    if calculate(numbers[1:], total, running_total + numbers[0], with_concat):
        return True
        
    # Try multiplication 
    if calculate(numbers[1:], total, running_total * numbers[0], with_concat):
        return True
        
    return False

for line in input:
    total, rest = line.split(':')
    total, numbers = int(total), list(map(int, rest.split()))

    # Start iterating through all possible variations of the numbers
    p1_valid = calculate(numbers, total, 0, False)
    p2_valid = calculate(numbers, total, 0, True)

    # If valid, add to the count
    if p1_valid: p1_count += total
    if p2_valid: p2_count += total

print("Part 1: ", p1_count)
print("Part 2: ", p2_count)

