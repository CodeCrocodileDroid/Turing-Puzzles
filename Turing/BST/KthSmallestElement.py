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
    def kthSmallest(self, root, k):
        """Iterative inorder traversal"""
        stack = []
        current = root
        count = 0

        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()
            count += 1

            if count == k:
                return current.val

            # Move to right subtree
            current = current.right

        return -1


class Solution2:
    def kthSmallest(self, root, k):
        """Recursive inorder traversal with early termination"""
        self.k = k
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return

            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.result


class Solution3:
    def kthSmallest(self, root, k):
        """Inorder traversal with list"""
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return values[k - 1] if k <= len(values) else -1


# For follow-up: Augmented tree with node counts
class AugmentedTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 1  # Number of nodes in subtree including self


class AugmentedBST:
    """BST with node counts for O(h) kth smallest queries"""

    def __init__(self, root):
        self.root = self._build_augmented(root)

    def _build_augmented(self, node):
        """Build augmented tree with node counts"""
        if not node:
            return None

        left = self._build_augmented(node.left)
        right = self._build_augmented(node.right)

        new_node = AugmentedTreeNode(node.val)
        new_node.left = left
        new_node.right = right

        # Calculate node count
        new_node.count = 1
        if left:
            new_node.count += left.count
        if right:
            new_node.count += right.count

        return new_node

    def kthSmallest(self, k):
        """Find kth smallest in O(h) time"""
        return self._kthSmallest(self.root, k)

    def _kthSmallest(self, node, k):
        if not node:
            return -1

        left_count = node.left.count if node.left else 0

        if k <= left_count:
            return self._kthSmallest(node.left, k)
        elif k == left_count + 1:
            return node.val
        else:
            return self._kthSmallest(node.right, k - left_count - 1)


