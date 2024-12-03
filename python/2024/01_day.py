input = open('python/2024/inputs.txt').read().splitlines()

list1, list2 = [], []

for line in input:
    left, right = [int(x) for x in line.split()]
    list1.append(left)
    list2.append(right)

### Part 1 ###
list1.sort()
list2.sort()

# Calculate the total by summing the absolute differences between the lists
total = sum(abs(a - b) for a, b in zip(list1, list2))
print("Part 1:", total)

### Part 2 ###
# Count the occurrences of each number in list2
counts = {}
for x in list2:
    counts[x] = counts.get(x, 0) + 1

total = 0
cache = {}

# Calculate the total by summing the product of each number in list1 and its count in list2
for number in list1:
    if number in cache:
        total += cache[number]
        continue
    
    # If the number is in list2, calculate the product and add it to the cache and total
    if number in counts:
        cache[number] = number * counts[number]
        total += cache[number]

print("Part 2:", total)