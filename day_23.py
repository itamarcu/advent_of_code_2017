def day_23():
    with open("input.txt") as file:
        lines = file.readlines()
    
    N = 8
    
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    def part_1():
        registers = [0 for _ in range(N)]
        curr = 0
        mul_count = 0
        while 0 <= curr < len(lines):
            cmd, *args = lines[curr].strip().split(" ")
            a1 = ord(args[0]) - ord('a')
            a2 = int(args[-1]) if is_int(args[-1]) else registers[
                ord(args[-1]) - ord('a')]
            if cmd == "set":
                registers[a1] = a2
            elif cmd == "sub":
                registers[a1] -= a2
            elif cmd == "mul":
                registers[a1] *= a2
                mul_count += 1
            elif cmd == "jnz":
                if a1 < 0 or a1 >= N:
                    if is_int(args[0]) and int(
                            args[0]) != 0:  # Fucking jgz 1 3
                        curr += a2 - 1
                elif registers[a1] != 0:
                    curr += a2 - 1
            else:
                print("Error!" + cmd)
            curr += 1
        
        print("Part 1:", mul_count)  # 4225
        
    def part_2():
        # counts non=primes in the b..c (inc.) range with jumps of 17
        b = 106700
        c = 123700
        non_primes = 0
        for number in range(b, c + 1, +17):
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    non_primes += 1
                    break
        print("Part 2:", non_primes)  # 905
    
    part_1()
    part_2()


day_23()
