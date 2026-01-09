class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def level_order_with_next(self):
        """Return level order traversal showing next pointers"""
        if not self:
            return []

        result = []
        level_start = self

        while level_start:
            current = level_start
            level_start = None

            while current:
                result.append(current.val)

                # Find start of next level
                if not level_start:
                    if current.left:
                        level_start = current.left
                    elif current.right:
                        level_start = current.right

                # Move to next node in current level
                current = current.next

            # Add marker for end of level
            result.append('#')

        return result


def create_tree_from_list(lst):
    """Create tree from level-order list"""
    if not lst or lst[0] is None:
        return None

    root = Node(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        node = queue.pop(0)

        if i < len(lst) and lst[i] is not None:
            node.left = Node(lst[i])
            queue.append(node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = Node(lst[i])
            queue.append(node.right)
        i += 1

    return root


class Solution:
    def connect(self, root):
        """O(1) space solution using next pointers"""
        if not root:
            return None

        # Dummy node to track start of next level
        dummy = Node(0)

        # Start with root
        current = root

        while current:
            # Reset tail for new level
            tail = dummy
            dummy.next = None

            # Traverse current level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                # Move to next node in current level
                current = current.next

            # Move to next level
            current = dummy.next

        return root


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = create_tree_from_list([1, 2, 3, 4, 5, None, 7])
    connected1 = solution.connect(root1)
    print("Example 1:")
    print("Input: [1, 2, 3, 4, 5, null, 7]")
    print(f"Output: {connected1.level_order_with_next() if connected1 else []}")
    print("Expected: [1, '#', 2, 3, '#', 4, 5, 7, '#']")
    print()

    # Example 2
    root2 = create_tree_from_list([])
    connected2 = solution.connect(root2)
    print("Example 2:")
    print("Input: []")
    print(f"Output: {connected2.level_order_with_next() if connected2 else []}")
    print("Expected: []")
    print()

    # Additional test
    root3 = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    connected3 = solution.connect(root3)
    print("Perfect binary tree:")
    print("Input: [1, 2, 3, 4, 5, 6, 7]")
    print(f"Output: {connected3.level_order_with_next() if connected3 else []}")
    print("Expected: [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']")