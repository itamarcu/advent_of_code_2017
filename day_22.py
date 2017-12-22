from collections import defaultdict


def day_22():
    with open("input.txt") as file:
        lines = file.readlines()
    
    N = len(lines)
    
    def part_1():
        infecteds = set()
        for y in range(N):
            for x in range(N):
                if lines[y][x] == '#':
                    infecteds.add(x - N // 2 + (-y + N // 2) * 1j)
        
        current = 0 + 0j  # 0 in x axis and 0 in y axis
        direction = 1j  # up (1 in y axis)
        
        count = 0
        for _ in range(10000):
            if current in infecteds:
                direction *= -1j  # rotate right
                infecteds.remove(current)
            else:
                direction *= 1j  # rotate left
                infecteds.add(current)
                count += 1
            current += direction
                
        print("Part 1:", count)
    
    def part_2():
        # 0 = clean, 1 = weakened,
        # 2 = infected, 3 = flagged
        states = defaultdict(lambda: 0)
        for y in range(N):
            for x in range(N):
                if lines[y][x] == '#':
                    states[x - N // 2 + (-y + N // 2) * 1j] = 2
    
        current = 0 + 0j
        direction = 1j
    
        count = 0
        for _ in range(10000000):
            state = states[current]
            if state == 0:
                direction *= 1j  # rotate left
            elif state == 1:
                count += 1  # no rotation
            elif state == 2:
                direction *= -1j  # rotate right
            else:
                direction *= -1  # rotate 180 degrees
            if state == 3:
                del states[current]
            else:
                states[current] = (states[current] + 1) % 4  # states are only 0..3
            current += direction
    
        print("Part 2:", count)
    
    part_1()
    part_2()


day_22()
