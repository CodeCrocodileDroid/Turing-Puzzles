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
    def zigzagLevelOrder(self, root):
        """BFS with direction flag"""
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True  # Start with left to right

        while queue:
            level_size = len(queue)
            level_nodes = deque()  # Use deque for efficient appending

            for _ in range(level_size):
                node = queue.popleft()

                # Add node based on current direction
                if left_to_right:
                    level_nodes.append(node.val)  # Append to end
                else:
                    level_nodes.appendleft(node.val)  # Append to front

                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level_nodes))
            left_to_right = not left_to_right  # Reverse direction

        return result


class Solution2:
    def zigzagLevelOrder(self, root):
        """BFS with reverse"""
        if not root:
            return []

        result = []
        queue = deque([root])
        level = 0

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

            # Reverse every other level
            if level % 2 == 1:
                level_nodes.reverse()

            result.append(level_nodes)
            level += 1

        return result


class Solution3:
    def zigzagLevelOrder(self, root):
        """DFS Recursive"""
        result = []

        def dfs(node, depth):
            if not node:
                return

            # Add new level list if needed
            if depth == len(result):
                result.append([])

            # Add node to appropriate position based on depth
            if depth % 2 == 0:  # Even depth: left to right
                result[depth].append(node.val)
            else:  # Odd depth: right to left
                result[depth].insert(0, node.val)

            # Recursively process children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result


