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


# Solution 1: Controlled Recursion (O(h) memory)
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        """Add all left nodes to stack"""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """Return next smallest number"""
        # Get the next smallest element
        top_node = self.stack.pop()

        # If right child exists, add its leftmost subtree
        if top_node.right:
            self._leftmost_inorder(top_node.right)

        return top_node.val

    def hasNext(self):
        """Check if there are more elements"""
        return len(self.stack) > 0


# Solution 2: Flatten BinaryTreeGeneral (O(n) memory, simpler)
class BSTIterator2:
    def __init__(self, root):
        self.nodes = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, node):
        """Perform inorder traversal to get sorted list"""
        if not node:
            return
        self._inorder(node.left)
        self.nodes.append(node.val)
        self._inorder(node.right)

    def next(self):
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self):
        return self.index + 1 < len(self.nodes)


# Test cases
if __name__ == "__main__":
    print("Testing BSTIterator (O(h) memory solution):")
    print("=" * 70)

    # Test case 1: Example from problem
    print("\nTest case 1 - Example from problem:")
    root1 = create_tree_from_list([7, 3, 15, None, None, 9, 20])
    iterator1 = BSTIterator(root1)

    operations = ["next", "next", "hasNext", "next", "hasNext",
                  "next", "hasNext", "next", "hasNext"]
    expected = [3, 7, True, 9, True, 15, True, 20, False]

    print("Tree: [7, 3, 15, None, None, 9, 20]")
    print("BinaryTreeGeneral structure (BinaryTreeGeneral):")
    print("        7")
    print("       / \\")
    print("      3   15")
    print("         /  \\")
    print("        9    20")

    print("\nOperations and results:")
    for i, (op, exp) in enumerate(zip(operations, expected)):
        if op == "next":
            result = iterator1.next()
        else:
            result = iterator1.hasNext()

        status = "✓" if result == exp else "✗"
        print(f"{op:10} -> {result:5} (expected: {exp:5}) {status}")

    # Test case 2: Single node
    print("\n" + "-" * 50)
    print("Test case 2 - Single node:")
    root2 = create_tree_from_list([5])
    iterator2 = BSTIterator(root2)

    print("Tree: [5]")
    print(f"hasNext: {iterator2.hasNext()} (expected: True)")
    print(f"next: {iterator2.next()} (expected: 5)")
    print(f"hasNext: {iterator2.hasNext()} (expected: False)")

    # Test case 3: Left-skewed BinaryTreeGeneral
    print("\n" + "-" * 50)
    print("Test case 3 - Left-skewed BinaryTreeGeneral:")
    root3 = create_tree_from_list([5, 4, None, 3, None, 2, None, 1])
    iterator3 = BSTIterator(root3)

    print("Tree: [5, 4, None, 3, None, 2, None, 1]")
    print("BinaryTreeGeneral structure (left-skewed):")
    print("        5")
    print("       /")
    print("      4")
    print("     /")
    print("    3")
    print("   /")
    print("  2")
    print(" /")
    print("1")

    print("\nIn-order traversal (should be sorted):")
    while iterator3.hasNext():
        print(iterator3.next(), end=" ")
    print("(expected: 1 2 3 4 5)")

    # Test case 4: Right-skewed BinaryTreeGeneral
    print("\n" + "-" * 50)
    print("Test case 4 - Right-skewed BinaryTreeGeneral:")
    root4 = create_tree_from_list([1, None, 2, None, 3, None, 4, None, 5])
    iterator4 = BSTIterator(root4)

    print("Tree: [1, None, 2, None, 3, None, 4, None, 5]")
    print("\nIn-order traversal (should be sorted):")
    while iterator4.hasNext():
        print(iterator4.next(), end=" ")
    print("(expected: 1 2 3 4 5)")

    # Test case 5: Complex BinaryTreeGeneral
    print("\n" + "-" * 50)
    print("Test case 5 - Complex BinaryTreeGeneral:")
    root5 = create_tree_from_list([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13])
    iterator5 = BSTIterator(root5)

    print("Tree: [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13]")
    print("BinaryTreeGeneral structure:")
    print("        8")
    print("       / \\")
    print("      3   10")
    print("     / \\    \\")
    print("    1   6    14")
    print("       / \\   /")
    print("      4   7 13")

    print("\nIn-order traversal (should be sorted):")
    result = []
    while iterator5.hasNext():
        result.append(iterator5.next())
    print(f"{result} (expected: [1, 3, 4, 6, 7, 8, 10, 13, 14])")
    print(f"Sorted: {sorted(result) == result}")

    # Test both solutions
    print("\n" + "=" * 70)
    print("Comparing both solutions:")
    print("=" * 70)

    test_tree = create_tree_from_list([7, 3, 15, None, None, 9, 20])

    print("\nSolution 1 (O(h) memory):")
    iter1 = BSTIterator(test_tree)
    result1 = []
    while iter1.hasNext():
        result1.append(iter1.next())
    print(f"Result: {result1}")

    print("\nSolution 2 (O(n) memory):")
    iter2 = BSTIterator2(test_tree)
    result2 = []
    while iter2.hasNext():
        result2.append(iter2.next())
    print(f"Result: {result2}")

    print(f"\nResults match: {result1 == result2}")

    # Memory complexity explanation
    print("\n" + "=" * 70)
    print("Algorithm Explanation:")
    print("=" * 70)
    print("""
Solution 1 (O(h) memory):
1. Initialize: Push all left nodes to stack (go left until null)
2. next(): 
   - Pop top node from stack
   - If node has right child, push all left nodes of right subtree
   - Return node value
3. hasNext(): Check if stack is not empty

Time Complexity:
- Constructor: O(h) where h is tree height
- next(): Amortized O(1) (each node pushed/popped once)
- hasNext(): O(1)

Space Complexity: O(h) where h is tree height

Solution 2 (O(n) memory):
1. Initialize: Perform full inorder traversal, store in array
2. next(): Return next element from array
3. hasNext(): Check if index < length

Time Complexity:
- Constructor: O(n)
- next(): O(1)
- hasNext(): O(1)

Space Complexity: O(n)

For the follow-up requirement (O(h) memory), use Solution 1.
    """)