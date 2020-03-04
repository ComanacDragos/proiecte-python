class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def target_sum_bst(root, target):
    if root == None:
        return 0
    if target == root.value and root.left == None and root.right == None:
        return True
    if target_sum_bst(root.left, target-root.value) == True:
        return True
    if target_sum_bst(root.right, target - root.value) == True:
        return True
    return False
  # Fill this in.

#      1
#    /   \
#   2     3
#    \     \
#     6     4
n6 = Node(6)
n4 = Node(4)
n3 = Node(3, None, n4)
n2 = Node(2, None, n6)
n1 = Node(1, n2, n3)

print(target_sum_bst(n1, 8))
# True
# Path from 1 -> 2 -> 6

