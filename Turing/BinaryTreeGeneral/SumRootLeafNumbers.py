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
    def sumNumbers(self, root):
        """Recursive DFS solution"""

        def dfs(node, current_sum):
            if not node:
                return 0

            # Update current number: shift left and add current digit
            current_sum = current_sum * 10 + node.val

            # If leaf node, return the current number
            if not node.left and not node.right:
                return current_sum

            # Otherwise, return sum from left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


class Solution2:
    def sumNumbers(self, root):
        """Iterative solution using stack"""
        if not root:
            return 0

        total = 0
        stack = [(root, 0)]

        while stack:
            node, current_sum = stack.pop()

            # Update current number
            current_sum = current_sum * 10 + node.val

            # If leaf node, add to total
            if not node.left and not node.right:
                total += current_sum

            # Add children to stack
            if node.right:
                stack.append((node.right, current_sum))
            if node.left:
                stack.append((node.left, current_sum))

        return total


class Solution3:
    def sumNumbers(self, root):
        """Alternative recursive solution"""
        self.total = 0

        def traverse(node, path_sum):
            if not node:
                return

            # Update path sum
            path_sum = path_sum * 10 + node.val

            # Check if leaf node
            if not node.left and not node.right:
                self.total += path_sum
                return

            # Traverse left and right
            traverse(node.left, path_sum)
            traverse(node.right, path_sum)

        traverse(root, 0)
        return self.total


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()
    solution3 = Solution3()

    test_cases = [
        # (tree_list, expected_sum, test_name)
        ([1, 2, 3], 25, "Example 1"),
        ([4, 9, 0, 5, 1], 1026, "Example 2"),
        ([0], 0, "Single node 0"),
        ([1], 1, "Single node 1"),
        ([1, 2], 12, "Two nodes, left child only"),
        ([1, None, 3], 13, "Two nodes, right child only"),
        ([1, 2, 3, 4, 5, 6, 7], 522, "Perfect binary tree"),
        ([1, 2, None, 3, None, 4], 1234, "Left-skewed tree"),
        ([1, None, 2, None, 3, None, 4], 1234, "Right-skewed tree"),
        ([4, 9, 0, None, 1], 531, "Tree with single path"),
        ([], 0, "Empty tree"),
    ]

    print("Testing Recursive DFS Solution:")
    print("=" * 70)

    for tree_list, expected, test_name in test_cases:
        print(f"\nTest: {test_name}")
        print(f"Tree: {tree_list}")

        if tree_list:
            tree = create_tree_from_list(tree_list)
            result = solution.sumNumbers(tree)
        else:
            result = 0

        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

        # Show path calculations for small trees
        if len(tree_list) <= 5 and tree_list:
            print("Path calculations:")
            tree_obj = create_tree_from_list(tree_list)
            result2 = solution.sumNumbers(tree_obj)

    print("\n" + "=" * 70)
    print("\nTesting Iterative Solution:")
    print("=" * 70)

    for tree_list, expected, test_name in test_cases[:5]:  # Test first 5
        print(f"\nTest: {test_name}")
        print(f"Tree: {tree_list}")

        if tree_list:
            tree = create_tree_from_list(tree_list)
            result = solution2.sumNumbers(tree)
        else:
            result = 0

        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

    print("\n" + "=" * 70)

    # Detailed explanation with example
    print("\nDetailed explanation for Example 1:")
    print("Tree: [1, 2, 3]")
    print("Tree structure:")
    print("    1")
    print("   / \\")
    print("  2   3")
    print("\nPaths:")
    print("Path 1->2: Forms number 12")
    print("Path 1->3: Forms number 13")
    print("Sum = 12 + 13 = 25")

    print("\n\nDetailed explanation for Example 2:")
    print("Tree: [4, 9, 0, 5, 1]")
    print("Tree structure:")
    print("       4")
    print("      / \\")
    print("     9   0")
    print("    / \\")
    print("   5   1")
    print("\nPaths:")
    print("Path 4->9->5: Forms number 495")
    print("Path 4->9->1: Forms number 491")
    print("Path 4->0: Forms number 40")
    print("Sum = 495 + 491 + 40 = 1026")

    print("\n" + "=" * 70)
    print("\nTesting Alternative Recursive Solution:")
    print("=" * 70)

    for tree_list, expected, test_name in test_cases[:3]:  # Test first 3
        print(f"\nTest: {test_name}")
        print(f"Tree: {tree_list}")

        if tree_list:
            tree = create_tree_from_list(tree_list)
            result = solution3.sumNumbers(tree)
        else:
            result = 0

        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")