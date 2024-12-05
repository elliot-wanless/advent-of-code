from itertools import permutations

input = open('python/2024/day_05/inputs.txt').read().split('\n\n')

rules, updates = input[0].splitlines(), input[1].splitlines()

rules_dict = {}
incorrect_updates = []

# Create rules dictionary where  {left-value: [all required rules/right-values]}
for rule in rules:
    a, b = rule.split('|')
    if a not in rules_dict:
        rules_dict[a] = [b]
    else:
        rules_dict[a].append(b)

total = 0

### Part 1 ###
for update in updates:
    update = update.split(',')
    valid = True
    # For each number in the update
    for index, number in enumerate(update):
        if number not in rules_dict:
            continue
        # Check each rule that the current number has
        for rule in rules_dict[number]:
            # If the rule is in the update and the index is greater than the current index, the update is invalid
            if rule in update and update.index(rule) < index:
                valid = False
                break

    # If the update is invalid, add it to the list for part 2
    if not valid:
        incorrect_updates.append(update)
        continue

    # Add the middle number to the total
    total += int(update[len(update)//2])

print("Part 1:", total)

### Part 2 ###
def find_valid_order(numbers):
    used_nums = set()
    result = []

    while len(result) < len(numbers):
        # Go through the number list
        for num in numbers:
            # If the number has already been used, skip it
            if num in used_nums:
                continue
            
            # Check if all required numbers are already used
            can_use = True
            if num in rules_dict:
                for required in rules_dict[num]:
                    if required in numbers and required not in used_nums:
                        can_use = False
                        break
            
            # If we can use the number, add it to the result and mark it as used
            if can_use:
                result.append(num)
                used_nums.add(num)
                break
        
        # If we couldn't add any number, no valid order exists
        else:
            return None
    
    return result

total = 0
for update in incorrect_updates:
    valid_update = find_valid_order(update)
    if valid_update:
        total += int(valid_update[len(valid_update)//2])

print("Part 2:", total)
