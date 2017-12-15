with open("input.txt") as file:
    line = [int(x) for x in list(file.readline().strip())]


def day_1():
    N = len(line)
    print("Part 1:",
          sum(line[i] for i in range(N) if line[i] == line[(i + 1) % N]))
    print("Part 1:",
          sum(line[i] for i in range(N) if line[i] == line[(i + N//2) % N]))


day_1()
