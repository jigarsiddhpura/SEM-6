class Node:
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None

def build_kdtree(points, depth=0):
    if not points:
        return None

    # Select axis based on depth so that axis cycles through all valid values
    k = len(points[0])  # Dimension of the points
    axis = depth % k

    # Sort points based on the axis and choose median as pivot element
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    # Create node and construct subtrees
    node = Node(points[median], axis)
    node.left = build_kdtree(points[:median], depth + 1)
    node.right = build_kdtree(points[median + 1:], depth + 1)

    return node

def print_tree(node, level=0, side=None):
    if node is not None:
        prefix = ""
        if side is not None:
            prefix = side + "---- "
        print("   " * level + prefix + str(node.point))
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")

# Sample data points
points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 8], [1, 5], [9, 5]]
# points = [[6, 2, 9], [7, 1, 2], [2, 9, 6], [3, 6, 1], [4, 8, 5], [8, 4, 4], [5, 3, 7], [1, 5, 1], [9, 5, 4]]
# Build balanced KDTree
root = build_kdtree(points)
# Print the tree
print_tree(root)
