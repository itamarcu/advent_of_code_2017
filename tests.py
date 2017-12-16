#!/bin/python3

import sys

direction_strings = ["UL", "UR", "R", "LR", "LL", "L"]
directions = {"UL": (-1, -2), "UR": (+1, -2), "R": (+2, 0), "LR": (+1, +2),
              "LL": (-1, +2), "L": (-2, 0)}


def printShortestPath(n, y_start, x_start, y_end, x_end):
    #  Print the distance along with the sequence of moves.
    def coordimod(x, y):
        return (x * 2 + y) % 4
    
    if coordimod(x_start, y_start) != coordimod(x_end, y_end):
        print("Impossible")
        return
    
    answer = None
    frontier = [(x_start, y_start, [])]
    while True:
        x, y, path = frontier.pop(0)
        if x == x_end and y == y_end:
            answer = path
            break
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        for dirc in direction_strings:
            step = (
                x + directions[dirc][0], y + directions[dirc][1],
                path[:] + [dirc])
            frontier.append(step)
    
    print(len(answer))
    print(" ".join(answer))


if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end),
                                      int(j_end)]
    printShortestPath(n, i_start, j_start, i_end, j_end)
