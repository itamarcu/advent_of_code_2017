def day_6():
    with open("input.txt") as file:
        line = [int(x) for x in file.readline().split()]
    
    blocks = line.copy()
    N = len(blocks)
    steps_amount = 0
    seen = set()
    
    while tuple(blocks) not in seen:
        seen.add(tuple(blocks))
        taken = max(blocks)
        largest_index = blocks.index(taken)
        blocks[largest_index] = 0
        for i in range(1, taken + 1):
            blocks[(largest_index + i) % N] += 1
        steps_amount += 1
    print("part 1", steps_amount)

    steps_up_to_loop = 0
    loop_start = tuple(blocks)
    blocks = line.copy()
    while tuple(blocks) != loop_start:
        taken = max(blocks)
        largest_index = blocks.index(taken)
        blocks[largest_index] = 0
        for i in range(1, taken + 1):
            blocks[(largest_index + i) % N] += 1
        steps_up_to_loop += 1
    
    print("part 2", steps_amount - steps_up_to_loop)


day_6()
