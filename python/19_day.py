workflows_input, parts_input = map(str.splitlines, open('python/inputs.txt').read().split("\n\n"))
workflows = {}
total = 0

def parse_rule(rule):
    category, comparator, rest = rule[0], rule[1], rule[2:]
    number, location = rest.split(":")
    number = int(number)

    return category, comparator, number, location

def check_workflow(parts, workflow):
    # Check each rule in order and return the location if it matches
    for rule in workflow[0]:
        category, comparator, number, location = parse_rule(rule)
        
        # Get part from parts mapping
        part = parts[category]

        # Check comparator and numbers
        if comparator == "<" and part < number:
            return location
        elif comparator == ">" and part > number:
            return location
        
    return workflow[1]

for workflow in workflows_input:
    name, rules = workflow.split("{")
    rules = rules[:-1].split(",")

    # Set the workflow as the key, with rules and default destination as the value
    workflows[name] = (rules[:-1], rules[-1])

for part in parts_input:
    parts = {}
    part = part[1:-1].split(",")

    # Get the value for each parts category
    for category in part:
        cat, number = category.split("=")
        parts[cat] = int(number)
    
    # Set the default location to "in"
    location = "in"

    # Check the workflows until they are accepted or rejected
    while(location != "A" and location != "R"):
        workflow = workflows[location]
        location = check_workflow(parts, workflow)
    
    # Sum up all accepted parts values
    if location == "A":
        total += sum(parts.values())

    
print(total)

def find_limits(ranges, category):
    # If the category is "A", return the total number of possible values
    if category == "A":
        count = 1
        for low, high in ranges.values():
            count *= high - low + 1
        return count

    # If the category is "R", return nothing because we don't care about rejected values
    if category == "R":
        return 0
    
    # Get the list of rules and the default destination
    rules, default = workflows[category]
    total = 0

    for rule in rules:
        category, comparator, number, location = parse_rule(rule)
        # Get the low and high values for the category (e.g. "x", "m", "a", "s")
        low, high = ranges[category]

        # We want to reduce the range down into halves based on the comparator
        match comparator:
            case "<":
                lower_half = (number, high)
                upper_half = (low, number - 1)
            case ">":
                lower_half = (low, number)
                upper_half = (number + 1, high)

        # Using the lower and upper ranges of the halves, we can reduce the range of the category
        # If the range is valid, we can set the new range and continue reducing
        if lower_half[1] > lower_half[0]:
            ranges[category] = lower_half
        if upper_half[1] > upper_half[0]:
            new_ranges = ranges.copy()
            new_ranges[category] = upper_half
            total += find_limits(new_ranges, location)
    else:
        # If we have reduced the range as much as possible, we can check the default destination
        total += find_limits(ranges, default)
            
    return total

# Set the ranges for each category
category_ranges = {}
for key in "xmas":
    category_ranges[key] = (1, 4000)

print(find_limits(category_ranges, "in"))