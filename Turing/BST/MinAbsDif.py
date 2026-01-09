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
    def getMinimumDifference(self, root):
        """Inorder traversal with O(1) extra space"""
        self.min_diff = float('inf')
        self.prev = None

        def inorder(node):
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)

            self.prev = node.val

            # Traverse right subtree
            inorder(node.right)

        inorder(root)
        return self.min_diff


class Solution2:
    def getMinimumDifference(self, root):
        """Inorder traversal with list"""
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

        return min_diff


class Solution3:
    def getMinimumDifference(self, root):
        """Iterative inorder traversal"""
        min_diff = float('inf')
        prev = None
        stack = []
        current = root

        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()

            if prev is not None:
                min_diff = min(min_diff, current.val - prev)

            prev = current.val

            # Move to right subtree
            current = current.right

        return min_diff


# Test cases
if __name__ == "__main__":
    solution1 = Solution()  # Recursive inorder with O(1) space
    solution2 = Solution2()  # Inorder with list
    solution3 = Solution3()  # Iterative inorder

    test_cases = [
        # (tree_list, expected, test_name)
        ([4, 2, 6, 1, 3], 1, "Example 1"),
        ([1, 0, 48, None, None, 12, 49], 1, "Example 2"),
        ([1, None, 3, 2], 1, "Simple 3-node tree"),
        ([1, 0], 1, "Two nodes"),
        ([5, 3, 7, 2, 4, 6, 8], 1, "Balanced BST"),
        ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 1, "Complex BST"),
        ([236, 104, 701, None, 227, None, 911], 9, "BST with larger difference"),
        ([0, None, 2236, 1277, 2776, 519], 519, "Another complex BST"),
        ([1, None, 5, 3], 2, "BST with difference 2"),
        ([543, 384, 652, None, 445, None, 699], 47, "Random BST"),
    ]

    print("Testing Minimum Absolute Difference in BST")
    print("=" * 70)

    for i, (tree_list, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Tree list: {tree_list}")

        if tree_list:
            root = create_tree_from_list(tree_list)

            result1 = solution1.getMinimumDifference(root)
            result2 = solution2.getMinimumDifference(root)
            result3 = solution3.getMinimumDifference(root)

            print(f"\nRecursive Inorder (O1 space): {result1}")
            print(f"Inorder with List:            {result2}")
            print(f"Iterative Inorder:            {result3}")
            print(f"Expected:                     {expected}")

            match1 = result1 == expected
            match2 = result2 == expected
            match3 = result3 == expected

            if match1 and match2 and match3:
                print("✓ ALL SOLUTIONS PASS")
            else:
                status = []
                if match1:
                    status.append("✓ Recursive")
                else:
                    status.append("✗ Recursive")

                if match2:
                    status.append("✓ With List")
                else:
                    status.append("✗ With List")

                if match3:
                    status.append("✓ Iterative")
                else:
                    status.append("✗ Iterative")

                print("Status: " + " | ".join(status))

            # Show inorder traversal and calculation for examples
            if test_name in ["Example 1", "Example 2", "Simple 3-node tree"]:
                print("\nDetailed Calculation:")


                # Get inorder traversal
                def get_inorder(node):
                    if not node:
                        return []
                    return get_inorder(node.left) + [node.val] + get_inorder(node.right)


                inorder_vals = get_inorder(root)
                print(f"Inorder traversal (sorted): {inorder_vals}")

                # Calculate differences
                differences = []
                for j in range(1, len(inorder_vals)):
                    diff = inorder_vals[j] - inorder_vals[j - 1]
                    differences.append(diff)

                print(f"Differences between consecutive nodes: {differences}")
                print(f"Minimum difference: {min(differences)}")

                # Show tree structure for small trees
                if len(tree_list) <= 7:
                    print("\nTree Structure (BST):")
                    if tree_list == [4, 2, 6, 1, 3]:
                        print("""
        4
       / \\
      2   6
     / \\
    1   3
                        """)
                        print("Inorder: 1, 2, 3, 4, 6")
                        print("Differences: (2-1)=1, (3-2)=1, (4-3)=1, (6-4)=2")
                        print("Minimum: 1")
                    elif tree_list == [1, 0, 48, None, None, 12, 49]:
                        print("""
        1
       / \\
      0   48
         /  \\
        12   49
                        """)
                        print("Inorder: 0, 1, 12, 48, 49")
                        print("Differences: (1-0)=1, (12-1)=11, (48-12)=36, (49-48)=1")
                        print("Minimum: 1")
        else:
            print("Tree: (empty)")
            # Note: Problem says at least 2 nodes, so empty not in test cases

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Key Insight: In a Binary Search Tree (BST), inorder traversal gives sorted values.

Solution 1 (Recursive Inorder with O(1) space):
1. Perform inorder traversal (left, root, right)
2. Track previous node value
3. At each node, calculate difference with previous
4. Update minimum difference
5. Time: O(n), Space: O(h) (recursion stack)

Solution 2 (Inorder with List):
1. Collect all values in inorder traversal
2. Values will be sorted
3. Find minimum difference between consecutive values
4. Time: O(n), Space: O(n)

Solution 3 (Iterative Inorder):
1. Use stack to simulate inorder traversal
2. Same logic as Solution 1 but iterative
3. Time: O(n), Space: O(h)
""")

    print("\nWhy Inorder Traversal Works:")
    print("-" * 40)
    print("""
In a BST:
1. Left subtree contains values < node value
2. Right subtree contains values > node value
3. Inorder traversal visits nodes in sorted order

For minimum absolute difference:
- Minimum difference will be between two consecutive values in sorted order
- Because if a < b < c, then:
  - |b - a| ≤ |c - a|
  - |c - b| ≤ |c - a|
- So we only need to check consecutive pairs
""")

    print("\n" + "=" * 70)

    # Step-by-step demonstration
    print("\nStep-by-step Demonstration for Example 1:")
    print("=" * 70)

    demo_root = create_tree_from_list([4, 2, 6, 1, 3])

    print("Tree: [4, 2, 6, 1, 3] (BST)")
    print("""
        4
       / \\
      2   6
     / \\
    1   3
    """)

    print("\nSolution 1 Execution (Recursive Inorder):")
    print("min_diff = ∞, prev = None")
    print("\nInorder Traversal:")
    print("1. Go to leftmost: 4→2→1")
    print("   Process 1: prev=None, no comparison")
    print("   Update prev = 1")
    print("2. Backtrack to 2")
    print("   Process 2: diff = 2-1 = 1, min_diff = 1")
    print("   Update prev = 2")
    print("3. Process right of 2: 3")
    print("   Process 3: diff = 3-2 = 1, min_diff = 1")
    print("   Update prev = 3")
    print("4. Backtrack to 4")
    print("   Process 4: diff = 4-3 = 1, min_diff = 1")
    print("   Update prev = 4")
    print("5. Process right of 4: 6")
    print("   Process 6: diff = 6-4 = 2, min_diff = 1")
    print("   Update prev = 6")
    print("\nFinal min_diff = 1")

    final_result = solution1.getMinimumDifference(demo_root)
    print(f"\nActual Result: {final_result}")

    print("\n" + "=" * 70)

    # Edge cases and considerations
    print("\nEdge Cases and Considerations:")
    print("=" * 70)

    print("""
1. Minimum difference could be between:
   - Parent and child
   - Two leaves
   - Any two nodes in the tree

2. Why not check all pairs?
   - Naive approach would be O(n²)
   - Inorder gives O(n) solution

3. Large values:
   - Node values up to 10^5
   - Differences fit in integer range

4. At least 2 nodes:
   - Problem guarantees tree has ≥ 2 nodes
   - No need to handle single node case

5. BST property ensures inorder is sorted
   - If not BST, this approach wouldn't work
""")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)
    print("""
class Solution:
    def getMinimumDifference(self, root):
        self.min_diff = float('inf')
        self.prev = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff
    """)

    print("\nAlternative (Iterative):")
    print("""
class Solution:
    def getMinimumDifference(self, root):
        min_diff = float('inf')
        prev = None
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if prev is not None:
                min_diff = min(min_diff, current.val - prev)

            prev = current.val
            current = current.right

        return min_diff
    """)