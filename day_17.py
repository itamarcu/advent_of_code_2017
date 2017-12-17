def day_17():
    jump = 377
    
    def part_1():
        """Calculates regularly, but only 2017 steps so it's fast."""
        num_of_steps = 2017
        state = [0]
        curr = 0
        for i in range(1, num_of_steps + 1):
            curr = 1 + (curr + jump) % i
            state.insert(curr, i)
        
        print("Part 1:", state[(state.index(2017) + 1) % num_of_steps])  # 596

    def part_2():
        """Calculates 50 million steps but only writes into the second
        state and only if it needs to.
        Takes about 8 seconds to calculate (on my computer)."""
        num_of_steps = 50000000
        second = None
        curr = 0
        for i in range(1, num_of_steps + 1):
            curr = 1 + (curr + jump) % i
            if curr == 1:
                second = i
    
        print("Part 2:", second)  # 39051595
    
    part_1()
    part_2()


day_17()
