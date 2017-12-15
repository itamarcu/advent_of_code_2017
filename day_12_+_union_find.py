from typing import Generic, TypeVar, Optional, Dict, List, Set

K = TypeVar("K")


class UpNode(Generic[K]):
    def __init__(self, key: K,
                 parent: Optional["UpNode[K]"] = None) -> None:
        self.parent = parent
        self.key = key
        self.rank = 0
        self.size = 1
    
    def __repr__(self):
        par_str = str(self.parent.key) if self.parent is not None else "*"
        return "k:" + str(self.key) \
               + " r:" + str(self.rank) \
               + " s:" + str(self.size) \
               + " pk:" + par_str
    
    
class DisjointSets(Generic[K]):  # Union-find
    def __init__(self):
        self.nodes: Dict[K, UpNode[K]] = {}
        self.roots: Set[UpNode[K]] = set()
    
    def make_set(self, key: K):
        if key not in self.nodes:
            self.nodes[key] = UpNode(key)
            self.roots.add(self.nodes[key])
    
    def union(self, key1: K, key2: K):
        node1 = self.find_as_node(key1)
        node2 = self.find_as_node(key2)
        if node1 == node2:
            return
        if node1.rank > node2.rank:
            node2.parent = node1
            node1.size += node2.size
            self.roots.remove(node2)
        elif node1.rank < node2.rank:
            node1.parent = node2
            node2.size += node1.size
            self.roots.remove(node1)
        else:
            node2.parent = node1
            node1.size += node2.size
            node1.rank += 1
            self.roots.remove(node2)
    
    def find_as_key(self, key: K) -> K:
        return self.find_as_node(key).key
    
    def find_as_node(self, key: K) -> UpNode[K]:
        """Returns "root" of the key's disjoint set.
         The parent of return node is guaranteed to be None."""
        if key not in self.nodes:
            raise KeyError("Key did not go through make_set()! " + key)
        node = self.nodes[key]
        visited_nodes: List[UpNode[K]] = []
        while node.parent is not None:
            visited_nodes.append(node)
            node = node.parent
        for visited_node in visited_nodes:  # Path compression
            visited_node.parent = node
            # no need for size changes, do not worry
        return node


def day_12():
    with open('input.txt') as input_file:
        lines = [line.replace(",", "")
                     .strip()
                     .split(" ") for line in input_file.readlines()]
    
    disj = DisjointSets()
    for line in lines:
        disj.make_set(line[0])
    for line in lines:
        word1, sign, *words = line
        for word in words:
            disj.union(word1, word)
    
    node1 = disj.find_as_node(lines[0][0])
    print("Size of set 1:", node1.size)
    print("Number of sets:", len(disj.roots))

day_12()
