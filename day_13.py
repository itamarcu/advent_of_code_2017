def day_13():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    
    # input setup
    N = int(lines[-1].split()[0][:-1]) + 1  # number of walls
    
    depths = [0 for _ in range(N)]
    for line in lines:
        index, depth = map(int, line.strip().split(": "))
        depths[index] = int(depth)
    
    # Part 1
    sum_cost = 0
    for beat in range(N):
        depth = depths[beat]
        if depth == 0:
            continue
        if (beat % (2 * depth - 2)) == 0:
            sum_cost += beat * depth
    print("Cost of travel:", sum_cost)
    
    # Part 2
    start_delay = 0
    while True:
        for beat in range(N):
            depth = depths[beat]
            if depth == 0:
                continue
            if ((beat + start_delay) % (depth * 2 - 2)) == 0:
                break
        else:  # if not broken during loop
            print("Delay needed:", start_delay)
            break
        start_delay += 1


day_13()
