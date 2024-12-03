import re

input = open('python/2024/inputs.txt').read()

pattern = r'(mul)\((\d+),(\d+)\)'

# this took far too long to figure out 😅
enable_pattern = r"^([^d]|d(?!on't\(\)))*(?=don't\(\)|$)|(?:do\(\))+([^d]|d(?!on't\(\)))*(?=don't\(\)|$)"

def parse_instructions(data):
    instructions = []
    total = 0

    instructions.extend(re.findall(pattern, data))

    for instruction in instructions:
        total += int(instruction[1]) * int(instruction[2])
    return total

### Part 1 ###
print("Part 1: ", parse_instructions(input))

### Part 2 ###
enabled_input = []
matches = re.finditer(enable_pattern, input)

for match in matches:
    enabled_input.append(match.group(0))

print("Part 2: ", parse_instructions(''.join(enabled_input)))