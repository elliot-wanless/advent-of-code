import re

input = open('python/2024/day_03/inputs.txt').read()

pattern = r'(mul)\((\d+),(\d+)\)'

# this took far too long to figure out 😅
enable_pattern = r"^([^d]|d(?!on't\(\)))*(?=don't\(\)|$)|(?:do\(\))+([^d]|d(?!on't\(\)))*(?=don't\(\)|$)"

def parse_instructions(data):
    # Find all instructions that match the pattern
    instructions = re.findall(pattern, data)

    # Calculate the total by multiplying the numbers and summing them up
    total = sum(int(x) * int(y) for _, x, y in instructions)

    return total

print("Part 1: ", parse_instructions(input))

# Find all enabled instructions using my immaculately crafted regex
enabled_input = [match.group(0) for match in re.finditer(enable_pattern, input)]

# Join the enabled instructions into a string
enabled_string = ''.join(enabled_input)
print("Part 2: ", parse_instructions(enabled_string))
