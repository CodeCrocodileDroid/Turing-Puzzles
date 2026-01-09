from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


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
    def averageOfLevels(self, root):
        """BFS Level Order Traversal"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate average for this level
            # Using float() to ensure floating point division
            result.append(float(level_sum) / level_size)

        return result


class Solution2:
    def averageOfLevels(self, root):
        """DFS Recursive Solution"""
        if not root:
            return []

        levels = []  # Each element is [sum, count]

        def dfs(node, depth):
            if not node:
                return

            # Initialize level data if needed
            if depth == len(levels):
                levels.append([0, 0])

            # Add node value to level sum and increment count
            levels[depth][0] += node.val
            levels[depth][1] += 1

            # Recursively process children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        # Calculate averages
        return [float(total) / count for total, count in levels]


class Solution3:
    def averageOfLevels(self, root):
        """Alternative BFS without deque"""
        if not root:
            return []

        result = []
        current_level = [root]

        while current_level:
            next_level = []
            level_sum = 0
            level_count = len(current_level)

            # Process current level
            for node in current_level:
                level_sum += node.val

                # Prepare next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # Calculate average
            result.append(float(level_sum) / level_count)

            # Move to next level
            current_level = next_level

        return result


def print_tree_visual(lst):
    """Print tree in a visual format"""
    if not lst:
        print("(empty tree)")
        return

    height = 0
    level_nodes = []
    i = 0

    print("Tree structure:")
    while i < len(lst):
        # Get nodes at current level
        current_level = []
        for j in range(min(2 ** height, len(lst) - i)):
            if lst[i + j] is None:
                current_level.append("N")
            else:
                current_level.append(str(lst[i + j]))
        level_nodes.append(current_level)
        i += 2 ** height
        height += 1

    # Print levels
    for h in range(len(level_nodes)):
        indent = " " * (2 ** (len(level_nodes) - h - 1) - 1)
        spacing = " " * (2 ** (len(level_nodes) - h) - 1)
        print(f"Level {h}: {indent}{spacing.join(level_nodes[h])}")


# Test cases
if __name__ == "__main__":
    solution_bfs = Solution()
    solution_dfs = Solution2()
    solution_bfs2 = Solution3()

    test_cases = [
        # (tree_list, expected, test_name)
        ([3, 9, 20, None, None, 15, 7], [3.0, 14.5, 11.0], "Example 1"),
        ([3, 9, 20, 15, 7], [3.0, 14.5, 11.0], "Example 2"),
        ([], [], "Empty tree"),
        ([5], [5.0], "Single node"),
        ([1, 2, 3], [1.0, 2.5], "Simple 3-node tree"),
        ([3, 9, 20, 15, 7, 8, 9], [3.0, 14.5, 10.0], "7-node tree"),
        ([1, 2, 3, 4, 5, 6, 7], [1.0, 2.5, 5.5], "Perfect binary tree"),
        ([2147483647, 2147483647, 2147483647], [2147483647.0, 2147483647.0], "Large values"),
        ([1, 2, None, 3, None, 4], [1.0, 2.0, 3.0, 4.0], "Left-skewed tree"),
        ([1, None, 2, None, 3, None, 4], [1.0, 2.0, 3.0, 4.0], "Right-skewed tree"),
    ]

    print("Testing Average of Levels in Binary Tree")
    print("=" * 70)

    for i, (tree_list, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Tree list: {tree_list}")

        if tree_list:
            # Print tree structure
            print_tree_visual(tree_list)

            # Create tree and calculate results
            root = create_tree_from_list(tree_list)

            result_bfs = solution_bfs.averageOfLevels(root)
            result_dfs = solution_dfs.averageOfLevels(root)
            result_bfs2 = solution_bfs2.averageOfLevels(root)


            # Format results for display (5 decimal places)
            def format_result(res):
                return [format(val, ".5f") for val in res]


            print(f"\nBFS (deque) Result:   {format_result(result_bfs)}")
            print(f"DFS Result:           {format_result(result_dfs)}")
            print(f"BFS (list) Result:    {format_result(result_bfs2)}")
            print(f"Expected:             {format_result(expected)}")

            # Check if results match expected (within tolerance)
            tolerance = 1e-5


            def results_match(res1, res2):
                if len(res1) != len(res2):
                    return False
                for a, b in zip(res1, res2):
                    if abs(a - b) > tolerance:
                        return False
                return True


            bfs_match = results_match(result_bfs, expected)
            dfs_match = results_match(result_dfs, expected)
            bfs2_match = results_match(result_bfs2, expected)

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

            # Show detailed calculation for example cases
            if test_name in ["Example 1", "Example 2", "Simple 3-node tree"]:
                print("\nDetailed Calculation:")
                if tree_list == [3, 9, 20, None, None, 15, 7]:
                    print("""
    Level 0: [3] 
      Sum = 3, Count = 1 → Average = 3.0

    Level 1: [9, 20]
      Sum = 9 + 20 = 29, Count = 2 → Average = 29/2 = 14.5

    Level 2: [15, 7]
      Sum = 15 + 7 = 22, Count = 2 → Average = 22/2 = 11.0
                    """)
                elif tree_list == [1, 2, 3]:
                    print("""
    Level 0: [1]
      Sum = 1, Count = 1 → Average = 1.0

    Level 1: [2, 3]
      Sum = 2 + 3 = 5, Count = 2 → Average = 5/2 = 2.5
                    """)
        else:
            print("Tree: (empty)")
            result_bfs = solution_bfs.averageOfLevels(None)
            result_dfs = solution_dfs.averageOfLevels(None)
            result_bfs2 = solution_bfs2.averageOfLevels(None)

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
2. For each level:
   - Get the number of nodes at that level
   - Sum all node values at that level
   - Calculate average = sum / count
   - Add to result list
3. Continue until queue is empty

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(w) where w is maximum width of tree

Solution 2 (DFS Recursive):
1. Recursively traverse the tree
2. Track depth of each node
3. Maintain list of [sum, count] for each level
4. After traversal, calculate averages = sum / count for each level

Time Complexity: O(n)
Space Complexity: O(h) where h is height (recursion stack)

Solution 3 (BFS with lists):
1. Similar to Solution 1 but uses lists instead of deque
2. Keep two lists: current level and next level
3. Process current level, build next level
4. Calculate average after processing each level

Time Complexity: O(n)
Space Complexity: O(w)
    """)

    print("\n" + "=" * 70)

    # Interactive demo
    print("\nInteractive Demo:")
    print("=" * 70)

    demo_tree = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    print("Demo Tree: [3, 9, 20, None, None, 15, 7]")
    print("""
    Tree Structure:
          3
         / \\
        9   20
           /  \\
          15   7
    """)

    print("Calculating averages level by level:")

    # Simulate BFS step by step
    result = solution_bfs.averageOfLevels(demo_tree)
    print(f"Final Result: {[format(val, '.5f') for val in result]}")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nCode for LeetCode Submission:")
    print("=" * 70)
    print("""
from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(float(level_sum) / level_size)

        return result
    """)


# Additional helper to verify calculations
def manual_calculation(tree_list):
    """Manually calculate level averages for verification"""
    if not tree_list:
        return []

    levels = []
    i = 0
    level = 0

    while i < len(tree_list):
        # Get nodes at current level
        level_nodes = []
        for j in range(min(2 ** level, len(tree_list) - i)):
            val = tree_list[i + j]
            if val is not None:
                level_nodes.append(val)

        if level_nodes:  # Only add if there are non-None nodes
            level_sum = sum(level_nodes)
            level_avg = float(level_sum) / len(level_nodes)
            levels.append(level_avg)

        i += 2 ** level
        level += 1

    return levels


# Verify with manual calculation
print("\n" + "=" * 70)
print("Verification with Manual Calculation:")
print("=" * 70)

test_tree = [3, 9, 20, None, None, 15, 7]
manual_result = manual_calculation(test_tree)
print(f"Tree: {test_tree}")
print(f"Manual calculation: {[format(val, '.5f') for val in manual_result]}")
print(f"Matches expected: {[format(val, '.5f') for val in [3.0, 14.5, 11.0]]}")