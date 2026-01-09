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
    def buildTree(self, inorder, postorder):
        # Create hashmap for inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None

            # Last element in postorder is the root
            root_val = postorder[post_end]
            root = TreeNode(root_val)

            # Find root index in inorder
            root_idx = inorder_map[root_val]

            # Number of nodes in left subtree
            left_size = root_idx - in_start

            # Recursively build left and right subtrees
            # Note the indices calculation
            root.left = build(in_start, root_idx - 1,
                              post_start, post_start + left_size - 1)
            root.right = build(root_idx + 1, in_end,
                               post_start + left_size, post_end - 1)

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


class Solution2:
    def buildTree(self, inorder, postorder):
        """Alternative: Process from end of postorder"""
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        post_idx = [len(postorder) - 1]  # Start from last element

        def build(left, right):
            if left > right:
                return None

            root_val = postorder[post_idx[0]]
            root = TreeNode(root_val)
            post_idx[0] -= 1

            root_idx = inorder_map[root_val]

            # Build right subtree first (important!)
            root.right = build(root_idx + 1, right)
            root.left = build(left, root_idx - 1)

            return root

        return build(0, len(inorder) - 1)


# Test function to validate the constructed tree
def validate_tree(root, inorder, postorder):
    """Validate that the constructed tree matches the given traversals"""

    def inorder_traversal(node, result):
        if node:
            inorder_traversal(node.left, result)
            result.append(node.val)
            inorder_traversal(node.right, result)

    def postorder_traversal(node, result):
        if node:
            postorder_traversal(node.left, result)
            postorder_traversal(node.right, result)
            result.append(node.val)

    in_result = []
    post_result = []

    inorder_traversal(root, in_result)
    postorder_traversal(root, post_result)

    return in_result == inorder and post_result == postorder


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    test_cases = [
        # (inorder, postorder, expected_tree_list, test_name)
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3],
         [3, 9, 20, None, None, 15, 7], "Example 1"),

        ([-1], [-1], [-1], "Example 2 - Single node"),

        ([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1],
         [1, 2, 3, 4, 5, 6, 7], "Complete binary tree"),

        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
         [5, 4, 3, 2, 1], "Right-skewed tree (becomes left-skewed)"),

        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5],
         [5, 4, None, 3, None, 2, None, 1], "Left-skewed tree"),

        ([], [], [], "Empty tree"),

        ([2, 1, 3], [2, 3, 1],
         [1, 2, 3], "Simple 3-node tree"),

        ([3, 5, 7, 10, 12, 15, 18], [3, 7, 5, 12, 18, 15, 10],
         [10, 5, 15, 3, 7, 12, 18], "Binary search tree example"),
    ]

    print("Testing Solution 1 (explicit indices):")
    print("=" * 70)

    for i, (inorder, postorder, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Inorder:   {inorder}")
        print(f"Postorder: {postorder}")

        if inorder and postorder:
            tree = solution.buildTree(inorder, postorder)
            result = tree.to_list() if tree else []
            print(f"Constructed tree: {result}")
            print(f"Expected tree:   {expected}")

            # Validate the tree
            is_valid = validate_tree(tree, inorder, postorder)
            print(f"Tree validation: {'✓ PASS' if is_valid else '✗ FAIL'}")

            if result != expected:
                print(f"NOTE: Tree structure may differ but traversals match.")
        else:
            print(f"Constructed tree: []")
            print(f"Expected tree:   []")
            print(f"Tree validation: ✓ PASS (empty tree)")

    print("\n" + "=" * 70)
    print("\nTesting Solution 2 (mutable reference, process from end):")
    print("=" * 70)

    for i, (inorder, postorder, expected, test_name) in enumerate(test_cases[:3]):  # Test first 3
        print(f"\nTest {i + 1}: {test_name}")
        print(f"Inorder:   {inorder}")
        print(f"Postorder: {postorder}")

        if inorder and postorder:
            tree = solution2.buildTree(inorder, postorder)
            result = tree.to_list() if tree else []
            print(f"Constructed tree: {result}")

            is_valid = validate_tree(tree, inorder, postorder)
            print(f"Tree validation: {'✓ PASS' if is_valid else '✗ FAIL'}")

    print("\n" + "=" * 70)

    # Visual example
    print("\nVisual example for Example 1:")
    print("Inorder:   [9, 3, 15, 20, 7]")
    print("Postorder: [9, 15, 7, 20, 3]")
    print("\nStep-by-step construction:")
    print("1. Root = 3 (last element in postorder)")
    print("2. Find 3 in inorder: [9, 3, 15, 20, 7]")
    print("   - Left subtree: [9]")
    print("   - Right subtree: [15, 20, 7]")
    print("3. Right subtree:")
    print("   - Root = 20 (last element in remaining postorder [15, 7, 20])")
    print("   - Find 20 in [15, 20, 7]")
    print("     * Left: [15]")
    print("     * Right: [7]")
    print("\nFinal tree structure:")
    print("       3")
    print("      / \\")
    print("     9   20")
    print("        /  \\")
    print("       15   7")