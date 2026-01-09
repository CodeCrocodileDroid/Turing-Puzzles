class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_complete_tree_from_list(lst):
    """Create complete tree from level-order list"""
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
    def countNodes(self, root):
        """O(log n × log n) solution for complete trees"""
        if not root:
            return 0

        # Get left and right heights
        left_height = self.get_height(root, 'left')
        right_height = self.get_height(root, 'right')

        # If it's a perfect binary tree
        if left_height == right_height:
            return (1 << left_height) - 1  # 2^h - 1

        # Otherwise, count recursively
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_height(self, node, direction):
        height = 0
        while node:
            height += 1
            if direction == 'left':
                node = node.left
            else:
                node = node.right
        return height


class Solution2:
    """Binary search approach - O(log² n) - FIXED VERSION"""

    def countNodes(self, root):
        if not root:
            return 0

        h = self.get_left_height(root)
        if h == 0:
            return 1

        # Binary search for last level nodes
        # Last level can have 1 to 2^h nodes
        left, right = 1, (1 << h)  # 2^h
        while left < right:
            mid = (left + right + 1) // 2
            if self.node_exists(root, h, mid):
                left = mid
            else:
                right = mid - 1

        # Total nodes = perfect tree of height (h-1) + nodes in last level
        return (1 << h) - 1 + left

    def get_left_height(self, node):
        height = 0
        while node.left:
            height += 1
            node = node.left
        return height

    def node_exists(self, node, h, idx):
        """Check if node at position idx exists in last level"""
        # idx is 1-indexed position in last level
        # Convert to 0-indexed for binary search
        idx -= 1
        left, right = 0, (1 << h) - 1

        for _ in range(h):
            mid = (left + right) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1

        return node is not None


# Simple O(n) solution for comparison
class SolutionNaive:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


def print_tree_visual(lst):
    """Simple tree visualization for small trees"""
    if not lst:
        print("(empty)")
        return

    height = 0
    nodes_at_level = 1
    i = 0

    while i < len(lst):
        level_nodes = lst[i:i + nodes_at_level]
        # Format the level nicely
        formatted = []
        for node in level_nodes:
            if node is None:
                formatted.append("N")
            else:
                formatted.append(str(node))

        # Calculate indentation
        spaces = " " * ((2 ** (3 - height)) - 2) if height < 4 else " "
        print(f"Level {height}: {spaces}{' '.join(formatted)}")

        i += nodes_at_level
        nodes_at_level *= 2
        height += 1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()
    naive = SolutionNaive()

    test_cases = [
        # (tree_list, expected_count, test_name)
        ([1, 2, 3, 4, 5, 6], 6, "Example 1"),
        ([], 0, "Example 2 - Empty tree"),
        ([1], 1, "Example 3 - Single node"),
        ([1, 2, 3, 4], 4, "Complete tree with 4 nodes"),
        ([1, 2, 3, 4, 5], 5, "Complete tree with 5 nodes"),
        ([1, 2, 3, 4, 5, 6, 7], 7, "Perfect binary tree (height 2)"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15, "Perfect binary tree (height 3)"),
        ([1, 2, 3, 4, 5, 6, 7, 8], 8, "Complete tree height 3, full last level"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, "Complete tree height 3, partial last level"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, "Complete tree with 10 nodes"),
    ]

    print("Testing Count Complete Tree Nodes:")
    print("=" * 70)

    for tree_list, expected, test_name in test_cases:
        print(f"\nTest: {test_name}")
        print(f"Tree: {tree_list}")

        if tree_list:
            tree = create_complete_tree_from_list(tree_list)
            result = solution.countNodes(tree)
            result2 = solution2.countNodes(tree)
            naive_result = naive.countNodes(tree)
        else:
            result = result2 = naive_result = 0

        print(f"Solution 1 (height comparison): {result}")
        print(f"Solution 2 (binary search):     {result2}")
        print(f"Naive O(n) solution:           {naive_result}")
        print(f"Expected:                      {expected}")

        all_correct = result == expected and result2 == expected and naive_result == expected
        status = "✓ ALL PASS" if all_correct else "✗ SOME FAIL"
        if result2 != expected:
            status += " (Solution 2 failed)"
        print(f"Status: {status}")

        if len(tree_list) <= 7:
            print("Tree visualization:")
            print_tree_visual(tree_list)

    print("\n" + "=" * 70)

    # Let's debug the failing test case
    print("\nDebugging Example 1 ([1,2,3,4,5,6]):")
    print("-" * 40)
    tree = create_complete_tree_from_list([1, 2, 3, 4, 5, 6])

    # Show tree structure
    print("Tree structure:")
    print("""
        1
       / \\
      2   3
     / \\  /
    4  5 6
    """)

    # Solution 1 calculation
    print("\nSolution 1 calculation:")
    print("Left height from root (following left): 1->2->4 = 3")
    print("Right height from root (following right): 1->3 = 2")
    print("Heights differ (3 != 2), so recursively count:")
    print("Total = 1 + count(left) + count(right)")

    # Manually calculate
    print("\nLeft subtree [2,4,5]:")
    print("    2")
    print("   / \\")
    print("  4   5")
    print("Left height: 2->4 = 2")
    print("Right height: 2->5 = 2")
    print("Equal heights → perfect tree: 2² - 1 = 3 nodes")

    print("\nRight subtree [3,6]:")
    print("    3")
    print("   /")
    print("  6")
    print("Left height: 3->6 = 2")
    print("Right height: 3 = 1")
    print("Heights differ, so recursively:")
    print("count([3,6]) = 1 + count([6]) + count([])")
    print("count([6]) = 1 (single node)")
    print("count([3,6]) = 1 + 1 + 0 = 2")

    print("\nTotal = 1 + 3 + 2 = 6")

    # Solution 2 calculation
    print("\n" + "=" * 70)
    print("Solution 2 (Binary Search) calculation:")
    print("Height h (following left from root): 1->2->4 = 3 levels")
    print("But for binary search, we use h = number of edges = 2")
    print("Perfect tree of height 2 has 2² - 1 = 3 nodes")
    print("Last level can have up to 2² = 4 nodes")
    print("Binary search to find how many nodes in last level...")

    # Debug Solution 2
    print("\nChecking Solution 2 implementation:")
    sol2 = Solution2()
    h = sol2.get_left_height(tree)
    print(f"h = {h} (should be 2 for tree height)")

    # Check node_exists for different positions
    print("\nChecking if nodes exist at positions in last level:")
    for i in range(1, 5):
        exists = sol2.node_exists(tree, h, i)
        print(f"Position {i}: {'Exists' if exists else 'Missing'}")

    # Binary search simulation
    print("\nBinary search simulation:")
    left, right = 1, 4
    while left < right:
        mid = (left + right + 1) // 2
        exists = sol2.node_exists(tree, h, mid)
        print(f"Checking position {mid}: {'Exists' if exists else 'Missing'}")
        if exists:
            left = mid
        else:
            right = mid - 1
    print(f"Last level has {left} nodes")
    print(f"Total = (2^{h} - 1) + {left} = {(1 << h) - 1} + {left} = {(1 << h) - 1 + left}")