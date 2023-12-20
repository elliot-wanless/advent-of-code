input =  open('python/inputs.txt').read().splitlines()

modules, conjunctions, pulses = dict(), dict(), list()
LOW, HIGH = "LOW", "HIGH"
totals = {LOW: 0, HIGH: 0}

for line in input:
    line = line.split(" -> ")
    # If a broadcast or output module, parse it. Otherwise, parse it but differently 😆
    if line[0][0] not in "%&":
        modules[line[0]] = ("", line[1].split(", "), False)
    else:
        modules[line[0][1:]] = (line[0][:1], line[1].split(", "), False)
    
# For each conjunction module, find it's connections and put them in a dict
for module, (module_type, destinations, module_status) in modules.items():
    if module_type == "&":
        conjunctions[module] = dict()
        for other_mods, (_, destinations, _) in modules.items():
            if module in destinations:
                conjunctions[module][other_mods] = LOW


for i in range(1000):
    # Start with the button press
    pulses.append(("broadcaster", LOW, "button"))

    # FIFO the queue of pulses
    while pulses:
        # Get the next pulse and fund the module it relates to
        module, pulse_type, parent_module = pulses.pop(0)
        module_type, destinations, module_status = modules.get(module, ("", "", ""))
        print(parent_module, "-"+pulse_type+"->", module, module_type, destinations, module_status)

        # Part 2... yeah right, I'll be here for years
        if module == "rx" and pulse_type == LOW:
            print("Done in:", i, "button presses")
            break
        
        # Increment the totals
        totals[pulse_type] += 1

        # If a flip-flop, only pulse when receiving a LOW pulse and toggle each time
        if module_type == "%":
            if pulse_type == LOW:
                for destination in destinations:
                    pulses.append((destination, HIGH if not module_status else LOW, module))
                modules[module] = (module_type, destinations, not module_status)
        
        # If a conjunction, only pulse when all inputs are HIGH
        elif module_type == "&":
            # And store the most recent pulse from connected modules
            conjunctions[module][parent_module] = pulse_type
            for destination in destinations:
                pulses.append((destination, LOW if all(value == HIGH for value in conjunctions[module].values()) else HIGH, module))

        # If a broadcast, pulse all connected modules by default
        else:
            for destination in destinations:
                pulses.append((destination, pulse_type, module))



print(totals[LOW]*totals[HIGH])