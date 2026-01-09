class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self):
        """Convert to level-order list"""
        if not self:
            return []

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

        while result and result[-1] is None:
            result.pop()

        return result


def create_tree_from_list(lst):
    """Create tree from level-order list"""
    if not lst or lst[0] is None:
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
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Max gain from left and right subtrees (ignore if negative)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Current path sum if we take this node as "root"
            current_path_sum = node.val + left_gain + right_gain

            # Update global maximum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return max gain if we continue path upward (can only take one side)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum


# Test cases
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (tree_list, expected, test_name)
        ([1, 2, 3], 6, "Example 1"),
        ([-10, 9, 20, None, None, 15, 7], 42, "Example 2"),
        ([-3], -3, "Single negative node"),
        ([2, -1], 2, "Node with negative child"),
        ([1, -2, 3], 4, "Path through root"),
        ([-1, -2, -3], -1, "All negative values"),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48, "Complex tree"),
        ([10, 9, 20, None, None, 15, 7], 45, "Modified example 2"),
        ([1, 2, 3, 4, 5, 6, 7], 18, "Perfect binary tree"),
        ([1, 2, None, 3, None, 4], 10, "Left-skewed tree"),
        ([1, None, 2, None, 3, None, 4], 10, "Right-skewed tree"),
        ([0], 0, "Single zero node"),
    ]

    print("Testing Binary Tree Maximum Path Sum:")
    print("=" * 70)

    for tree_list, expected, test_name in test_cases:
        print(f"\nTest: {test_name}")
        print(f"Tree: {tree_list}")

        tree = create_tree_from_list(tree_list)
        result = solution.maxPathSum(tree)

        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

        # Show explanation for small examples
        if len(tree_list) <= 3:
            print("Explanation:")
            if tree_list == [1, 2, 3]:
                print("  Path 2 -> 1 -> 3 = 2 + 1 + 3 = 6")
            elif tree_list == [-10, 9, 20, None, None, 15, 7]:
                print("  Path 15 -> 20 -> 7 = 15 + 20 + 7 = 42")

    print("\n" + "=" * 70)

    # Visual explanation
    print("\nVisual explanation for Example 1:")
    print("Tree: [1, 2, 3]")
    print("    1")
    print("   / \\")
    print("  2   3")
    print("\nPossible paths and their sums:")
    print("Path [2]: sum = 2")
    print("Path [3]: sum = 3")
    print("Path [1]: sum = 1")
    print("Path [2, 1]: sum = 3")
    print("Path [1, 3]: sum = 4")
    print("Path [2, 1, 3]: sum = 6  ← Maximum")

    print("\n\nVisual explanation for Example 2:")
    print("Tree: [-10, 9, 20, None, None, 15, 7]")
    print("      -10")
    print("      /  \\")
    print("     9    20")
    print("         /  \\")
    print("        15   7")
    print("\nPossible paths and their sums:")
    print("Path [9]: sum = 9")
    print("Path [15]: sum = 15")
    print("Path [7]: sum = 7")
    print("Path [20]: sum = 20")
    print("Path [15, 20]: sum = 35")
    print("Path [20, 7]: sum = 27")
    print("Path [15, 20, 7]: sum = 42  ← Maximum")
    print("Path [-10, 20, 15]: sum = 25")
    print("Path [-10, 20, 7]: sum = 17")