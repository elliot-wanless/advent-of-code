input = open('python/2024/day_13/inputs.txt').read().splitlines()

def parse_machine(lines):
    # Parse 3 lines of input for a single machine
    a_line = lines[0].split(': ')[1]
    b_line = lines[1].split(': ')[1]
    prize_line = lines[2].split(': ')[1]
    
    # Extract X and Y movements for button A
    ax = int(a_line.split(', ')[0].split('+')[1])
    ay = int(a_line.split(', ')[1].split('+')[1])
    
    # Extract X and Y movements for button B
    bx = int(b_line.split(', ')[0].split('+')[1])
    by = int(b_line.split(', ')[1].split('+')[1])
    
    # Extract prize coordinates
    prize_x = int(prize_line.split(', ')[0].split('=')[1])
    prize_y = int(prize_line.split(', ')[1].split('=')[1])
    
    return (ax, ay), (bx, by), (prize_x, prize_y)

def find_solution(button_a, button_b, target, max_presses=100):
    ax, ay = button_a
    bx, by = button_b
    target_x, target_y = target
    
    # Try all combinations of button presses up to max_presses
    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            if (a * ax + b * bx == target_x) and (a * ay + b * by == target_y):
                return a, b
    return None

def find_solution_gcd(button_a, button_b, target):
    ax, ay = button_a
    bx, by = button_b
    target_x, target_y = target
    
    # Returns GCD and coefficients of Bézout's identity... whatever that means!
    def extended_gcd(a, b):
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1
        
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        
        return old_r, old_s, old_t

    # Find GCD and Bézout coefficients for X coordinates
    gcd_x, s1, t1 = extended_gcd(ax, bx)
    if target_x % gcd_x != 0:
        return None
    
    # Base solution for X
    s1 = s1 * (target_x // gcd_x)
    t1 = t1 * (target_x // gcd_x)
    
    # Find k_coef and k_const for Y coordinates
    k_coef = (ay*bx - by*ax) // gcd_x
    k_const = ay*s1 + by*t1 - target_y
    
    if k_coef == 0:
        return None
    
    # Solve for k
    if k_const % k_coef != 0:
        return None
        
    k = -k_const // k_coef
    
    # Calculate final A and B
    a = s1 + k * (bx // gcd_x)
    b = t1 - k * (ax // gcd_x)
    
    # Verify solution is positive and correct
    if a >= 0 and b >= 0:
        if a * ax + b * bx == target_x and a * ay + b * by == target_y:
            return a, b
            
    return None

# Split input into groups of 3 lines (plus empty line)
machines = []

# Process each machine
for i in range(0, len(input), 4):
    if i + 2 >= len(input):
        break
    machines.append(parse_machine(input[i:i+3]))

total_tokens = 0
total_tokens_2 = 0
offset = 10000000000000

# Find solutions for each machine
for button_a, button_b, target in machines:
    target_x, target_y = target
    new_target = (target_x + offset, target_y + offset)

    # Part 1
    solution = find_solution(button_a, button_b, target)
    if solution:
        a_presses, b_presses = solution
        tokens = a_presses * 3 + b_presses * 1
        total_tokens += tokens

    # Part 2
    solution_part_2 = find_solution_gcd(button_a, button_b, new_target)
    if solution_part_2:
        a_presses, b_presses = solution_part_2
        tokens = a_presses * 3 + b_presses * 1
        total_tokens_2 += tokens

print("Part 1:", total_tokens)
print("Part 2:", total_tokens_2)