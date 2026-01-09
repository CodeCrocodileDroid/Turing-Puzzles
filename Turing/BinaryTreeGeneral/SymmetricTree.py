# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Level-order representation
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

        return str(result)


class Solution:
    # Solution 1: Recursive
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        # Both are None
        if not left and not right:
            return True
        # One is None, other is not
        if not left or not right:
            return False
        # Values don't match
        if left.val != right.val:
            return False
        # Check outer and inner pairs recursively
        return (self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))

    # Solution 2: Iterative using queue
    def isSymmetricIterative(self, root):
        from collections import deque

        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            # Both are None
            if not left and not right:
                continue
            # One is None, other is not
            if not left or not right:
                return False
            # Values don't match
            if left.val != right.val:
                return False

            # Add pairs to check
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True

    # Solution 3: Iterative using stack
    def isSymmetricStack(self, root):
        if not root:
            return True

        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()

            # Both are None
            if not left and not right:
                continue
            # One is None, other is not
            if not left or not right:
                return False
            # Values don't match
            if left.val != right.val:
                return False

            # Add pairs to check (right first for stack)
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True


# Helper function to create a binary tree from a list representation
def create_tree_from_list(lst):
    """
    Creates a binary tree from a level-order list representation.
    """
    if not lst or lst[0] is None:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        node = queue.pop(0)

        # Left child
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root


# Helper function to print tree structure
def print_tree_structure(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree_structure(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree_structure(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Symmetric tree from example
    print("=" * 60)
    print("Test case 1: Symmetric tree")
    print("=" * 60)
    tree1 = create_tree_from_list([1, 2, 2, 3, 4, 4, 3])
    print(f"Tree: {tree1}")
    print()
    print("Tree structure:")
    print_tree_structure(tree1)
    print()
    print(f"Recursive result: {solution.isSymmetric(tree1)}")
    print(f"Iterative (queue) result: {solution.isSymmetricIterative(tree1)}")
    print(f"Iterative (stack) result: {solution.isSymmetricStack(tree1)}")
    print(f"Expected: True")
    print()

    # Test case 2: Asymmetric tree from example
    print("=" * 60)
    print("Test case 2: Asymmetric tree")
    print("=" * 60)
    tree2 = create_tree_from_list([1, 2, 2, None, 3, None, 3])
    print(f"Tree: {tree2}")
    print()
    print("Tree structure:")
    print_tree_structure(tree2)
    print()
    print(f"Recursive result: {solution.isSymmetric(tree2)}")
    print(f"Iterative (queue) result: {solution.isSymmetricIterative(tree2)}")
    print(f"Iterative (stack) result: {solution.isSymmetricStack(tree2)}")
    print(f"Expected: False")
    print()

    # Test case 3: Single node
    print("=" * 60)
    print("Test case 3: Single node")
    print("=" * 60)
    tree3 = create_tree_from_list([1])
    print(f"Tree: {tree3}")
    print()
    print("Tree structure:")
    print_tree_structure(tree3)
    print()
    print(f"Recursive result: {solution.isSymmetric(tree3)}")
    print(f"Iterative (queue) result: {solution.isSymmetricIterative(tree3)}")
    print(f"Iterative (stack) result: {solution.isSymmetricStack(tree3)}")
    print(f"Expected: True")
    print()

    # Test case 4: Empty tree
    print("=" * 60)
    print("Test case 4: Empty tree")
    print("=" * 60)
    tree4 = create_tree_from_list([])
    print(f"Tree: {tree4}")
    print()
    print(f"Recursive result: {solution.isSymmetric(tree4)}")
    print(f"Iterative (queue) result: {solution.isSymmetricIterative(tree4)}")
    print(f"Iterative (stack) result: {solution.isSymmetricStack(tree4)}")
    print(f"Expected: True")
    print()

    # Test case 5: Perfect symmetric tree
    print("=" * 60)
    print("Test case 5: Perfect symmetric tree")
    print("=" * 60)
    tree5 = create_tree_from_list([1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 4, 4, 5, 5, 4])
    print(f"Tree: {tree5}")
    print()
    print(f"Recursive result: {solution.isSymmetric(tree5)}")
    print(f"Iterative (queue) result: {solution.isSymmetricIterative(tree5)}")
    print(f"Iterative (stack) result: {solution.isSymmetricStack(tree5)}")
    print(f"Expected: True")
    print()

    # Test case 6: Asymmetric tree with same values but different structure
    print("=" * 60)
    print("Test case 6: Asymmetric tree (same values, different structure)")
    print("=" * 60)
    tree6 = create_tree_from_list([1, 2, 2, 3, 3, None, 3])
    print(f"Tree: {tree6}")
    print()
    print("Tree structure:")
    print_tree_structure(tree6)
    print()
    print(f"Recursive result: {solution.isSymmetric(tree6)}")
    print(f"Iterative (queue) result: {solution.isSymmetricIterative(tree6)}")
    print(f"Iterative (stack) result: {solution.isSymmetricStack(tree6)}")
    print(f"Expected: False")
    print()

    # Test case 7: Tree with only left children
    print("=" * 60)
    print("Test case 7: Tree with only left children")
    print("=" * 60)
    tree7 = create_tree_from_list([1, 2, None, 3, None, 4])
    print(f"Tree: {tree7}")
    print()
    print("Tree structure:")
    print_tree_structure(tree7)
    print()
    print(f"Recursive result: {solution.isSymmetric(tree7)}")
    print(f"Iterative (queue) result: {solution.isSymmetricIterative(tree7)}")
    print(f"Iterative (stack) result: {solution.isSymmetricStack(tree7)}")
    print(f"Expected: False")