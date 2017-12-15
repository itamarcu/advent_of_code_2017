def day_15():
    def part_1():
        """Takes about 30 seconds to run."""
        gen_1 = 883
        gen_2 = 879
        count = 0
        for _ in range(40000000):
            if (gen_1 & 0xFFFF) == (gen_2 & 0xFFFF):
                count += 1
            gen_1 = (gen_1 * 16807) % 2147483647
            gen_2 = (gen_2 * 48271) % 2147483647
        print(count)
    
    def part_2():
        """Takes about 15 seconds to run."""
        gen_1 = 883
        gen_2 = 879
        count = 0
        for _ in range(5000000):
            while (gen_1 & (4-1)) != 0:
                gen_1 = (gen_1 * 16807) % 2147483647
            while (gen_2 & (8-1)) != 0:
                gen_2 = (gen_2 * 48271) % 2147483647
            if (gen_1 & 0xFFFF) == (gen_2 & 0xFFFF):
                count += 1
            gen_1 = (gen_1 * 16807) % 2147483647
            gen_2 = (gen_2 * 48271) % 2147483647
        print(count)

    part_1()
    part_2()


day_15()