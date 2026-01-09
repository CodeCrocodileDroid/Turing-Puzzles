# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Level-order representation
        result = []
        queue = [self]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return str(result)


class Solution:
    def invertTree(self, root):
        # Base case: if root is None, return None
        if not root:
            return None

        # Invert left and right subtrees recursively
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Swap the left and right children
        root.left, root.right = right, left

        return root


# Helper function to create a binary tree from a list representation
def create_tree_from_list(lst):
    """
    Creates a binary tree from a level-order list representation.
    """
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        node = queue.pop(0)

        # Left child
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root


# Helper function to get level-order traversal
def level_order_traversal(root):
    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem
    print("Test case 1:")
    tree1 = create_tree_from_list([4, 2, 7, 1, 3, 6, 9])
    print(f"Original tree: {level_order_traversal(tree1)}")
    inverted1 = solution.invertTree(tree1)
    print(f"Inverted tree: {level_order_traversal(inverted1)}")
    print(f"Expected: [4, 7, 2, 9, 6, 3, 1]")
    print()

    # Visual representation for test case 1
    print("Visual representation:")
    print("Original:       4               Inverted:       4")
    print("              /   \\                          /   \\")
    print("             2     7                        7     2")
    print("            / \\   / \\                      / \\   / \\")
    print("           1   3 6   9                    9   6 3   1")
    print()

    # Test case 2: Example from problem
    print("Test case 2:")
    tree2 = create_tree_from_list([2, 1, 3])
    print(f"Original tree: {level_order_traversal(tree2)}")
    inverted2 = solution.invertTree(tree2)
    print(f"Inverted tree: {level_order_traversal(inverted2)}")
    print(f"Expected: [2, 3, 1]")
    print()

    # Visual representation for test case 2
    print("Visual representation:")
    print("Original:       2               Inverted:       2")
    print("              /   \\                          /   \\")
    print("             1     3                        3     1")
    print()

    # Test case 3: Empty tree
    print("Test case 3:")
    tree3 = create_tree_from_list([])
    print(f"Original tree: {level_order_traversal(tree3)}")
    inverted3 = solution.invertTree(tree3)
    print(f"Inverted tree: {level_order_traversal(inverted3)}")
    print(f"Expected: []")
    print()

    # Test case 4: Single node
    print("Test case 4:")
    tree4 = create_tree_from_list([1])
    print(f"Original tree: {level_order_traversal(tree4)}")
    inverted4 = solution.invertTree(tree4)
    print(f"Inverted tree: {level_order_traversal(inverted4)}")
    print(f"Expected: [1]")
    print()

    # Test case 5: Left-skewed tree
    print("Test case 5:")
    tree5 = create_tree_from_list([1, 2, None, 3, None, 4])
    print(f"Original tree: {level_order_traversal(tree5)}")
    inverted5 = solution.invertTree(tree5)
    print(f"Inverted tree: {level_order_traversal(inverted5)}")
    print(f"Expected: [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4]")
    print("(Note: This becomes a right-skewed tree)")
    print()

    # Test case 6: Complete binary tree
    print("Test case 6:")
    tree6 = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    print(f"Original tree: {level_order_traversal(tree6)}")
    inverted6 = solution.invertTree(tree6)
    print(f"Inverted tree: {level_order_traversal(inverted6)}")
    print(f"Expected: [1, 3, 2, 7, 6, 5, 4]")
    print()

    # Visual representation for test case 6
    print("Visual representation:")
    print("Original:         1               Inverted:       1")
    print("                /   \\                          /   \\")
    print("               2     3                        3     2")
    print("              / \\   / \\                      / \\   / \\")
    print("             4   5 6   7                    7   6 5   4")