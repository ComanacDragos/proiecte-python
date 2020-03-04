class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def min_depth_bst(root):
    #print(root, root.left, root.right)
    if root.right == None and root.left == None:
        return 1

    if root.left != None:
        left = 1 + min_depth_bst(root.left)
    else:
        left = -1

    if root.right != None:
        right = 1 + min_depth_bst(root.right)
    else:
        right = -1


    if right == -1:
        return left
    if left == -1:
        return right

    #if left == -1:
    #  return right
    #if right == -1:
    # return left

    if left > right:
        return right
    return left



# Fill this in.

n3 = Node(3, None, Node(4))
n2 = Node(2)
n1 = Node(1, n2, n3)
n5 = Node(5,None, n1)

#     1
#    / \
#   2   3
#        \
#         4
print(min_depth_bst(n2))
# 2

def df(node):
    if node == None:
        return
    print(node, node.left, node.right)
    df(node.left)
    df(node.right)

