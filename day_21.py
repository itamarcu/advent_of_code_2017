from numpy import *


def day_21():
    with open("input.txt") as file:
        lines = file.readlines()
    # .#./###/.#. => #..#/.###/..#./.##.
    # ##/#. => .#./.../...
    rules = dict()
    for line in lines:
        rule = [[list(p) for p in part.split("/")] for part in
                line.strip().split(" => ")]
        mats = [asmatrix(array(rulepart)) for rulepart in rule]
        for j in range(4):
            rules[rot90(mats[0], j, (0, 1))] = mats[1]
            rules[rot90(flip(mats[0], 0), j, (0, 1))] = mats[1]
    
    def part_1():
        mat = asmatrix(array([list(".#."), list("..#"), list("###")]))
        n = 3
        for _ in range(5):
            if n % 2 == 0:
                newmat_arr = [[None for _ in range(n//2)] for _ in range(n//2)]
                for x in range(0, n, 2):
                    for y in range(0, n, 2):
                        submat = mat[y:y+2][x:x+2]
                        newmat_arr[x//2][y//2] = rules[submat]
        print(mat.flatten())
        pass
    
    def part_2():
        pass
    
    part_1()
    part_2()


day_21()
