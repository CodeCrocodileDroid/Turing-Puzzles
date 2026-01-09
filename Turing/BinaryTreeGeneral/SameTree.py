# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        # Base case: both nodes are None
        if not p and not q:
            return True
        # One is None, the other is not -> not the same
        if not p or not q:
            return False
        # Values differ -> not the same
        if p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Helper function to create a binary tree from a list representation
def create_tree_from_list(lst, index=0):
    """
    Creates a binary tree from a list representation.
    For node at index i:
    - left child is at index 2*i + 1
    - right child is at index 2*i + 2
    Returns None for None values or indices out of range
    """
    if index >= len(lst) or lst[index] is None:
        return None

    root = TreeNode(lst[index])
    root.left = create_tree_from_list(lst, 2 * index + 1)
    root.right = create_tree_from_list(lst, 2 * index + 2)

    return root


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem
    print("Test case 1:")
    p1 = create_tree_from_list([1, 2, 3])
    q1 = create_tree_from_list([1, 2, 3])
    result1 = solution.isSameTree(p1, q1)
    print(f"p = [1,2,3], q = [1,2,3]")
    print(f"Result: {result1}")
    print(f"Expected: True")
    print()

    # Test case 2: Example from problem
    print("Test case 2:")
    p2 = create_tree_from_list([1, 2])
    q2 = create_tree_from_list([1, None, 2])
    result2 = solution.isSameTree(p2, q2)
    print(f"p = [1,2], q = [1,null,2]")
    print(f"Result: {result2}")
    print(f"Expected: False")
    print()

    # Test case 3: Example from problem
    print("Test case 3:")
    p3 = create_tree_from_list([1, 2, 1])
    q3 = create_tree_from_list([1, 1, 2])
    result3 = solution.isSameTree(p3, q3)
    print(f"p = [1,2,1], q = [1,1,2]")
    print(f"Result: {result3}")
    print(f"Expected: False")
    print()

    # Test case 4: Both trees empty
    print("Test case 4:")
    p4 = create_tree_from_list([])
    q4 = create_tree_from_list([])
    result4 = solution.isSameTree(p4, q4)
    print(f"p = [], q = []")
    print(f"Result: {result4}")
    print(f"Expected: True")
    print()

    # Test case 5: One tree empty, other not
    print("Test case 5:")
    p5 = create_tree_from_list([1])
    q5 = create_tree_from_list([])
    result5 = solution.isSameTree(p5, q5)
    print(f"p = [1], q = []")
    print(f"Result: {result5}")
    print(f"Expected: False")
    print()

    # Test case 6: Same structure, different values
    print("Test case 6:")
    p6 = create_tree_from_list([1, 2, 3, 4])
    q6 = create_tree_from_list([1, 2, 3, 5])
    result6 = solution.isSameTree(p6, q6)
    print(f"p = [1,2,3,4], q = [1,2,3,5]")
    print(f"Result: {result6}")
    print(f"Expected: False")
    print()

    # Test case 7: Complex identical trees
    print("Test case 7:")
    p7 = create_tree_from_list([1, 2, 3, None, 4, 5, 6])
    q7 = create_tree_from_list([1, 2, 3, None, 4, 5, 6])
    result7 = solution.isSameTree(p7, q7)
    print(f"p = [1,2,3,null,4,5,6], q = [1,2,3,null,4,5,6]")
    print(f"Result: {result7}")
    print(f"Expected: True")