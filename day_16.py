def day_16():
    with open("input.txt") as file:
        line = file.readline()
        moves = line.strip().split(",")
    
    N = 16
    
    def part_1():
        dance = list("abcdefghijklmnop")
        for move in moves:
            move_type = move[0]
            if move_type == "s":
                arg = int(move[1:])
                dance = dance[N - arg:] + dance[:N - arg]
            elif move_type == "x":
                i0, i1 = list(map(int, move[1:].split("/")))
                dance[i0], dance[i1] = dance[i1], dance[i0]
            elif move_type == "p":
                args = move[1:].split("/")
                i0, i1 = dance.index(args[0]), dance.index(args[1])
                dance[i0], dance[i1] = dance[i1], dance[i0]
        
        print("Part 1:", "".join(dance))
    
    def part_2():
        ONE_BILLION = 1000000000
        dance = list("abcdefghijklmnop")
        seen = list()
        for i in range(ONE_BILLION):
            if "".join(dance) in seen:
                answer = seen[ONE_BILLION % i]
                print("Part 2:", "".join(answer))
                return
            seen.append("".join(dance))
            
            for move in moves:
                move_type = move[0]
                if move_type == "s":
                    arg = int(move[1:])
                    dance = dance[N - arg:] + dance[:N - arg]
                elif move_type == "x":
                    i0, i1 = list(map(int, move[1:].split("/")))
                    dance[i0], dance[i1] = dance[i1], dance[i0]
                elif move_type == "p":
                    args = move[1:].split("/")
                    i0, i1 = dance.index(args[0]), dance.index(args[1])
                    dance[i0], dance[i1] = dance[i1], dance[i0]

        print("Part 2:", "".join(dance))
    
    part_1()
    part_2()


day_16()
