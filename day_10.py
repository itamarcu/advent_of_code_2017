def day_10_1():
    with open('input.txt') as input_file:
        line = map(int, input_file.readline().split(","))
    
    size = 256
    numbers = list(range(size))
    skip = 0
    curr = 0
    for length in line:
        next = curr + length
        if next >= size:
            numbers *= 2  # concat list to itself
            numbers[curr:next] = reversed(numbers[curr:next])
            numbers = numbers[size:next] + numbers[next - size:curr] \
                      + numbers[curr:size]
        else:
            numbers[curr:next] = reversed(numbers[curr:next])
        curr = (next + skip) % size
        skip += 1
    print(numbers[0] * numbers[1])
    return


def day_10_2():
    with open('input.txt') as input_file:
        line = list(map(ord, list(input_file.readline())))
    line += [17, 31, 73, 47, 23]
    
    size = 256
    numbers = list(range(size))
    skip = 0
    curr = 0
    for _ in range(64):
        for length in line:
            next = curr + length
            if next >= size:
                numbers *= 2  # concat list to itself
                numbers[curr:next] = reversed(numbers[curr:next])
                numbers = numbers[size:next] + numbers[next - size:curr] \
                          + numbers[curr:size]
            else:
                numbers[curr:next] = reversed(numbers[curr:next])
            curr = (next + skip) % size
            skip += 1
    
    final_nums = []
    for i in range(16):
        s = 0
        for j in range(16):
            s ^= numbers[i * 16 + j]
        final_nums.append(s)
    
    final_nums = "".join("%02x" % num for num in final_nums)
    print(final_nums)
    return

day_10_2()