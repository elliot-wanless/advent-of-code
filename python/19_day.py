workflows_input, parts_input = map(str.splitlines, open('python/inputs.txt').read().split("\n\n"))
workflows = {}
total = 0

def check_workflow(parts, workflow):
    # Check each rule in order and return the location if it matches
    for rule in workflow[0]:
        category, comparator, rest = rule[0], rule[1], rule[2:]
        number, location = rest.split(":")
        number = int(number)
        
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