# Test cases
if __name__ == "__main__":
    solution1 = Solution()  # BFS with direction flag
    solution2 = Solution2()  # BFS with reverse
    solution3 = Solution3()  # DFS recursive

    test_cases = [
        # (tree_list, expected, test_name)
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]], "Example 1"),
        ([1], [[1]], "Example 2"),
        ([], [], "Example 3 - Empty tree"),
        ([1, 2, 3], [[1], [3, 2]], "Simple 3-node tree"),
        ([1, 2, 3, 4, 5], [[1], [3, 2], [4, 5]], "Complete tree with 5 nodes"),
        ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]], "Tree with missing nodes"),
        ([1, 2, None, 3, None, 4], [[1], [2], [3], [4]], "Left-skewed tree"),
        ([1, None, 2, None, 3, None, 4], [[1], [2], [3], [4]], "Right-skewed tree"),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [3, 2], [4, 5, 6, 7]], "Perfect binary tree"),
        ([1, 2, 3, None, 4, 5, 6], [[1], [3, 2], [4, 5, 6]], "Complex tree"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
         [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]],
         "Large perfect tree"),
    ]

    print("Testing Binary Tree Zigzag Level Order Traversal")
    print("=" * 70)

    for i, (tree_list, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Tree list: {tree_list}")

        if tree_list:
            root = create_tree_from_list(tree_list)

            result1 = solution1.zigzagLevelOrder(root)
            result2 = solution2.zigzagLevelOrder(root)
            result3 = solution3.zigzagLevelOrder(root)

            print(f"\nBFS (direction flag): {result1}")
            print(f"BFS (reverse):        {result2}")
            print(f"DFS (recursive):      {result3}")
            print(f"Expected:             {expected}")

            match1 = result1 == expected
            match2 = result2 == expected
            match3 = result3 == expected

            if match1 and match2 and match3:
                print("✓ ALL SOLUTIONS PASS")
            else:
                status = []
                if match1:
                    status.append("✓ BFS(flag)")
                else:
                    status.append("✗ BFS(flag)")

                if match2:
                    status.append("✓ BFS(reverse)")
                else:
                    status.append("✗ BFS(reverse)")

                if match3:
                    status.append("✓ DFS")
                else:
                    status.append("✗ DFS")

                print("Status: " + " | ".join(status))

            # Show visualization for small examples
            if len(tree_list) <= 10 and test_name in ["Example 1", "Simple 3-node tree"]:
                print("\nTree and Zigzag Traversal:")
                if tree_list == [3, 9, 20, None, None, 15, 7]:
                    print("""
    Tree Structure:
          3
         / \\
        9   20
           /  \\
          15   7

    Zigzag Level Order:
    Level 0 (left→right): [3]
    Level 1 (right→left): [20, 9]   (reversed)
    Level 2 (left→right): [15, 7]
                    """)
                elif tree_list == [1, 2, 3]:
                    print("""
    Tree Structure:
          1
         / \\
        2   3

    Zigzag Level Order:
    Level 0 (left→right): [1]
    Level 1 (right→left): [3, 2]   (reversed)
                    """)
        else:
            print("Tree: (empty)")
            result1 = solution1.zigzagLevelOrder(None)
            result2 = solution2.zigzagLevelOrder(None)
            result3 = solution3.zigzagLevelOrder(None)

            print(f"\nBFS (direction flag): {result1}")
            print(f"BFS (reverse):        {result2}")
            print(f"DFS (recursive):      {result3}")
            print(f"Expected:             {expected}")

            if result1 == expected and result2 == expected and result3 == expected:
                print("✓ ALL SOLUTIONS PASS")
            else:
                print("✗ SOME SOLUTIONS FAIL")

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Solution 1 (BFS with direction flag):
1. Use BFS level order traversal
2. Track direction with boolean flag (left_to_right)
3. Use deque for level nodes to append front/back efficiently
4. For left→right: append to end (normal order)
5. For right→left: append to front (reverse order)
6. Toggle direction after each level

Solution 2 (BFS with reverse):
1. Do normal level order traversal
2. Collect nodes in list for each level
3. Reverse the list for odd-numbered levels (1, 3, 5...)
4. Simple but reversing takes O(k) for level of size k

Solution 3 (DFS Recursive):
1. Recursively traverse tree with depth tracking
2. For even depths: append to end (left→right)
3. For odd depths: insert at front (right→left)
4. Note: insert(0) is O(n) for each insertion
""")

    print("\nTime Complexity Analysis:")
    print("-" * 40)
    print("All solutions: O(n) time (visit each node once)")
    print("Space Complexity:")
    print("- BFS solutions: O(w) where w is max width")
    print("- DFS solution: O(h) where h is height (recursion stack)")
    print("\nNote: Solution 3 (DFS) uses insert(0) which is O(k) per insertion,")
    print("      making it O(n²) in worst case for skewed trees.")

    print("\n" + "=" * 70)

    # Step-by-step demonstration
    print("\nStep-by-step Demonstration for Example 1:")
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

    print("\nSolution 1 (BFS with direction flag) execution:")
    print("1. Initialize: queue = [3], left_to_right = True, result = []")
    print("2. Level 0 (depth 0, left→right):")
    print("   - level_nodes = deque()")
    print("   - Process 3: append(3) → level_nodes = [3]")
    print("   - Add children 9, 20 to queue")
    print("   - result = [[3]], toggle direction → left_to_right = False")
    print("3. Level 1 (depth 1, right→left):")
    print("   - queue = [9, 20], level_nodes = deque()")
    print("   - Process 9: appendleft(9) → level_nodes = [9]")
    print("   - Process 20: appendleft(20) → level_nodes = [20, 9]")
    print("   - Add children 15, 7 to queue")
    print("   - result = [[3], [20, 9]], toggle direction → left_to_right = True")
    print("4. Level 2 (depth 2, left→right):")
    print("   - queue = [15, 7], level_nodes = deque()")
    print("   - Process 15: append(15) → level_nodes = [15]")
    print("   - Process 7: append(7) → level_nodes = [15, 7]")
    print("   - result = [[3], [20, 9], [15, 7]]")

    final_result = solution1.zigzagLevelOrder(demo_root)
    print(f"\nFinal Result: {final_result}")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)
    print("""
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = deque()

            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level_nodes))
            left_to_right = not left_to_right

        return result
    """)

# Performance comparison
print("\n" + "=" * 70)
print("Performance Comparison:")
print("=" * 70)

print("""
1. Solution 1 (BFS with direction flag):
   - Uses deque for efficient front/back appends
   - No reversing needed
   - O(n) time, O(w) space
   - Most efficient

2. Solution 2 (BFS with reverse):
   - Simpler logic
   - Uses list.reverse() which is O(k) for level size k
   - Still O(n) overall
   - Good balance of simplicity and efficiency

3. Solution 3 (DFS recursive):
   - Clean recursive solution
   - Uses insert(0) which is O(k) for each insertion
   - Can be O(n²) for skewed trees
   - Not recommended for large trees

For LeetCode, Solution 1 or 2 are both good choices.
""")