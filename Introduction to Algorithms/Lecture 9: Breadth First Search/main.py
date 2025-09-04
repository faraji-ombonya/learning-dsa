class G:
    pass


class Node:
    pass


class Vertex:
    pass


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
