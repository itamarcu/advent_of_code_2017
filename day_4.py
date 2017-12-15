def day_4():
    with open("input.txt") as file:
        lines = [line.strip().split()
                 for line in file.readlines()]
    
    def part_1():
        print("Part 1:", sum(len(line) == len(set(line)) for line in lines))
    
    def part_2():
        sum2 = 0
        for line in lines:
            sum2 += 1
            seen_sorted = set()
            for word in line:
                sorted_word = "".join(sorted(list(word)))
                if sorted_word in seen_sorted:
                    sum2 -= 1
                    break
                seen_sorted.add(sorted_word)
        print("Part 2:", sum2)
    
    part_1()
    part_2()


day_4()
