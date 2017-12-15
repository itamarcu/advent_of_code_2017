def day_8():
    maximum = 0
    regs = dict()
    lines = [line.split() for line in open('input.txt', 'r').readlines()]
    for line in lines:
        regs[line[0]] = 0
    for line in lines:
        for i in {4, 6}:
            try:
                line[i] = str(int(line[i]))
            except ValueError:
                line[i] = regs[line[i]]
        
        cond = eval(" ".join(line[4:7]))
        if cond:
            amount = int(line[2]) * (1 if line[1] == "inc" else -1)
            regs[line[0]] += amount
            maximum = max(maximum, regs[line[0]])
    
    print("Part 1:", max(regs.values()))
    print("Part 2:", maximum)


day_8()


def day_8_old():
    maximum = 0
    lines = [line.split() for line in open('input.txt', 'r').readlines()]
    for line in lines:
        locals()[line[0]] = 0
    for line in lines:
        cond = eval(" ".join(line[4:7]))
        if cond:
            amount = int(line[2]) * (1 if line[1] == "inc" else -1)
            current = locals()[line[0]]
            locals()[line[0]] += amount
            maximum = max(maximum, locals()[line[0]])
    loc = dict(locals())
    loc.pop("maximum")
    print("Part 1:", max([loc[x] for x in loc if isinstance(loc[x], int)]))
    print("Part 2:", maximum)