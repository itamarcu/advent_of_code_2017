from numpy import *


def day_21():
    with open("input.txt") as file:
        lines = file.readlines()

    def tup(matrix_2d):
        return tuple(map(tuple, matrix_2d))
    def untup(tup_2d):
        return asmatrix(array(tup_2d))
    # .#./###/.#. => #..#/.###/..#./.##.
    # ##/#. => .#./.../...
    rules = dict()
    for line in lines:
        rule = [[list(p) for p in part.split("/")] for part in
                line.strip().split(" => ")]
        mats = [asmatrix(array(rulepart)) for rulepart in rule]
        m1 = tup(mats[1])
        for j in range(4):
            rules[tup(rot90(mats[0], j, (0, 1)))] = m1
            rules[tup(rot90(flip(mats[0], 0), j, (0, 1)))] = m1
    
    def part_1():
        mat = tup(asmatrix(array([list(".#."), list("..#"), list("###")])))
        n = 3
        for _ in range(5):
            if n % 2 == 0:
                newmat_arr = [[None for _ in range(n//2)] for _ in range(n//2)]
                for x in range(0, n, 2):
                    for y in range(0, n, 2):
                        submat = mat[y:y+2][x:x+2]
                        newmat_arr[x//2][y//2] = rules[submat]
                mat = tup(newmat_arr)
        print(untup(mat).flatten())
        pass
    
    def part_2():
        pass
    
    part_1()
    part_2()


day_21()
