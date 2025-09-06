class G:
    pass


class Node:
    pass


class Vertex:
    pass


G1 = {0: [1, 2], 1: [0, 2, 3], 3: [2, 1]}

G2 = {0: [2], 1: [2, 0], 2: [1]}

G3 = {
    "a": ["b", "s"],
    "b": ["a"],
    "c": ["s", "d", "e"],
    "s": ["a", "c"],
    "d": ["f", "e", "c"],
    "e": ["c", "d", "f"],
    "f": ["d", "e"],
    "g": [],
}


G4 = {
    "s": ["r", "v", "u"],
    "r": ["w", "s", "t"],
    "u": ["t", "s", "y"],
    "t": ["u", "s", "r"],
    "y": ["u", "v", "x"],
    "v": ["w", "s", "y"],
    "w": ["z", "x", "v", "r"],
    "x": ["z", "w", "y"],
    "z": ["x", "w"],
}


class Queue:
    def __init__(self):
        self.ds = []

    def __str__(self):
        return ", ".join(self.ds)

    def __bool__(self):
        return len(self.ds) > 0

    def dequeue(self):
        return self.ds.pop(0)

    def enqueue(self, value):
        self.ds.append(value)


class Node:
    def __init__(self, key, length=0, visited=False, predecessor=None):
        self.key = key
        self.length = length
        self.visited = visited
        self.predecessor = predecessor


class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node, neighbors):
        self.adj[node] = neighbors


def bfs_v2():
    q = Queue()

    s = Node("s")
    q.enqueue(s)


def bfs():
    q = Queue()
    discovered = {}
    visited = {}
    distance = {}
    predecessor = {}

    # Add the source node to the stack
    q.enqueue("s")
    discovered["s"] = True
    distance["s"] = 0
    predecessor["s"] = None

    while q:
        # Visit node

        node = q.dequeue()

        # Discover neighbors
        for neighbor in G4[node]:
            is_discovered = discovered.get(neighbor, False)
            if not is_discovered:
                q.enqueue(neighbor)
                discovered[neighbor] = True
                distance[neighbor] = distance[node] + 1
                predecessor[neighbor] = node

        # Mark node as visited
        visited[node] = True

    print(visited)
    print("DISTANCE", distance)
    print("PREDECESSOR", predecessor)

    pre = predecessor["z"]
    path = []
    while pre:
        path.append(pre)
        pre = predecessor[pre]

    print(path)

    while path:
        print(path.pop(), end="", sep="->")


if __name__ == "__main__":

    bfs()
