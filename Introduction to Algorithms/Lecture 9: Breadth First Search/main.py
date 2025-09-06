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
