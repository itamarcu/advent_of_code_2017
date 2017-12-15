def day_5():
    with open("input.txt") as file:
        lines = [int(line.strip()) for line in file.readlines()]
    
    def part_1():
        jumps = lines.copy()
        current = 0
        steps_amount = 0
        N = len(jumps)
        while 0 <= current < N:
            j = jumps[current]
            jumps[current] += 1
            current += j
            steps_amount += 1
        
        print("part 1", steps_amount)
    
    def part_2():
        jumps = lines.copy()
        current = 0
        steps_amount = 0
        N = len(jumps)
        while 0 <= current < N:
            j = jumps[current]
            jumps[current] += (1 if j < 3 else -1)
            current += j
            steps_amount += 1
        
        print("part 2", steps_amount)
    
    part_1()
    part_2()


day_5()
