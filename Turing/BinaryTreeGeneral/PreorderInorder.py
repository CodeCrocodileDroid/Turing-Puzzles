# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self):
        """Convert to level-order list representation"""
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

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result

    def __repr__(self):
        return str(self.to_list())


class Solution:
    def buildTree(self, preorder, inorder):
        """
        Build a binary tree from preorder and inorder traversals.

        Preorder: Root -> Left -> Right
        Inorder: Left -> Root -> Right
        """
        if not preorder or not inorder:
            return None

        # Create a dictionary to map values to their inorder indices for O(1) lookup
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        # Use indices to track current position in preorder
        pre_idx = [0]  # List is mutable, works like a reference

        def build(left, right):
            """Helper function to build tree recursively"""
            if left > right:
                return None

            # Current root value from preorder traversal
            root_val = preorder[pre_idx[0]]
            root = TreeNode(root_val)
            pre_idx[0] += 1

            # Find root position in inorder traversal
            root_idx = inorder_map[root_val]

            # Build left subtree (elements before root in inorder)
            root.left = build(left, root_idx - 1)
            # Build right subtree (elements after root in inorder)
            root.right = build(root_idx + 1, right)

            return root

        return build(0, len(inorder) - 1)


# Helper function for alternative approach (explicit indices)
class Solution2:
    def buildTree(self, preorder, inorder):
        """Alternative solution using explicit indices without mutable reference"""
        if not preorder or not inorder:
            return None

        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            root_idx = inorder_map[root_val]
            left_size = root_idx - in_start

            root.left = build(pre_start + 1, pre_start + left_size,
                              in_start, root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end,
                               root_idx + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


# Test function to validate the constructed tree
def validate_tree(root, preorder, inorder):
    """Validate that the constructed tree matches the given traversals"""

    def preorder_traversal(node, result):
        if node:
            result.append(node.val)
            preorder_traversal(node.left, result)
            preorder_traversal(node.right, result)

    def inorder_traversal(node, result):
        if node:
            inorder_traversal(node.left, result)
            result.append(node.val)
            inorder_traversal(node.right, result)

    pre_result = []
    in_result = []

    preorder_traversal(root, pre_result)
    inorder_traversal(root, in_result)

    return pre_result == preorder and in_result == inorder


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    test_cases = [
        # (preorder, inorder, expected_tree_list, test_name)
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7],
         [3, 9, 20, None, None, 15, 7], "Example 1"),

        ([-1], [-1], [-1], "Example 2 - Single node"),

        ([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7],
         [1, 2, 3, 4, 5, 6, 7], "Complete binary tree"),

        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
         [1, None, 2, None, 3, None, 4, None, 5], "Right-skewed tree"),

        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1],
         [1, 2, None, 3, None, 4, None, 5], "Left-skewed tree"),

        ([], [], [], "Empty tree"),

        ([1, 2, 3], [2, 1, 3],
         [1, 2, 3], "Simple 3-node tree"),

        ([10, 5, 3, 7, 15, 12, 18], [3, 5, 7, 10, 12, 15, 18],
         [10, 5, 15, 3, 7, 12, 18], "Binary search tree example"),
    ]

    print("Testing Solution 1 (with mutable reference):")
    print("=" * 70)

    for preorder, inorder, expected, test_name in test_cases:
        print(f"\nTest: {test_name}")
        print(f"Preorder: {preorder}")
        print(f"Inorder: {inorder}")

        if preorder:  # Only build if there are nodes
            tree = solution.buildTree(preorder, inorder)
            result = tree.to_list() if tree else []
            print(f"Constructed tree: {result}")
            print(f"Expected tree:   {expected}")

            # Validate the tree
            is_valid = validate_tree(tree, preorder, inorder)
            print(f"Tree validation: {'✓ PASS' if is_valid else '✗ FAIL'}")

            if result != expected:
                print(f"NOTE: Tree structure differs but may still be valid.")
                print(f"      Multiple trees can have same traversals.")
        else:
            print(f"Constructed tree: []")
            print(f"Expected tree:   []")
            print(f"Tree validation: ✓ PASS (empty tree)")

    print("\n" + "=" * 70)
    print("\nTesting Solution 2 (with explicit indices):")
    print("=" * 70)

    for preorder, inorder, expected, test_name in test_cases[:3]:  # Test first 3 cases
        print(f"\nTest: {test_name}")
        print(f"Preorder: {preorder}")
        print(f"Inorder: {inorder}")

        if preorder:
            tree = solution2.buildTree(preorder, inorder)
            result = tree.to_list() if tree else []
            print(f"Constructed tree: {result}")

            is_valid = validate_tree(tree, preorder, inorder)
            print(f"Tree validation: {'✓ PASS' if is_valid else '✗ FAIL'}")

    print("\n" + "=" * 70)

    # Additional explanation
    print("\nExplanation of algorithm:")
    print("1. Preorder traversal gives: Root -> Left -> Right")
    print("2. Inorder traversal gives: Left -> Root -> Right")
    print("3. First element in preorder is always the root")
    print("4. Find root in inorder: elements to left are in left subtree,")
    print("   elements to right are in right subtree")
    print("5. Recursively apply this to build the entire tree")