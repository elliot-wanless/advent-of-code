from itertools import permutations

input = open('python/2024/day_05/inputs.txt').read().split('\n\n')

rules, updates = input[0].splitlines(), input[1].splitlines()

rules_dict = {}
incorrect_updates = []

# Create rules dictionary
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
    status = True
    # For each number in the update
    for index, number in enumerate(update):
        # If the number has a rule, apply the rule
        if number in rules_dict:
            # Check each rule that the number has
            for rule in rules_dict[number]:
                # Check the rule is in the update and the index is greater than the current index
                if rule in update and update.index(rule) < index:
                    status = False

    if status:
        # print(update)
        total += int(update[len(update)//2])
    else:
        incorrect_updates.append(update)

print("Part 1:", total)

### Part 2 ###
def find_valid_order(numbers, rules_dict):
    # Track which numbers we've placed
    used_nums = set()
    result = []
    while len(result) < len(numbers):
        # Try to find a number we can add
        for num in numbers:
            if num in used_nums:
                continue
                
            # Check if all required numbers are already used
            can_use = True
            if num in rules_dict:
                for required in rules_dict[num]:
                    if required in numbers and required not in used_nums:
                        can_use = False
                        break
            
            if can_use:
                result.append(num)
                used_nums.add(num)
                break
        else:
            # If we couldn't add any number, no valid order exists
            return None
    
    return result

total = 0
for update in incorrect_updates:
    valid_order = find_valid_order(update, rules_dict)
    if valid_order:
        total += int(valid_order[len(valid_order)//2])

print("Part 2:", total)
