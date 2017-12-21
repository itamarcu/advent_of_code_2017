from numpy import *


def day_21():
    with open("input.txt") as file:
        lines = file.readlines()

    def hashable(matrix_2d):
        return matrix_2d.tobytes()

    def niceprint(mat):
        s = 0
        for line in mat:
            s += sum(1 for ch in line if ch == '#')
            print("".join(line))
        print("count =", s)

    # .#./###/.#. => #..#/.###/..#./.##.
    # ##/#. => .#./.../...
    rules = dict()
    booler = lambda c: c == '#'
    unbooler = lambda c: '#' if c else '.'
    for line in lines:
        rule = [[list(p) for p in part.split("/")] for part in
                line.strip().split(" => ")]
        mats = [asmatrix(vectorize(booler)(array(rulepart))) for rulepart in rule]
        m1 = mats[1]
        for j in range(4):
            rules[hashable(rot90(mats[0], j, (0, 1)))] = m1
            rules[hashable(rot90(flip(mats[0], 0), j, (0, 1)))] = m1

    def part_1():
        mat = asmatrix(array([list(".#."), list("..#"), list("###")]))
        mat = vectorize(booler)(mat)
        n = 3
        for _ in range(18):
            if n % 2 == 0:
                m = 2
            else:  # if n % 3 == 0:
                m = 3
            new_n = n // m * (m + 1)
            newmat_arr = empty((new_n, new_n), dtype=bool)
            for x in range(0, n, m):
                for y in range(0, n, m):
                    submat = hashable(mat[y:y + m, x:x + m])
                    xx = x // m * (m + 1)
                    yy = y // m * (m + 1)
                    newmat_arr[xx:xx + (m + 1), yy:yy + (m + 1)] = rules[submat]
            n = new_n
            mat = newmat_arr.transpose()  # I dunno why but it solves a bug :|
        print(sum(mat.flatten()))
        mat = vectorize(unbooler)(mat)
        # niceprint(mat)

    def part_2():
        pass

    part_1()
    part_2()


day_21()
