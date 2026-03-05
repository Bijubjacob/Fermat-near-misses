class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

def lowestCommonAncestor(p: Node, q: Node) -> Node:
    a, b = p, q

    while a != b:
        a = a.parent if a else q
        b = b.parent if b else p

    return a