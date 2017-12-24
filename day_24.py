from typing import Tuple, List, Set, Dict


def day_24():
    with open("input.txt") as file:
        lines = file.readlines()
        all_bridges: List[Tuple[int, int]] = [tuple(map(int, line.strip().split("/"))) for line in
                       lines]
    
    Encoding = Tuple[int, Tuple[Tuple[int, int]]]
    
    def part_1():
        seen: Dict[Encoding, int] = dict()
        
        def recur(start: int, bridges: Set[Tuple[int, int]]) -> int:
            """Return maximum strength."""
            key: Encoding = (start, tuple(bridges))
            if key not in seen:
                if len(bridges) == 0:
                    seen[key] = 0
                    return seen[key]
                best = 0
                for b0, b1 in bridges:
                    for a, b in [(b0, b1), (b1, b0)]:
                        if a == start:
                            bridges.remove((b0, b1))
                            best = max(best, b0 + b1 + recur(b, bridges))
                            bridges.add((b0, b1))
                seen[key] = best
            return seen[key]
        
        print("Part 1:", recur(0, set(all_bridges)))  # 1940
    
    def part_2():
        seen: Dict[Encoding, Tuple[int, int]] = dict()
        
        def recur(start: int, bridges: Set[Tuple[int, int]]) -> Tuple[int, int]:
            """Return maximum strength and maximum length, with
            length being more important"""
            key: Encoding = (start, tuple(bridges))
            if key not in seen:
                if len(bridges) == 0:  # probably won't happen
                    seen[key] = (0, 0)
                    return seen[key]
                max_length = 0
                possibilities = []
                for b0, b1 in bridges:
                    for a, b in [(b0, b1), (b1, b0)]:
                        if a == start:
                            bridges.remove((b0, b1))
                            strength, length = recur(b, bridges)
                            bridges.add((b0, b1))
                            length += 1
                            strength += b0 + b1
                            if max_length < length:
                                max_length = length
                                possibilities = [strength]
                            elif max_length == length:
                                possibilities.append(strength)
                if len(possibilities) == 0:
                    seen[key] = (0, 0)
                else:
                    seen[key] = (max(possibilities), max_length)
            return seen[key]
        
        print("Part 2: (strength, length) =",
              recur(0, set(all_bridges)))  # (1928, 35)
    
    part_1()
    part_2()


day_24()
