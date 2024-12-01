import time

input = open('python/2023/inputs.txt').read().splitlines()

spring_map = [[item for item in line.split(' ')] for line in input]
memo = {}

BROKEN_SPRING = '#'
GOOD_SPRING = '.'
ANY_SPRING = '?'
expansion = 5

def unfold(config, condition):
    # Expand config
    config = config + ((ANY_SPRING + config) * (expansion-1))
    # Expand condition and cast to integers
    condition = [int(item) for item in condition*expansion]

    return config, condition

def get_arrangements(config, condition):
    # Memoization for Part 2
    # Check if we've already calculated this
    if (config, tuple(condition)) in memo:
        return memo[(config, tuple(condition))]

    result = 0

    # At the end of config, make sure we used all the conditions
    if not config:
        if not condition: 
            return 1
        return 0
    
    # If no more conditions and there are no more broken springs
    if not condition:
        if BROKEN_SPRING in config: 
            return 0
        return 1
    
    # If spring isn't broken, keep counting
    if config[0] == GOOD_SPRING or config[0] == ANY_SPRING:
        result += get_arrangements(config[1:], condition)
    
    # If spring is broken or 'potentially' broken
    if config[0] == BROKEN_SPRING or config[0] == ANY_SPRING:
        # Check index isn't out of bounds and there are no 'good' springs to the left
        if condition[0] <= len(config) and GOOD_SPRING not in config[:condition[0]]:
            # If the number of conditions is the same as what's left of the config
            # And the spring at that index isn't broken, keep counting
            if (condition[0] == len(config) or config[condition[0]] != BROKEN_SPRING):
                result += get_arrangements(config[condition[0] + 1:], condition[1:])

    # Memoization for Part 2
    memo[(config, tuple(condition))] = result
    return result

total = 0

start = time.time()
for line in input:
    config, condition = line.split(' ')
    condition = condition.split(',')

    # Expand the config and condition for Part 2
    unfolded = unfold(config, condition)

    # Add the number of arrangements to the total
    total += get_arrangements(*unfolded)
end = time.time()

print("Time:", end - start)
print("Total:", total)
    
