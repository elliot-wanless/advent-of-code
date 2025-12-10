input = open('python/2024/day_19/inputs.txt').read().splitlines()

def parse_input(lines):
    patterns, designs = [], []
    parsing_patterns = True
    
    for line in lines:
        if not line:
            parsing_patterns = False
            continue
            
        if parsing_patterns:
            patterns.extend(p.strip() for p in line.split(','))
        else:
            designs.append(line.strip())
            
    return patterns, designs

def solve_design(design, patterns, count_ways=False, memo=None):
    if memo is None:
        memo = {}
        
    if not design:
        return 1 if count_ways else True
        
    if design in memo:
        return memo[design]
    
    result = 0 if count_ways else False
    
    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern):]
            sub_result = solve_design(remaining, patterns, count_ways, memo)
            
            if count_ways:
                result += sub_result
            elif sub_result:
                result = True
                break
                
    memo[design] = result
    return result

patterns, designs = parse_input(input)

### Part 1 ###  
possible_count = sum(1 for design in designs if solve_design(design, patterns))
print("Part 1:", possible_count)

### Part 2 ###
total_ways = sum(solve_design(design, patterns, count_ways=True) for design in designs if solve_design(design, patterns))
print("Part 2:", total_ways)
