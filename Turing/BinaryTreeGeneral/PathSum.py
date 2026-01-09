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
    def hasPathSum(self, root, targetSum):
        """Recursive solution"""
        if not root:
            return False

        # Check if current node is a leaf
        if not root.left and not root.right:
            return targetSum == root.val

        # Subtract current node's value from targetSum
        remaining = targetSum - root.val

        # Check left and right subtrees
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


class Solution2:
    def hasPathSum(self, root, targetSum):
        """Iterative solution using stack"""
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, current_sum = stack.pop()

            # Check if leaf node and sum equals 0
            if not node.left and not node.right and current_sum == 0:
                return True

            # Add children to stack
            if node.right:
                stack.append((node.right, current_sum - node.right.val))
            if node.left:
                stack.append((node.left, current_sum - node.left.val))

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    test_cases = [
        # (tree_list, targetSum, expected, test_name)
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True, "Example 1"),
        ([1, 2, 3], 5, False, "Example 2"),
        ([], 0, False, "Example 3 - Empty tree"),
        ([1], 1, True, "Single node, target equals node value"),
        ([1], 2, False, "Single node, target not equal"),
        ([1, 2], 1, False, "Not a leaf path"),
        ([1, 2, 3], 4, True, "Path 1->3"),
        ([1, 2, 3], 3, True, "Path 1->2"),
        ([1, -2, -3, 1, 3, -2, None, -1], -1, True, "Negative values"),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 26, True, "Path 5->8->13"),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 18, True, "Path 5->4->11->-2? Wait, check"),
        ([1, 2, None, 3, None, 4, None, 5], 15, True, "Left-skewed tree"),
        ([1, None, 2, None, 3, None, 4, None, 5], 15, True, "Right-skewed tree"),
    ]

    # Fix the test cases with correct sums
    test_cases[9] = ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 26, True, "Path 5->8->13")
    test_cases[10] = ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 18, False, "No path sum 18")

    print("Testing Recursive Solution:")
    print("=" * 70)

    for tree_list, target, expected, test_name in test_cases:
        print(f"\nTest: {test_name}")
        print(f"Tree: {tree_list}")
        print(f"TargetSum: {target}")

        if tree_list:
            tree = create_tree_from_list(tree_list)
            result = solution.hasPathSum(tree, target)
        else:
            result = False

        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

    print("\n" + "=" * 70)
    print("\nTesting Iterative Solution:")
    print("=" * 70)

    for tree_list, target, expected, test_name in test_cases[:5]:  # Test first 5
        print(f"\nTest: {test_name}")
        print(f"Tree: {tree_list}")
        print(f"TargetSum: {target}")

        if tree_list:
            tree = create_tree_from_list(tree_list)
            result = solution2.hasPathSum(tree, target)
        else:
            result = False

        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

    print("\n" + "=" * 70)

    # Visual example
    print("\nVisual example for Example 1:")
    print("Tree: [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]")
    print("TargetSum: 22")
    print("\nTree structure:")
    print("        5")
    print("       / \\")
    print("      4   8")
    print("     /   / \\")
    print("    11  13  4")
    print("   / \\      \\")
    print("  7   2      1")
    print("\nPath 5->4->11->2 = 5 + 4 + 11 + 2 = 22 ✓")