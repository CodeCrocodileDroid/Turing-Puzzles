class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self):
        """Convert the flattened tree to list representation"""
        result = []
        current = self
        while current:
            result.append(current.val)
            if current.left:
                # Should not happen in flattened tree
                result.append("ERROR: Left not null!")
            current = current.right
        return result


def create_tree_from_list(lst):
    """Create tree from level-order list"""
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        node = queue.pop(0)

        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root


class Solution:
    def flatten(self, root):
        current = root

        while current:
            if current.left:
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = current.right
                current.right = current.left
                current.left = None

            current = current.right


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    print("Test case 1:")
    tree1 = create_tree_from_list([1, 2, 5, 3, 4, None, 6])
    solution.flatten(tree1)
    print(f"Flattened: {tree1.to_list()}")
    print(f"Expected: [1, 2, 3, 4, 5, 6]")
    print()

    # Test case 2
    print("Test case 2:")
    tree2 = create_tree_from_list([])
    if tree2:
        solution.flatten(tree2)
        print(f"Flattened: {tree2.to_list()}")
    else:
        print(f"Flattened: []")
    print(f"Expected: []")
    print()

    # Test case 3
    print("Test case 3:")
    tree3 = create_tree_from_list([0])
    solution.flatten(tree3)
    print(f"Flattened: {tree3.to_list()}")
    print(f"Expected: [0]")
    print()

    # Test case 4
    print("Test case 4:")
    tree4 = create_tree_from_list([1, 2, None, 3])
    solution.flatten(tree4)
    print(f"Flattened: {tree4.to_list()}")
    print(f"Expected: [1, 2, 3]")