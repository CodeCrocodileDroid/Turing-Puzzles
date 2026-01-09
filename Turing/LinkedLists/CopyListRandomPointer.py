class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        # Helper to print the list structure
        nodes = []
        randoms = []
        curr = self
        node_index = {}
        idx = 0
        # First, index all nodes
        temp = self
        while temp:
            node_index[temp] = idx
            idx += 1
            temp = temp.next
        # Now build representation
        curr = self
        while curr:
            rand_idx = node_index.get(curr.random, None)
            nodes.append([curr.val, rand_idx])
            curr = curr.next
        return str(nodes)


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Dictionary to map original nodes to their copies
        old_to_new = {}

        # First pass: create all nodes
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Second pass: assign next and random pointers
        current = head
        while current:
            copy_node = old_to_new[current]
            if current.next:
                copy_node.next = old_to_new[current.next]
            if current.random:
                copy_node.random = old_to_new[current.random]
            current = current.next

        return old_to_new[head]


# Helper function to create a linked list from list of [val, random_index]
def create_linked_list(arr):
    if not arr:
        return None

    # Create all nodes first
    nodes = [Node(val) for val, _ in arr]

    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Set random pointers
    for i, (_, random_idx) in enumerate(arr):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]

    return nodes[0]


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    print("Example 1:")
    head1 = create_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    print("Original:", head1)
    copied1 = solution.copyRandomList(head1)
    print("Copied:  ", copied1)

    # Example 2
    print("\nExample 2:")
    head2 = create_linked_list([[1, 1], [2, 1]])
    print("Original:", head2)
    copied2 = solution.copyRandomList(head2)
    print("Copied:  ", copied2)

    # Example 3
    print("\nExample 3:")
    head3 = create_linked_list([[3, None], [3, 0], [3, None]])
    print("Original:", head3)
    copied3 = solution.copyRandomList(head3)
    print("Copied:  ", copied3)

    # Edge case: empty list
    print("\nEdge case - empty list:")
    head4 = None
    copied4 = solution.copyRandomList(head4)
    print("Original: None")
    print("Copied:  ", copied4)