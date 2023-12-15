input = open('python/inputs.txt').read()

total = 0
boxes = [[] for _ in range(256)]
focal_lengths = {}

# Find the ASCII, multiply by 17, mod 256
def hash(sequence):
    current_total = 0
    for ch in sequence:
        current_total += ord(ch)
        current_total *= 17
        current_total %= 256

    return current_total

# For each sequence in the input, add/remove from the box
for sequence in input.split(","):
    # If "=", add to the right box (using label as box index)
    if "=" in sequence:
        label, length = sequence.split("=")
        length = int(length)
        index = hash(label)
        # Store the focal length for the calculation later
        focal_lengths[label] = length
        if label not in boxes[index]:
            boxes[index].append(label)
    # If "-", add to the right box (using label as box index)
    if "-" in sequence:
        label = sequence[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)

# For each box, add the total up!
for i, box in enumerate(boxes):
    for j, label in enumerate(box):
        total += (i+1) * (j+1) * focal_lengths[label]

print(total)
