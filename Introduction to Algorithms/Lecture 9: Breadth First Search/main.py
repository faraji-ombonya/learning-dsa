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

    print("new stack::", stack)

    stack.append("s")

    print(" stack after adding the source node::", stack)

    i = 0

    while stack:

        # Visit node
        node = stack.pop()
        print("POPPED NODE::", node)

        print("STACK After POP::", stack)

        print("NEIGHBOURS OF THE SOURCE NODE::", G4[node])

        # Discover neighbours
        for neigbour in G4[node]:
            stack.append(neigbour)

        print(f"STACk on Iter::: {i}", stack)

        i += 1

        if i == 1:
            return


if __name__ == "__main__":
    bfs()
