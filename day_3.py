import operator
from typing import Tuple, Dict, List

input_number = 347991

directions: List[Tuple[int, int]] = [(+1, 0), (0, +1), (-1, 0), (0, -1)]


def day_3():
    def part_1():
        step_size = 1
        current = 1
        position: Tuple[int, int] = (0, 0)
        i = 0
        while True:
            direction = directions[i]
            for _ in range(step_size):
                position: Tuple[int, int] = tuple(map(operator.__add__, position, direction))
                current += 1
                if current == input_number:
                    print("Part 1:", sum(abs(coord) for coord in position))
                    return
            if i % 2 == 1:  # after move up and move down
                step_size += 1
            i = (i + 1) % 4
    
    def part_2():
        grid: Dict[Tuple[int, int], int] = {(0, 0): 1}
        
        def calc_area(x, y):
            amount = 0
            for xx in range(-1, 1 + 1):
                for yy in range(-1, 1 + 1):
                    amount += grid.setdefault((x + xx, y + yy), 0)
            grid[(x, y)] = amount
        
        step_size = 1
        current = 1
        position: Tuple[int, int] = (0, 0)
        i = 0
        while True:
            direction = directions[i]
            for _ in range(step_size):
                position: Tuple[int, int] = tuple(map(operator.__add__, position, direction))
                current += 1
                calc_area(*position)
                if grid[position] > input_number:
                    print("Part 2:", grid[position])
                    return
            if i % 2 == 1:  # after move up and move down
                step_size += 1
            i = (i + 1) % 4
    
    part_1()
    part_2()


day_3()
