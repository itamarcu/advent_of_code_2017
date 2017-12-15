with open("input.txt") as file:
    lines = [[int(x) for x in line.strip().split()]
             for line in file.readlines()]


def day_2():
    print("Part 1:", sum(max(line) - min(line) for line in lines))
    
    def line_checksum(line):
        N = len(line)
        for i in range(N):
            for j in range(N):
                if i != j and line[i] % line[j] == 0:
                    return line[i] // line[j]
    
    print("Part 2:", sum(line_checksum(line) for line in lines))


day_2()
