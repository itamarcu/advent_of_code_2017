from typing import List

lines = [line.split() for line in open('input.txt', 'r').readlines()]


class Node:
    def __init__(self, name, weight):
        self.name: str = name
        self.weight: int = weight
        self.children: List[Node] = []
        self.solution = ()
    
    def solve(self):  # (False, weight) or (True, answer weight)
        if len(self.children) == 0:
            return False, self.weight, self.name
        weights = []
        for node in self.children:
            node.solution = node.solve()
            boo, weigh, nod = node.solution
            if boo:
                return True, weigh, nod
            weights.append(weigh)
        
        for i in range(len(self.children)):
            good_weight = weights[0]
            if good_weight != weights[i]:
                # hopefully there's a 3rd one, otherwise
                # there are multiple answers
                if weights[2] != weights[0]:
                    i = 0  # :P
                    good_weight = weights[2]
                return True, good_weight - weights[i] \
                       + self.children[i].weight, self.children[i].name
        
        return False, sum(weights) + self.weight, self.name
    
    def print(self, depth):
        print(depth * "\t", self.name, self.weight, self.solution)
        depth += 1
        for child in self.children:
            child.print(depth)


def day_7():
    seen = set()
    nodes = dict()
    for line in lines:
        nodes[line[0]] = Node(name=line[0], weight=int(line[1][1:-1]))
    for s in nodes:
        seen.add(s)
    for line in lines:
        if len(line) > 2:
            for s in line[3:]:
                s = s.replace(",", "")
                nodes[line[0]].children.append(nodes[s])
                seen.remove(s)
    
    root = nodes[seen.pop()]
    root.solution = root.solve()
    root.print(0)
    print()
    print("(solved?, answer, culprit) =", root.solution)


day_7()
