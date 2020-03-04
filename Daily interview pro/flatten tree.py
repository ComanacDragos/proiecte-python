class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def in_order(node):
    if node == None:
        return
    print(node.value, end = " ")
    in_order(node.left)
    in_order(node.right)

def flatten_bst(node):
    if node == None or (node.left == None and node.right == None):
        return
    if node.left != None:
        flatten_bst(node.left)
        temp = node.right
        node.right = node.left
        node.left = None

        t = node.right
        while t.right != None:
            t = t.right
        t.right = temp


    flatten_bst(node.right)


# Fill this in.
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

in_order(n1)
print()
#       1
#    /    \
#   2      3
#  / \    /
# 5   6  4

flatten_bst(n1)
in_order(n1)

# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4
