def distance_alt(x, y, z):
    return max(abs(x), abs(y), abs(z))


def day11_alt():
    with open('input.txt') as input_file:
        moves = input_file.readline().split(",")
    
    dirs = {"ne": (+1, -1, 0),
            "sw": (-1, +1, 0),
            "n": (0, -1, +1),
            "s": (0, +1, -1),
            "nw": (-1, 0, +1),
            "se": (+1, 0, -1), }
    place = (0, 0, 0)
    max_dist = 0
    
    for move in moves:
        print(place, move)
        place = tuple(a + b for a, b in zip(place, dirs[move]))
        max_dist = max(max_dist, distance_alt(*place))
    
    print("last distance:", distance_alt(*place))
    print("max distance:", max_dist)


# ~~~~~~~~~~~~~~


def distance(x, y):
    return max(abs(x), abs(y), abs(x + y))


def day11():
    with open('input.txt') as input_file:
        moves = input_file.readline().split(",")
    
    dirs = {"n": (0, 1),
            "s": (0, -1),
            "ne": (1, 0),
            "sw": (-1, 0),
            "nw": (-1, 1),
            "se": (1, -1), }
    place = (0, 0)
    max_dist = 0
    
    for move in moves:
        place = (place[0] + dirs[move][0], place[1] + dirs[move][1])
        max_dist = max(max_dist, distance(*place))
    
    print("last distance:", distance(*place))
    print("max distance:", max_dist)


day11_alt()
