from collections import defaultdict


def day_25():
    input_bettered = "" \
                     + "  A 1 R B 0 L C  " \
                     + "  B 1 L A 1 L D  " \
                     + "  C 1 R D 0 R C  " \
                     + "  D 0 L B 0 R E  " \
                     + "  E 1 R C 1 L F  " \
                     + "  F 1 L E 1 R A  "
    lines = input_bettered.split("   ")
    start_state = 0
    steps_to_take = 12656374
    moves = dict()
    
    def to_int(character):
        return ord(character) - ord('A')
    
    for line in lines:
        #  F : 1 L E / 1 R A
        s, w1, d1, s1, w2, d2, s2 = line.strip().split(" ")
        moves[(to_int(s), 0)] = (
            int(w1), +1 if d1 == 'R' else -1, to_int(s1))
        moves[(to_int(s), 1)] = (
            int(w2), +1 if d2 == 'R' else -1, to_int(s2))
    
    def part_1():
        position = 0
        state = start_state
        tape = defaultdict(int)
        for _ in range(steps_to_take):
            w, d, s = moves[(state, tape[position])]
            if w == 1:
                tape[position] = w
            else:
                del (tape[position])
            position += d
            state = s
        print("Part 1:", len(tape))
    
    def part_2():
        pass
    
    part_1()
    part_2()


day_25()
