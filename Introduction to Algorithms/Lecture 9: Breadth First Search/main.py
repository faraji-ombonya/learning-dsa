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


def bfs():
    stack = []

    # Add the source node to the stack
    stack.append("s")

    discovered = {}

    # Mark the source node as discovered
    discovered["s"] = True

    visited = {}

    i = 1
    while stack:

        # Visit node
        node = stack.pop()

        # Discover neighbours
        for neigbour in G4[node]:
            is_discovered = discovered.get(neigbour, False)
            if not is_discovered:
                stack.append(neigbour)
                discovered[neigbour] = True

        # Mark node as visited
        visited[node] = True

        print(i)
        i += 1

        print("Just visited::", node)

    print(visited)


if __name__ == "__main__":
    bfs()
