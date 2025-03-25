class Category:
    def __init__(self, name: str, parent: "Category | None"):
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name


a = Category(name="A", parent=None)
b = Category(name="B", parent=a)
c = Category(name="C", parent=a)
d = Category(name="D", parent=b)
e = Category(name="E", parent=b)
f = Category(name="F", parent=c)
g = Category(name="G", parent=c)
h = Category(name="H", parent=d)
i = Category(name="I", parent=e)
j = Category(name="J", parent=e)
k = Category(name="K", parent=f)
l = Category(name="L", parent=g)
m = Category(name="M", parent=g)
n = Category(name="N", parent=g)

CATEGORIES = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]




def get_children(category: Category):
    """Get children of a category.

    Args:
        category (Category): The category to find children for.

    Returns:
        children (list(Category)): The list of child categories of the
            parent category.
    """
    print("filtering")
    return [
        c
        for c in CATEGORIES
        if hasattr(c.parent, "name") and c.parent.name == category.name
    ]


def get_descendants(category: Category):

    descendants = []
    children = get_children(category=category)

    for child in children:
        descendants.append(child)
        descendants.extend(get_descendants(child))

    return descendants


if __name__ == "__main__":
    descendants = get_descendants(c)
    print(*descendants, sep=",")
