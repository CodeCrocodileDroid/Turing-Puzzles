from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        """DFS Recursive Solution"""
        if not node:
            return None

        clones = {}

        def dfs(original):
            if original in clones:
                return clones[original]

            clone = Node(original.val)
            clones[original] = clone

            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


class Solution2:
    def cloneGraph(self, node):
        """BFS Iterative Solution"""
        if not node:
            return None

        clones = {}
        clones[node] = Node(node.val)

        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]


# Test the solution
if __name__ == "__main__":
    # Example 1: [[2,4],[1,3],[2,4],[1,3]]

    # Create original graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloned = solution.cloneGraph(node1)

    # Verify the clone
    print("Original graph structure:")
    print(f"Node {node1.val} neighbors: {[n.val for n in node1.neighbors]}")
    print(f"Node {node2.val} neighbors: {[n.val for n in node2.neighbors]}")
    print(f"Node {node3.val} neighbors: {[n.val for n in node3.neighbors]}")
    print(f"Node {node4.val} neighbors: {[n.val for n in node4.neighbors]}")

    print("\nCloned graph structure:")
    print(f"Node {cloned.val} neighbors: {[n.val for n in cloned.neighbors]}")

    # Check that clone is deep copy (different objects)
    print(f"\nAre node1 and clone the same object? {node1 is cloned}")
    print(f"Are node1's neighbors same as clone's neighbors? {node1.neighbors is cloned.neighbors}")