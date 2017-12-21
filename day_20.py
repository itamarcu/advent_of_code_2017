from operator import __add__

import itertools


def day_20():
    with open("input.txt") as file:
        lines = file.readlines()
    
    def part_1():
        particles = []
        for line in lines:
            particles.append(
                [tuple(map(int, part[part.index("<") + 1:part.index(">")]
                           .split(","))) for part in
                 line.strip().split(", ")])
        minimum = 99999999
        bests = []
        for i in range(len(particles)):
            acceleration = sum(map(abs, particles[i][2]))
            if acceleration < minimum:
                minimum = acceleration
                bests = [i]
            elif acceleration == minimum:
                bests.append(i)
        
        #  might get a super edge case, but not with my input :P
        print("Part 1:", bests)  # 364
    
    def part_2():
        particles = []
        for line in lines:
            particles.append(
                [tuple(map(int, part[part.index("<") + 1:part.index(">")]
                           .split(","))) for part in
                 line.strip().split(", ")])
        print("...")
        for _ in range(100):
            # print(len(particles))  # for debugging
            for i in range(len(particles)):
                par1 = particles[i]
                par1[1] = tuple(map(__add__, par1[1], par1[2]))
                par1[0] = tuple(map(__add__, par1[0], par1[1]))
            indices_to_remove = set()
            for i, j in itertools.product(range(len(particles)), repeat=2):
                if i != j:
                    par1, par2 = particles[i], particles[j]
                    if par1[0] == par2[0]:
                        indices_to_remove.add(i)
                        indices_to_remove.add(j)
            particles = [i for j, i in enumerate(particles) if
                         j not in indices_to_remove]
        
        print()
        print("Part 2 is probably:", len(particles))
    
    part_1()
    part_2()


day_20()