# Test cases
if __name__ == "__main__":
    solution1 = Solution()  # Iterative inorder
    solution2 = Solution2()  # Recursive inorder with early stop
    solution3 = Solution3()  # Inorder with list

    test_cases = [
        # (tree_list, k, expected, test_name)
        ([3, 1, 4, None, 2], 1, 1, "Example 1"),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3, "Example 2"),
        ([1], 1, 1, "Single node"),
        ([2, 1, 3], 1, 1, "Balanced BST, k=1"),
        ([2, 1, 3], 2, 2, "Balanced BST, k=2"),
        ([2, 1, 3], 3, 3, "Balanced BST, k=3"),
        ([4, 2, 6, 1, 3, 5, 7], 4, 4, "Perfect BST, k=4"),
        ([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 12, None, 20], 6, 10, "Large BST"),
        ([1, None, 2, None, 3, None, 4, None, 5], 3, 3, "Right-skewed tree"),
        ([5, 3, 7, 2, 4, 6, 8, 1], 5, 5, "Complete BST"),
        ([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 8, 8, "Large perfect BST"),
    ]

    print("Testing Kth Smallest Element in a BST")
    print("=" * 70)

    for i, (tree_list, k, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Tree: {tree_list}")
        print(f"k = {k}")

        if tree_list:
            root = create_tree_from_list(tree_list)

            result1 = solution1.kthSmallest(root, k)
            result2 = solution2.kthSmallest(root, k)
            result3 = solution3.kthSmallest(root, k)

            print(f"\nIterative Inorder:      {result1}")
            print(f"Recursive Inorder:      {result2}")
            print(f"Inorder with List:      {result3}")
            print(f"Expected:               {expected}")

            match1 = result1 == expected
            match2 = result2 == expected
            match3 = result3 == expected

            if match1 and match2 and match3:
                print("✓ ALL SOLUTIONS PASS")
            else:
                status = []
                if match1:
                    status.append("✓ Iterative")
                else:
                    status.append("✗ Iterative")

                if match2:
                    status.append("✓ Recursive")
                else:
                    status.append("✗ Recursive")

                if match3:
                    status.append("✓ With List")
                else:
                    status.append("✗ With List")

                print("Status: " + " | ".join(status))

            # Show inorder traversal for examples
            if test_name in ["Example 1", "Example 2", "Balanced BST, k=1"]:
                print("\nDetailed Calculation:")


                # Get inorder traversal
                def get_inorder(node):
                    if not node:
                        return []
                    return get_inorder(node.left) + [node.val] + get_inorder(node.right)


                inorder_vals = get_inorder(root)
                print(f"Inorder traversal (sorted): {inorder_vals}")
                print(f"kth smallest (1-indexed): {inorder_vals[k - 1]}")

                # Show tree structure for small trees
                if len(tree_list) <= 7:
                    print("\nTree Structure (BST):")
                    if tree_list == [3, 1, 4, None, 2]:
                        print("""
        3
       / \\
      1   4
       \\
        2
                        """)
                        print("Inorder: 1, 2, 3, 4")
                        print(f"{k}th smallest: {inorder_vals[k - 1]}")
                    elif tree_list == [2, 1, 3]:
                        print("""
        2
       / \\
      1   3
                        """)
                        print("Inorder: 1, 2, 3")
                        print(f"{k}th smallest: {inorder_vals[k - 1]}")
        else:
            print("Tree: (empty)")
            # Note: k is always >= 1 and tree has at least 1 node in tests

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Solution 1 (Iterative Inorder):
1. Use stack to simulate inorder traversal
2. Go left as far as possible
3. Process nodes in sorted order
4. Stop when count reaches k
5. Time: O(h + k), Space: O(h)

Solution 2 (Recursive Inorder with Early Termination):
1. Recursive inorder traversal
2. Decrement k at each node
3. Stop when k reaches 0
4. Time: O(h + k), Space: O(h) (recursion stack)

Solution 3 (Inorder with List):
1. Collect all values in inorder traversal
2. Return k-1 index from list
3. Time: O(n), Space: O(n)
""")

    print("\nWhy Inorder Traversal Works:")
    print("-" * 40)
    print("""
1. BST property: Left < Root < Right
2. Inorder traversal visits nodes in sorted order
3. kth element in inorder = kth smallest in BST
""")

    print("\n" + "=" * 70)

    # Step-by-step demonstration
    print("\nStep-by-step Demonstration for Example 1:")
    print("=" * 70)

    demo_root = create_tree_from_list([3, 1, 4, None, 2])
    k = 1

    print("Tree: [3, 1, 4, None, 2], k = 1")
    print("""
        3
       / \\
      1   4
       \\
        2
    """)

    print("\nSolution 1 (Iterative Inorder) Execution:")
    print("stack = [], current = 3, count = 0")
    print("1. Go left: push 3, push 1, current = None")
    print("   stack = [3, 1]")
    print("2. Pop 1: count = 1")
    print("   count == k (1 == 1) → return 1 ✓")

    result = solution1.kthSmallest(demo_root, k)
    print(f"\nActual Result: {result}")

    print("\n" + "=" * 70)

    # Follow-up solution demonstration
    print("\nFollow-up Solution (Augmented Tree):")
    print("=" * 70)
    print("""
Problem: If BST is modified often (insert/delete), 
         how to optimize frequent kth smallest queries?

Solution: Augment tree nodes with count of nodes in subtree.

Each node stores:
- val: node value
- left: left child
- right: right child  
- count: number of nodes in subtree (including self)

Algorithm to find kth smallest:
1. Start at root
2. left_count = root.left.count (if exists)
3. If k <= left_count: search in left subtree
4. If k == left_count + 1: current node is answer
5. If k > left_count + 1: search in right subtree with k = k - left_count - 1

Time: O(h) where h is tree height
Space: O(1) extra space
""")

    # Demonstrate augmented tree
    print("\nExample: Tree [3, 1, 4, None, 2] with node counts:")
    print("""
        3(count=4)
       /         \\
    1(count=2)   4(count=1)
       \\
        2(count=1)

    Find k=3:
    1. At root (3): left_count = 2
    2. k=3 > left_count+1=3? No, k=3 == left_count+1=3
    3. Answer is root value: 3

    Find k=1:
    1. At root (3): left_count = 2
    2. k=1 <= left_count=2
    3. Go to left child (1): left_count = 0
    4. k=1 > left_count+1=1? No, k=1 == left_count+1=1
    5. Answer is 1
    """)

    # Test augmented tree
    print("\nTesting Augmented Tree Implementation:")
    test_root = create_tree_from_list([3, 1, 4, None, 2])
    augmented_bst = AugmentedBST(test_root)

    test_cases_followup = [(1, 1), (2, 2), (3, 3), (4, 4)]
    for k_val, expected in test_cases_followup:
        result = augmented_bst.kthSmallest(k_val)
        print(f"k={k_val}: {result} (expected: {expected}) {'✓' if result == expected else '✗'}")

    print("\n" + "=" * 70)

    # Complexity comparison
    print("\nComplexity Comparison:")
    print("=" * 70)

    print("""
| Method                | Time Complexity | Space | Best For          |
|-----------------------|-----------------|-------|-------------------|
| Inorder (basic)       | O(n)            | O(n)  | One-time query    |
| Inorder (early stop)  | O(h + k)        | O(h)  | Small k           |
| Augmented Tree        | O(h)            | O(n)* | Frequent queries  |

* Augmented tree uses O(n) extra space for count values
""")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)
    print("""
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            current = current.right

        return -1
    """)

    print("\nAlternative (Recursive):")
    print("""
class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None

        def inorder(node):
            if not node or self.result:
                return

            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.result
    """)