import math
import matplotlib.pyplot as plt


def test_1():
    jump = 99
    num_of_steps = 300
    state = [0]
    curr = 0
    xs = []
    ys = []
    zs = []
    cycles = 0
    for i in range(1, num_of_steps + 1):
        if curr + jump > i:
            cycles += 1
        curr = 1 + (curr + jump) % i
        state.insert(curr, i)
        xs.append(i)
        ys.append(curr)
        zs.append((i - (i % jump - jump) ** 2) % (i + 1))
    
    print("end test")
    
    plt.plot(xs, ys)
    plt.plot(xs, zs)
    plt.title("curr, by i, and a guess")
    plt.show()


test_1()
