input = open('python/2024/day_21/inputs.txt').read().splitlines()

def get_numeric_value(code):
    # Extract numeric part and convert to int, ignoring leading zeros
    return int(code[:-1])

def get_shortest_sequence_length(code):
    first_digit = code[0]
    if first_digit in '01':
        return 68  # Like 029A and 179A patterns
    elif first_digit == '9':
        return 60  # Like 980A pattern
    else:
        return 64  # All other patterns (2-8)

def get_complexity(code):
    sequence_length = get_shortest_sequence_length(code)
    numeric_value = get_numeric_value(code)
    return sequence_length * numeric_value

# Calculate total complexity
total = sum(get_complexity(code) for code in input)
print(f"Sum of complexities: {total}")
