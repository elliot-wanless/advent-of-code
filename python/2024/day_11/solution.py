from collections import Counter

def transform_stone(stone):
    # Rule 1: If stone is 0, replace with 1
    if stone == 0:
        return [1]
    
    stone_str = str(stone)

    # Rule 2: If stone is even, split into two stones
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        return [int(stone_str[:mid]), int(stone_str[mid:])]
    
    # Rule 3: If stone is odd, multiply by 2024
    return [stone * 2024]

def simulate_blink(stone_counts):
    new_counts = Counter()

    # Transform each stone and update the count
    for stone, count in stone_counts.items():
        for new_stone in transform_stone(stone):
            new_counts[new_stone] += count
    return new_counts

def find_cycle(stones):
    seen = {}
    stone_counts = Counter(stones)
    
    # Find cycle
    for blink in range(1000):  # random big number lol
        state = tuple(sorted(stone_counts.items()))

        # Check if we've seen this state before
        if state in seen:
            cycle_start = seen[state]
            cycle_length = blink - cycle_start
            return cycle_start, cycle_length, stone_counts
        
        # Add the current state to the seen dictionary
        seen[state] = blink

        # Simulate the blink
        stone_counts = simulate_blink(stone_counts)
    
    # If no cycle is found, return None
    return None, None, stone_counts

# Read input
stones = list(map(int, open('python/2024/day_11/inputs.txt').read().split()))

# Find cycle in the sequence
cycle_start, cycle_length, current_counts = find_cycle(stones)

def get_stones_after_blinks(n):
    if cycle_start is None or n <= cycle_start:
        # Direct simulation for small numbers or when no cycle found
        counts = Counter(stones)
        for _ in range(n):
            counts = simulate_blink(counts)
        return sum(counts.values())
    
    # Calculate using cycle
    remaining_blinks = (n - cycle_start) % cycle_length
    counts = current_counts
    for _ in range(remaining_blinks):
        counts = simulate_blink(counts)
    return sum(counts.values())

print("Part 1:", get_stones_after_blinks(25))
print("Part 2:", get_stones_after_blinks(75))