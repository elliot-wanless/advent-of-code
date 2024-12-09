from collections import deque
import time

input = open('python/2024/day_09/inputs.txt').read()

def is_even(n):
    return n % 2 == 0

def get_file_blocks():
    queue = deque(input)
    p1 = 0
    file_blocks = deque()
    max_file, min_file = len(input) // 2, 0

    while queue:
        current_char = int(queue.popleft())
        # Use it if it's 'even' (not a '.')
        if is_even(p1):
            file_blocks.extend([min_file] * current_char)
            min_file += 1
        # Add a '.' if it's odd (a gap)
        else:
            file_blocks.extend(['.'] * current_char)
            max_file -= 1
        p1 += 1

    return file_blocks, len(file_blocks)

### Part 1 ###
def part_1():
    file_blocks, length = get_file_blocks()
    p1, p2 = 0, length-1

    while p1 < p2:
        if file_blocks[p1] == '.':
            # Find next non-gap file from the end
            while p2 > p1 and file_blocks[p2] == '.':
                p2 -= 1
                
            if p2 > p1:
                # Move file to gap
                file_blocks[p1] = file_blocks[p2]
                file_blocks[p2] = '.'
                p2 -= 1
        p1 += 1

    total = sum(i*int(file_blocks[i]) for i in range(len(file_blocks)) if file_blocks[i] != '.')
    print("Part 1: ", total)

part_1()

### Part 2 ###
def part_2():
    
    file_blocks, length = get_file_blocks()
    p1, p2 = 0, length-1
    
    file_blocks = list(file_blocks)

    while p2 > 1:
        if file_blocks[p2] != '.':
            rabbit = p2 - 1
            while rabbit > 1 and file_blocks[rabbit] == file_blocks[p2]:
                rabbit -= 1

            # Find how far the rabbit went
            diff = p2 - rabbit
            nums_to_move = file_blocks[p2-diff+1:p2+1]
            amount_to_move = len(nums_to_move)

            # Don't move blocks past where they currently are
            target_index = p2 - diff

            for i in range(len(file_blocks) - amount_to_move + 1):
                # Check if the slice is all dots and within bounds
                if i < target_index and set(file_blocks[i:i + amount_to_move]) == {'.'}:
                    # Move the blocks
                    file_blocks[i:i + amount_to_move] = nums_to_move
                    file_blocks[p2 - amount_to_move + 1:p2 + 1] = ['.'] * amount_to_move
                    break
            p2 = p2-diff
        else:
            p2 -= 1

    total = sum(i*int(file_blocks[i]) for i in range(len(file_blocks)) if file_blocks[i] != '.')
    print("Part 2: ", total)

start_time = time.time()
part_2()
end_time = time.time()
print(f"Time taken for Part 2: {end_time - start_time} seconds")


