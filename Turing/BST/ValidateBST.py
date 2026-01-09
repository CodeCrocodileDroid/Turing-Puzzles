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
    def isValidBST(self, root):
        """Inorder traversal approach"""
        self.prev = None

        def inorder(node):
            if not node:
                return True

            # Check left subtree
            if not inorder(node.left):
                return False

            # Check current node
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val

            # Check right subtree
            return inorder(node.right)

        return inorder(root)


class Solution2:
    def isValidBST(self, root):
        """Recursive with range boundaries"""

        def validate(node, min_val, max_val):
            if not node:
                return True

            # Check current node value within bounds
            if (min_val is not None and node.val <= min_val) or \
                    (max_val is not None and node.val >= max_val):
                return False

            # Recursively validate left and right subtrees
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, None, None)


class Solution3:
    def isValidBST(self, root):
        """Iterative inorder traversal"""
        if not root:
            return True

        stack = []
        current = root
        prev = None

        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()

            # Check if current value > previous value
            if prev is not None and current.val <= prev:
                return False

            prev = current.val
            current = current.right

        return True


class Solution4:
    def isValidBST(self, root):
        """Alternative range approach with float bounds"""

        def validate(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root)


# Test cases
if __name__ == "__main__":
    solution1 = Solution()  # Inorder recursive
    solution2 = Solution2()  # Range recursive
    solution3 = Solution3()  # Iterative inorder
    solution4 = Solution4()  # Range with float bounds

    test_cases = [
        # (tree_list, expected, test_name)
        ([2, 1, 3], True, "Example 1 - Valid BST"),
        ([5, 1, 4, None, None, 3, 6], False, "Example 2 - Invalid BST"),
        ([], True, "Empty tree"),
        ([1], True, "Single node"),
        ([1, 1], False, "Duplicate values"),
        ([5, 1, 7, None, None, 6, 8], True, "Valid BST"),
        ([10, 5, 15, 3, 7, 13, 18], True, "Large valid BST"),
        ([10, 5, 15, 3, 11, None, 18], False, "11 in wrong place"),
        ([3, 2, 5, 1, 4], True, "Another valid BST"),
        ([3, 2, 5, 1, 6], False, "6 in wrong place"),
        ([5, 3, 7, 2, 4, 6, 8, 1], True, "Complete valid BST"),
        ([5, 3, 7, 2, 4, 6, 8, 1, 9], False, "9 in wrong place"),
        ([2147483647], True, "Max int value"),
        ([-2147483648], True, "Min int value"),
        ([1, None, 2, None, 3], True, "Right-skewed valid BST"),
        ([3, 2, None, 1], True, "Left-skewed valid BST"),
        ([2, 1, 3, 0, 4], False, "4 in wrong place"),
        ([5, 3, 8, 2, 4, 6, 9, 1], True, "Valid with all levels"),
    ]

    print("Testing Validate Binary Search Tree")
    print("=" * 70)

    for i, (tree_list, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Tree: {tree_list}")

        if tree_list:
            root = create_tree_from_list(tree_list)

            result1 = solution1.isValidBST(root)
            result2 = solution2.isValidBST(root)
            result3 = solution3.isValidBST(root)
            result4 = solution4.isValidBST(root)

            print(f"\nInorder Recursive:    {result1}")
            print(f"Range Recursive:      {result2}")
            print(f"Iterative Inorder:    {result3}")
            print(f"Range with Float:     {result4}")
            print(f"Expected:             {expected}")

            match1 = result1 == expected
            match2 = result2 == expected
            match3 = result3 == expected
            match4 = result4 == expected

            if match1 and match2 and match3 and match4:
                print("✓ ALL SOLUTIONS PASS")
            else:
                status = []
                if match1:
                    status.append("✓ Inorder")
                else:
                    status.append("✗ Inorder")

                if match2:
                    status.append("✓ Range")
                else:
                    status.append("✗ Range")

                if match3:
                    status.append("✓ Iterative")
                else:
                    status.append("✗ Iterative")

                if match4:
                    status.append("✓ FloatRange")
                else:
                    status.append("✗ FloatRange")

                print("Status: " + " | ".join(status))

            # Show detailed analysis for examples
            if test_name in ["Example 1 - Valid BST", "Example 2 - Invalid BST", "Duplicate values"]:
                print("\nDetailed Analysis:")


                # Get inorder traversal
                def get_inorder(node):
                    if not node:
                        return []
                    return get_inorder(node.left) + [node.val] + get_inorder(node.right)


                inorder_vals = get_inorder(root)
                print(f"Inorder traversal: {inorder_vals}")

                # Check if sorted
                is_sorted = all(inorder_vals[i] < inorder_vals[i + 1] for i in range(len(inorder_vals) - 1))
                print(f"Strictly increasing? {is_sorted}")

                # Show tree structure
                if len(tree_list) <= 7:
                    print("\nTree Structure:")
                    if tree_list == [2, 1, 3]:
                        print("""
        2
       / \\
      1   3
                        """)
                        print("BST Rules:")
                        print("- Left child 1 < 2 ✓")
                        print("- Right child 3 > 2 ✓")
                        print("- Both subtrees valid ✓")
                    elif tree_list == [5, 1, 4, None, None, 3, 6]:
                        print("""
        5
       / \\
      1   4
         / \\
        3   6
                        """)
                        print("BST Rules:")
                        print("- Left subtree: 1 < 5 ✓")
                        print("- Right subtree: Root 4 should be > 5, but 4 < 5 ✗")
                        print("- 3 < 4 ✓ but irrelevant due to parent violation")
                    elif tree_list == [1, 1]:
                        print("""
        1
       /
      1
                        """)
                        print("BST Rules:")
                        print("- Left child 1 should be < 1, but 1 == 1 ✗")
                        print("- Need strictly less, not less than or equal")
        else:
            print("Tree: (empty)")
            # All solutions should return True for empty tree
            result1 = solution1.isValidBST(None)
            result2 = solution2.isValidBST(None)
            result3 = solution3.isValidBST(None)
            result4 = solution4.isValidBST(None)

            print(f"\nInorder Recursive:    {result1}")
            print(f"Range Recursive:      {result2}")
            print(f"Iterative Inorder:    {result3}")
            print(f"Range with Float:     {result4}")
            print(f"Expected:             {expected}")

            if all(r == expected for r in [result1, result2, result3, result4]):
                print("✓ ALL SOLUTIONS PASS")
            else:
                print("✗ SOME SOLUTIONS FAIL")

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Solution 1 (Inorder Traversal):
1. Perform inorder traversal of the tree
2. For BST, inorder traversal should produce strictly increasing sequence
3. Check if each value > previous value
4. Time: O(n), Space: O(h) (recursion stack)

Solution 2 (Range Validation):
1. Each node must be within valid range (min_val, max_val)
2. For root: range is (-∞, +∞)
3. For left child: range is (min_val, parent.val)
4. For right child: range is (parent.val, max_val)
5. Time: O(n), Space: O(h)

Solution 3 (Iterative Inorder):
1. Same as Solution 1 but iterative
2. Uses stack for traversal
3. Check if values strictly increasing
4. Time: O(n), Space: O(h)

Solution 4 (Range with Float Bounds):
1. Same as Solution 2 but uses float('-inf') and float('inf')
2. Simpler initialization
3. Time: O(n), Space: O(h)
""")

    print("\nKey BST Rules:")
    print("-" * 40)
    print("""
1. Left subtree contains ONLY nodes with values < node value
2. Right subtree contains ONLY nodes with values > node value
3. Both subtrees must also be BSTs
4. Comparisons are STRICT: < and >, not ≤ and ≥
5. This applies to all descendants, not just immediate children
""")

    print("\n" + "=" * 70)

    # Step-by-step demonstration
    print("\nStep-by-step Demonstration:")
    print("=" * 70)

    print("\nExample 1: Valid BST [2, 1, 3]")
    print("""
        2
       / \\
      1   3
    """)

    print("\nSolution 2 (Range Validation) execution:")
    print("1. validate(2, None, None)")
    print("   - Check: 2 within (None, None) ✓")
    print("   - validate(1, None, 2)")
    print("   - validate(3, 2, None)")
    print("\n2. validate(1, None, 2)")
    print("   - Check: 1 within (None, 2) ✓")
    print("   - validate(None, None, 1) → True")
    print("   - validate(None, 1, 2) → True")
    print("\n3. validate(3, 2, None)")
    print("   - Check: 3 within (2, None) ✓")
    print("   - validate(None, 2, 3) → True")
    print("   - validate(None, 3, None) → True")
    print("\nFinal: All checks pass → True")

    print("\n\nExample 2: Invalid BST [5, 1, 4, null, null, 3, 6]")
    print("""
        5
       / \\
      1   4
         / \\
        3   6
    """)

    print("\nSolution 2 (Range Validation) execution:")
    print("1. validate(5, None, None)")
    print("   - Check: 5 within (None, None) ✓")
    print("   - validate(1, None, 5)")
    print("   - validate(4, 5, None)  ← PROBLEM HERE")
    print("\n2. validate(4, 5, None)")
    print("   - Check: 4 within (5, None)")
    print("   - 4 should be > 5, but 4 < 5 ✗")
    print("   - Return False immediately")
    print("\nFinal: False (4 is in right subtree but less than 5)")

    print("\n" + "=" * 70)

    # Common mistakes
    print("\nCommon Mistakes to Avoid:")
    print("=" * 70)

    print("""
1. Only checking immediate children:
   - Wrong: if left.val < root.val and right.val > root.val
   - Must check ALL descendants, not just children

2. Using ≤ or ≥ instead of strict comparisons:
   - BST requires STRICT inequality
   - Left child must be < parent, not ≤
   - Right child must be > parent, not ≥

3. Not handling duplicate values:
   - BST cannot have duplicate values
   - All values must be unique

4. Not considering entire subtrees:
   - A node in left subtree must be < ALL ancestors
   - A node in right subtree must be > ALL ancestors

5. Integer overflow:
   - Node values can be ±2^31
   - Use None bounds or float('inf') for range method
""")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)

    print("""Solution 1 (Inorder Traversal):""")
    print("""
class Solution:
    def isValidBST(self, root):
        self.prev = None

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val

            return inorder(node.right)

        return inorder(root)
    """)

    print("\n""Solution 2 (Range Validation):""")
    print("""
class Solution:
    def isValidBST(self, root):
        def validate(node, min_val, max_val):
            if not node:
                return True

            if (min_val is not None and node.val <= min_val) or \\
               (max_val is not None and node.val >= max_val):
                return False

            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))

        return validate(root, None, None)
    """)

    print("\nNote: Both solutions are O(n) time and O(h) space.")
    print("Inorder traversal is more intuitive for BST validation.")
    print("Range validation explicitly shows the constraints.")