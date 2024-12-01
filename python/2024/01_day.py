input = open('python/2024/inputs.txt').read().splitlines()

list1, list2 = [], []

for line in input:
    left, right = [int(x) for x in line.split()]
    list1.append(left)
    list2.append(right)


### Part 1 ###
total = 0
list1.sort()
list2.sort()

total = sum(abs(a - b) for a, b in zip(list1, list2))
print("Part 1:", total)

### Part 2 ###
total = 0
cache = {}

for number in list1:
    if number in cache:
        total += cache[number]
    else:
        counts = 0
        for x in list2:
            if x == number:
                counts += 1
        if counts > 0: 
            cache[number] = number*counts
            total += cache[number]

print("Part 2:", total)