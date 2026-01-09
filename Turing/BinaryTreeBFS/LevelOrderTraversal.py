from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    def levelOrder(self, root):
        """BFS Solution"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result


class Solution2:
    def levelOrder(self, root):
        """DFS Recursive Solution"""
        result = []

        def dfs(node, depth):
            if not node:
                return

            # Add new level list if needed
            if depth == len(result):
                result.append([])

            # Add current node to its level
            result[depth].append(node.val)

            # Recursively process children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result


class Solution3:
    def levelOrder(self, root):
        """BFS without deque (using lists)"""
        if not root:
            return []

        result = []
        current_level = [root]

        while current_level:
            next_level = []
            level_values = []

            for node in current_level:
                level_values.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(level_values)
            current_level = next_level

        return result


# Test cases
if __name__ == "__main__":
    solution_bfs = Solution()
    solution_dfs = Solution2()
    solution_bfs2 = Solution3()

    test_cases = [
        # (tree_list, expected, test_name)
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]], "Example 1"),
        ([1], [[1]], "Example 2"),
        ([], [], "Example 3 - Empty tree"),
        ([1, 2, 3], [[1], [2, 3]], "Simple 3-node tree"),
        ([1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]], "Complete tree with 5 nodes"),
        ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]], "Tree with missing nodes"),
        ([1, 2, None, 3, None, 4], [[1], [2], [3], [4]], "Left-skewed tree"),
        ([1, None, 2, None, 3, None, 4], [[1], [2], [3], [4]], "Right-skewed tree"),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]], "Perfect binary tree"),
        ([1, 2, 3, None, 4, 5, 6], [[1], [2, 3], [4, 5, 6]], "Complex tree"),
    ]

    print("Testing Binary Tree Level Order Traversal")
    print("=" * 70)

    for i, (tree_list, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Tree list: {tree_list}")

        if tree_list:
            root = create_tree_from_list(tree_list)

            result_bfs = solution_bfs.levelOrder(root)
            result_dfs = solution_dfs.levelOrder(root)
            result_bfs2 = solution_bfs2.levelOrder(root)

            print(f"\nBFS (deque) Result:   {result_bfs}")
            print(f"DFS Result:           {result_dfs}")
            print(f"BFS (list) Result:    {result_bfs2}")
            print(f"Expected:             {expected}")

            bfs_match = result_bfs == expected
            dfs_match = result_dfs == expected
            bfs2_match = result_bfs2 == expected

            if bfs_match and dfs_match and bfs2_match:
                print("✓ ALL SOLUTIONS PASS")
            else:
                status = []
                if bfs_match:
                    status.append("✓ BFS(deque)")
                else:
                    status.append("✗ BFS(deque)")

                if dfs_match:
                    status.append("✓ DFS")
                else:
                    status.append("✗ DFS")

                if bfs2_match:
                    status.append("✓ BFS(list)")
                else:
                    status.append("✗ BFS(list)")

                print("Status: " + " | ".join(status))

            # Show tree visualization for small examples
            if len(tree_list) <= 10 and test_name in ["Example 1", "Simple 3-node tree"]:
                print("\nTree Visualization:")
                if tree_list == [3, 9, 20, None, None, 15, 7]:
                    print("""
        3
       / \\
      9   20
         /  \\
        15   7
                    """)
                    print("Level Order Traversal:")
                    print("Level 0: [3]")
                    print("Level 1: [9, 20]")
                    print("Level 2: [15, 7]")
                elif tree_list == [1, 2, 3]:
                    print("""
        1
       / \\
      2   3
                    """)
                    print("Level Order Traversal:")
                    print("Level 0: [1]")
                    print("Level 1: [2, 3]")
        else:
            print("Tree: (empty)")
            result_bfs = solution_bfs.levelOrder(None)
            result_dfs = solution_dfs.levelOrder(None)
            result_bfs2 = solution_bfs2.levelOrder(None)

            print(f"\nBFS (deque) Result: {result_bfs}")
            print(f"DFS Result:         {result_dfs}")
            print(f"BFS (list) Result:  {result_bfs2}")
            print(f"Expected:           {expected}")

            if result_bfs == expected and result_dfs == expected and result_bfs2 == expected:
                print("✓ ALL SOLUTIONS PASS")
            else:
                print("✗ SOME SOLUTIONS FAIL")

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Solution 1 (BFS with deque):
1. Use a queue to process nodes level by level
2. Start with root in queue
3. For each level:
   - Get number of nodes at current level (queue size)
   - Process each node:
     * Add value to current level list
     * Add left and right children to queue
   - Add level list to result
4. Continue until queue is empty

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(w) where w is maximum width of tree

Solution 2 (DFS Recursive):
1. Recursively traverse the tree
2. Track depth of each node
3. Add node value to appropriate level in result list
4. Create new level list when reaching new depth

Time Complexity: O(n)
Space Complexity: O(h) where h is height (recursion stack)

Solution 3 (BFS with lists):
1. Similar to BFS but uses two lists instead of queue
2. current_level stores nodes at current level
3. next_level stores nodes for next level
4. Process level by level

Time Complexity: O(n)
Space Complexity: O(w)
    """)

    print("\n" + "=" * 70)

    # Step-by-step demonstration
    print("\nStep-by-step BFS Demonstration for Example 1:")
    print("=" * 70)

    demo_root = create_tree_from_list([3, 9, 20, None, None, 15, 7])

    print("Tree: [3, 9, 20, None, None, 15, 7]")
    print("""
        3
       / \\
      9   20
         /  \\
        15   7
    """)

    print("\nBFS Execution Steps:")
    print("1. Initialize: queue = [3], result = []")
    print("2. Level 0:")
    print("   - Process level size = 1")
    print("   - Pop 3, add to level_nodes = [3]")
    print("   - Add children 9 and 20 to queue")
    print("   - result = [[3]]")
    print("3. Level 1:")
    print("   - Process level size = 2")
    print("   - Pop 9, add to level_nodes = [9]")
    print("   - 9 has no children")
    print("   - Pop 20, add to level_nodes = [9, 20]")
    print("   - Add children 15 and 7 to queue")
    print("   - result = [[3], [9, 20]]")
    print("4. Level 2:")
    print("   - Process level size = 2")
    print("   - Pop 15, add to level_nodes = [15]")
    print("   - 15 has no children")
    print("   - Pop 7, add to level_nodes = [15, 7]")
    print("   - 7 has no children")
    print("   - result = [[3], [9, 20], [15, 7]]")
    print("5. Queue is empty, return result")

    final_result = solution_bfs.levelOrder(demo_root)
    print(f"\nFinal Result: {final_result}")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)
    print("""
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result
    """)

# Additional: Different variations
print("\n" + "=" * 70)
print("Variations of Level Order Traversal:")
print("=" * 70)

print("""
1. Reverse Level Order (bottom-up):
   - Do normal level order, then reverse result
   - Or use BFS with stack

2. Zigzag Level Order:
   - Alternate direction each level
   - Use deque and append left/right based on level

3. Level Order with Null markers:
   - Include null values in result
   - Useful for serialization

4. Level Order with Depth info:
   - Return tuples (depth, value) or structured data
""")

# Performance comparison
print("\n" + "=" * 70)
print("Performance Considerations:")
print("=" * 70)

print("""
1. BFS (deque):
   - Fast for level-order traversal
   - Uses O(w) memory for queue
   - deque.popleft() is O(1)

2. DFS (recursive):
   - Simpler code
   - Uses recursion stack O(h)
   - Might cause stack overflow for deep trees

3. BFS (lists):
   - No deque dependency
   - Slightly more memory due to two lists
   - Still O(n) time

For most cases, BFS with deque is recommended.
""")