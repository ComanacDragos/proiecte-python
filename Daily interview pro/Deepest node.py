"""

You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.

Here's a starting point:
"""


class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def DFS(depth, node):
    if node.left is None and node.right is None:
        return depth, node.val

    left = depth, node
    if node.left is not None:
        left = DFS(depth + 1, node.left)

    right = depth, node
    if node.right is not None:
        right = DFS(depth + 1, node.right)

    if left[0] > right[0]:
        return left
    return right


def deepest(node):
  """
     Fill this in.
  """
  return DFS(1, node)


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
