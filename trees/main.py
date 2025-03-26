class Category:
    def __init__(
        self, k: str, p: "Category | None", lc: "Category | None", rs: "Category | None"
    ):
        """A category node.

        Args:
            k (str): Key.
            p (Category): Parent node.
            lc (Category): Left child.
            rs (Category): Right sibling.
        """
        self.k = k
        self.p = p
        self.lc = lc
        self.rs = rs

    def __str__(self):
        return self.k

    def get_rmc(self):
        """Given a category, return the right most child of the category."""
        if not self.lc:
            return None

        category = self.lc

        while category.rs:
            category = category.rs

        return category

    def add_child(self, k: str):
        new_node = Category(k=k, lc=None, rs=None, p=None)
        new_node.p = self
        rmc_of_parent = self.get_rmc(category=self)

        if rmc_of_parent:
            rmc_of_parent.rs = new_node
        else:
            new_node.p.lc = new_node

        return new_node

    def get_children(self):
        # Get left most child
        child = self.lc

        if not child:
            return []

        # Get all siblings of the left most child
        children = [child]

        while child.rs:
            children.append(child.rs)
            child = child.rs

        return children

    def get_descendants(self):
        descendants = []

        # Get children
        child = self.lc

        if not child:
            return []

        # Get all siblings of the left most child
        children = [child]

        while child.rs:
            children.append(child.rs)
            child = child.rs

        for child in children:
            descendants.append(child)
            self = self.lc
            descendants.extend(self.get_descendants())

        return descendants

    def get_descendants(self):
        if self is None:
            return []

        descendants = [self]

        for child in self.get_children():
            descendants += child.get_descendants()

        return descendants

    def get_ancestors(self):
        parents = []
        category = self
        while category.p:
            category = category.p
            parents.append(category)
        return parents

    def get_siblings(self):
        category = self
        if not category.p:
            return None
        self = category.p
        return self.get_children()

    def get_siblings_recursively(self):
        if self is None:
            return []

        if self.p is None:
            return []

        if self.rs is None:
            return [self]

        return [self] + self.rs.get_siblings_recursively()
    
    def get_children_v2(self):
        if self is None:
            return []

        if self.lc is None:
            return []
        
        return self.lc.get_siblings_recursively()


# class CategoryManager:
#     """Class to do tree wide operations."""
#     def __init__(self, root: Category):
#         """
#         Args:
#             root (Category): The root node.
#         """
#         self.root = root

#     def add_lc(self, k: str, c: Category):
#         """Add a left child to the node.

#         k (str): The key identifying the category
#         c (Category): The new category to be added.
#         """
#         pass

#     def add_rs(self, k:str, c: Category):
#         """Add a right sibling to the node.

#         k (str): The key identifying the category
#         c (Category): The new category to be added.
#         """
#         pass

a = Category(k="A", p=None, lc=None, rs=None)

b = Category(k="B", p=None, lc=None, rs=None)
b.p = a
a.lc = b

c = Category(k="C", p=None, lc=None, rs=None)
c.p = a
b.rs = c

d = Category(k="D", p=None, lc=None, rs=None)
d.p = b
b.lc = d

e = Category(k="E", p=None, lc=None, rs=None)
e.p = b
d.rs = e

f = Category(k="F", p=None, lc=None, rs=None)
f.p = c
c.lc = f

g = Category(k="G", p=None, lc=None, rs=None)
g.p = c
f.rs = g

h = Category(k="H", p=None, lc=None, rs=None)
h.p = d
d.lc = h

i = Category(k="I", p=None, lc=None, rs=None)
i.p = e
e.lc = i

j = Category(k="J", p=None, lc=None, rs=None)
j.p = e
i.rs = j

k = Category(k="K", p=None, lc=None, rs=None)
k.p = f
f.lc = k

l = Category(k="L", p=g, lc=None, rs=None)
l.p = g
g.lc = l

m = Category(k="M", p=None, lc=None, rs=None)
m.p = g
l.rs = m

n = Category(k="N", p=None, lc=None, rs=None)
n.p = g
m.rs = n

# CATEGORIES = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]


# def get_children(category: Category):
#     """Get children of a category.

#     Args:
#         category (Category): The category to find children for.

#     Returns:
#         children (list(Category)): The list of child categories of the
#             parent category.
#     """
#     print("filtering")
#     return [c for c in CATEGORIES if hasattr(c.p, "k") and c.p.k == category.k]


# def get_descendants(category: Category):

#     descendants = []
#     children = get_children(category=category)

#     for child in children:
#         descendants.append(child)
#         descendants.extend(get_descendants(child))

#     return descendants


if __name__ == "__main__":
    # descendants = get_descendants_v2(c)
    # print(*descendants, sep=",")
    # add_child(category=h, k="O")

    # print(*get_descendants_v2(h))

    # p = add_child(category=g, k="P")

    # print(*get_descendants_v2(g))

    # print(*get_ancestors(j))

    # print(*get_siblings(c))
    print(*e.get_children_v2(), sep=", ")
    # print(*l.get_siblings_recursively(), sep=", ")
    # print(*g.get_ancestors(), sep=", ")
    # print(*a.get_descendants(), sep=", ")
