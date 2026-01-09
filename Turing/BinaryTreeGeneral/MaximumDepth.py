# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        # Base case: empty tree has depth 0
        if not root:
            return 0

        # Recursively find depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return max depth + 1 (for current node)
        return max(left_depth, right_depth) + 1


# Helper function to create a binary tree from a list representation
def create_tree_from_list(lst, index=0):
    """
    Creates a binary tree from a list representation.
    For node at index i:
    - left child is at index 2*i + 1
    - right child is at index 2*i + 2
    """
    if index >= len(lst) or lst[index] is None:
        return None

    root = TreeNode(lst[index])
    root.left = create_tree_from_list(lst, 2 * index + 1)
    root.right = create_tree_from_list(lst, 2 * index + 2)

    return root


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from LeetCode
    print("Test case 1:")
    # Tree: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    tree1 = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    depth1 = solution.maxDepth(tree1)
    print(f"Tree: [3,9,20,null,null,15,7]")
    print(f"Maximum depth: {depth1}")
    print(f"Expected: 3")
    print()

    # Test case 2: Single node
    print("Test case 2:")
    # Tree: [1]
    tree2 = create_tree_from_list([1])
    depth2 = solution.maxDepth(tree2)
    print(f"Tree: [1]")
    print(f"Maximum depth: {depth2}")
    print(f"Expected: 1")
    print()

    # Test case 3: Empty tree
    print("Test case 3:")
    # Tree: []
    tree3 = create_tree_from_list([])
    depth3 = solution.maxDepth(tree3)
    print(f"Tree: []")
    print(f"Maximum depth: {depth3}")
    print(f"Expected: 0")
    print()

    # Test case 4: Left-skewed tree
    print("Test case 4:")
    # Tree: [1, 2, null, 3, null, 4, null]
    #       1
    #      /
    #     2
    #    /
    #   3
    #  /
    # 4
    tree4 = create_tree_from_list([1, 2, None, 3, None, 4, None])
    depth4 = solution.maxDepth(tree4)
    print(f"Tree: [1, 2, null, 3, null, 4, null]")
    print(f"Maximum depth: {depth4}")
    print(f"Expected: 4")
    print()

    # Test case 5: Complete binary tree
    print("Test case 5:")
    # Tree: [1, 2, 3, 4, 5, 6, 7]
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    tree5 = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    depth5 = solution.maxDepth(tree5)
    print(f"Tree: [1, 2, 3, 4, 5, 6, 7]")
    print(f"Maximum depth: {depth5}")
    print(f"Expected: 3")
    print()

    # Test case 6: Right-skewed tree
    print("Test case 6:")
    # Tree: [1, null, 2, null, 3, null, 4]
    #       1
    #        \
    #         2
    #          \
    #           3
    #            \
    #             4
    tree6 = create_tree_from_list([1, None, 2, None, 3, None, 4])
    depth6 = solution.maxDepth(tree6)
    print(f"Tree: [1, null, 2, null, 3, null, 4]")
    print(f"Maximum depth: {depth6}")
    print(f"Expected: 4")