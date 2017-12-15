def day_14():
    def knot_hash(string):
        string = list(map(ord, string))
        string += [17, 31, 73, 47, 23]
        
        size = 256
        numbers = list(range(size))
        skip = 0
        curr = 0
        for _ in range(64):
            for length in string:
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
        
        final_nums = "".join("{:08b}".format(num) for num in final_nums)
        return final_nums
    
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    input_str = lines[0]
    
    count = 0
    for i in range(128):
        count += sum(map(int, knot_hash(input_str + "-" + str(i))))
    
    print("Part 1:" + count)
    
    grid = []
    for i in range(128):
        grid.append(list(map(int, list(knot_hash(input_str + "-" + str(i))))))
    
    def fill(grid, x, y, char):
        if x < 0 or y < 0 or x >= 128 or y >= 128:
            return
        if grid[x][y] != 1:
            return
        grid[x][y] = char
        fill(grid, x, y + 1, char)
        fill(grid, x + 1, y, char)
        fill(grid, x, y - 1, char)
        fill(grid, x - 1, y, char)
    
    group_count = 0
    for y in range(128):
        for x in range(128):
            if grid[x][y] == 1:
                group_count += 1
                fill(grid, x, y, str(group_count))
    
    print("Part 2:" + group_count)


day_14()
