# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


from collections import deque


class Solution:
    def rightSideView(self, root):
        """BFS Level Order Traversal"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()

                # If this is the last node at this level, add to result
                if i == level_size - 1:
                    result.append(node.val)

                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


class Solution2:
    def rightSideView(self, root):
        """DFS Recursive Solution"""
        result = []

        def dfs(node, depth):
            if not node:
                return

            # If this is the first node at this depth, add it
            if depth == len(result):
                result.append(node.val)

            # Traverse right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
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


def visualize_tree(root, level=0, prefix="Root: "):
    """Visualize tree structure"""
    if not root:
        return

    print(" " * (level * 4) + prefix + str(root.val))
    if root.left or root.right:
        if root.left:
            visualize_tree(root.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        if root.right:
            visualize_tree(root.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")


# Test cases
if __name__ == "__main__":
    solution_bfs = Solution()
    solution_dfs = Solution2()

    test_cases = [
        # (tree_list, expected, test_name)
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4], "Example 1"),
        ([1, None, 3], [1, 3], "Example 2"),
        ([], [], "Empty tree"),
        ([1], [1], "Single node"),
        ([1, 2, 3, 4], [1, 3, 4], "Tree with 4 nodes"),
        ([1, 2, 3, None, 5, None, 4, None, None, 6], [1, 3, 4, 6], "Complex tree"),
        ([1, 2, 3, None, 5, 6], [1, 3, 6], "Multiple rightmost nodes"),
        ([1, 2, 3, 4, None, None, 5, None, None, None, None, 6], [1, 3, 5, 6], "Deep tree"),
        ([1, 2, 3, None, 5, None, 4, 6], [1, 3, 4, 6], "Tree with rightmost at different depths"),
    ]

    print("Testing Binary Tree Right Side View:")
    print("=" * 70)

    for i, (tree_list, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Tree: {tree_list}")

        if tree_list:
            root = create_tree_from_list(tree_list)

            print("\nTree Structure:")
            visualize_tree(root)

            result_bfs = solution_bfs.rightSideView(root)
            result_dfs = solution_dfs.rightSideView(root)

            print(f"\nBFS Result: {result_bfs}")
            print(f"DFS Result: {result_dfs}")
            print(f"Expected:   {expected}")

            bfs_correct = result_bfs == expected
            dfs_correct = result_dfs == expected

            if bfs_correct and dfs_correct:
                print(f"Status: ✓ BOTH PASS")
            elif bfs_correct:
                print(f"Status: ✓ BFS PASS, ✗ DFS FAIL")
            elif dfs_correct:
                print(f"Status: ✗ BFS FAIL, ✓ DFS PASS")
            else:
                print(f"Status: ✗ BOTH FAIL")
        else:
            print("\nTree Structure: (empty)")
            result_bfs = solution_bfs.rightSideView(None)
            result_dfs = solution_dfs.rightSideView(None)

            print(f"\nBFS Result: {result_bfs}")
            print(f"DFS Result: {result_dfs}")
            print(f"Expected:   {expected}")

            if result_bfs == expected and result_dfs == expected:
                print(f"Status: ✓ BOTH PASS")
            else:
                print(f"Status: ✗ SOME FAIL")

        # Show explanation for the first few test cases
        if i < 2 and tree_list:
            print("\nExplanation:")
            if tree_list == [1, 2, 3, None, 5, None, 4]:
                print("""
    Tree:
        1
       / \\
      2   3
       \\   \\
        5   4

    Right side view:
    Level 0: Node 1 (only node)
    Level 1: Node 3 (rightmost of level 1)
    Level 2: Node 4 (rightmost of level 2)
    Result: [1, 3, 4]
                """)
            elif tree_list == [1, None, 3]:
                print("""
    Tree:
        1
         \\
          3

    Right side view:
    Level 0: Node 1
    Level 1: Node 3
    Result: [1, 3]
                """)

    print("\n" + "=" * 70)

    # Algorithm comparison
    print("\nAlgorithm Comparison:")
    print("=" * 70)
    print("""
BFS (Level Order Traversal):
1. Use queue to process nodes level by level
2. For each level, track the last node
3. Add last node of each level to result
4. Time: O(n), Space: O(w) where w is max width

DFS (Recursive):
1. Traverse tree with depth-first search
2. Visit right child before left child
3. Track depth, add first node seen at each depth
4. Time: O(n), Space: O(h) where h is height (recursion stack)

Both give same result but different approaches!
    """)

    print("\n" + "=" * 70)

    # Interactive example
    print("\nInteractive Example:")
    print("=" * 70)

    example_tree = create_tree_from_list([1, 2, 3, None, 5, None, 4])
    print("Example Tree: [1, 2, 3, None, 5, None, 4]")
    print("\nVisual Representation:")
    print("""
        1
       / \\
      2   3
       \\   \\
        5   4
    """)

