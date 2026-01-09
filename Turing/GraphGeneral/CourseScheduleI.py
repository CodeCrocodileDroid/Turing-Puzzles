from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """Topological Sort (Kahn's Algorithm)"""
        # Create adjacency list and indegree array
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph: prereq → course
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        # Process courses
        while queue:
            course = queue.popleft()
            completed += 1

            # Decrease indegree of neighbors
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses


class Solution2:
    def canFinish(self, numCourses, prerequisites):
        """DFS with Cycle Detection"""
        # Create adjacency list
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def hasCycle(course):
            if state[course] == 1:  # Found a cycle
                return True
            if state[course] == 2:  # Already processed
                return False

            # Mark as visiting
            state[course] = 1

            # Check all neighbors
            for neighbor in adj[course]:
                if hasCycle(neighbor):
                    return True

            # Mark as visited
            state[course] = 2
            return False

        # Check each course for cycles
        for course in range(numCourses):
            if state[course] == 0:
                if hasCycle(course):
                    return False

        return True


class Solution3:
    def canFinish(self, numCourses, prerequisites):
        """Alternative Topological Sort"""
        if numCourses <= 0:
            return True

        # Build graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # Find all sources
        sources = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                sources.append(i)

        # Process topological sort
        sorted_order = []
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)

            for child in graph[vertex]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)

        return len(sorted_order) == numCourses


# Test cases
if __name__ == "__main__":
    solution_bfs = Solution()
    solution_dfs = Solution2()
    solution_topo = Solution3()

    test_cases = [
        # (numCourses, prerequisites, expected, test_name)
        (2, [[1, 0]], True, "Example 1"),
        (2, [[1, 0], [0, 1]], False, "Example 2 - Cycle"),
        (1, [], True, "Single course, no prerequisites"),
        (3, [[1, 0], [2, 1]], True, "Linear chain"),
        (3, [[1, 0], [2, 1], [0, 2]], False, "3-cycle"),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True, "Diamond pattern"),
        (4, [[1, 0], [2, 1], [3, 2], [0, 3]], False, "4-cycle"),
        (5, [], True, "No prerequisites"),
        (3, [[0, 1], [0, 2], [1, 2]], True, "Multiple prerequisites"),
        (4, [[0, 1], [1, 2], [2, 3], [3, 0]], False, "Large cycle"),
        (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]], True, "Long chain"),
        (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]], False, "Long cycle"),
        (7, [[1, 0], [2, 1], [3, 1], [4, 2], [5, 3], [6, 4], [6, 5]], True, "Complex DAG"),
    ]

    print("Testing Course Schedule")
    print("=" * 70)

    for i, (numCourses, prerequisites, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print(f"numCourses: {numCourses}")
        print(f"prerequisites: {prerequisites}")

        result_bfs = solution_bfs.canFinish(numCourses, prerequisites)
        result_dfs = solution_dfs.canFinish(numCourses, prerequisites)
        result_topo = solution_topo.canFinish(numCourses, prerequisites)

        print(f"\nBFS (Topological Sort): {result_bfs}")
        print(f"DFS (Cycle Detection):  {result_dfs}")
        print(f"Alternative Topo Sort:  {result_topo}")
        print(f"Expected:               {expected}")

        if result_bfs == expected and result_dfs == expected and result_topo == expected:
            print("✓ ALL SOLUTIONS PASS")
        else:
            print("✗ SOME SOLUTIONS FAIL")
            if result_bfs != expected:
                print(f"  BFS failed: got {result_bfs}, expected {expected}")
            if result_dfs != expected:
                print(f"  DFS failed: got {result_dfs}, expected {expected}")
            if result_topo != expected:
                print(f"  Alternative Topo failed: got {result_topo}, expected {expected}")

        # Show graph visualization for small examples
        if test_name in ["Example 1", "Example 2 - Cycle", "Linear chain"]:
            print("\nGraph Representation:")
            if test_name == "Example 1":
                print("""
    Courses: 0, 1
    Prerequisites: [1, 0] means "1 requires 0"

    Graph: 0 → 1
    No cycle → Possible
                """)
            elif test_name == "Example 2 - Cycle":
                print("""
    Courses: 0, 1
    Prerequisites: [1, 0], [0, 1]

    Graph: 0 ⇄ 1 (cycle)
    1 requires 0, and 0 requires 1
    Impossible → Cycle detected
                """)
            elif test_name == "Linear chain":
                print("""
    Courses: 0, 1, 2
    Prerequisites: [1, 0], [2, 1]

    Graph: 0 → 1 → 2
    Linear chain, no cycle → Possible
                """)

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Solution 1 (Topological Sort - Kahn's Algorithm):
1. Build graph and calculate indegree for each node
2. Add all nodes with indegree 0 to queue
3. Process queue:
   - Remove node, add to topological order
   - Decrease indegree of neighbors
   - Add neighbors with indegree 0 to queue
4. If topological order contains all nodes → no cycle

Solution 2 (DFS with Cycle Detection):
1. Build graph
2. Use DFS with 3 states:
   - 0 = unvisited
   - 1 = visiting (in current DFS path)
   - 2 = visited (processed)
3. If we encounter a node with state 1 → cycle detected
4. If all nodes processed without cycle → possible

Solution 3 (Alternative Topological Sort):
1. Similar to Solution 1 but tracks sorted order
2. Returns True if sorted order length == numCourses
""")

    print("\nKey Insight:")
    print("-" * 40)
    print("""
This is a classic directed graph cycle detection problem.

If there's a cycle in the prerequisites graph:
- Course A requires B, B requires C, C requires A
- Impossible to finish all courses
- Return False

If no cycles (DAG - Directed Acyclic Graph):
- Can find topological ordering
- Possible to finish all courses
- Return True
""")

    print("\n" + "=" * 70)

    # Step-by-step demonstration
    print("\nStep-by-step Demonstration for Example 1:")
    print("=" * 70)

    numCourses = 2
    prerequisites = [[1, 0]]

    print(f"numCourses: {numCourses}")
    print(f"prerequisites: {prerequisites}")
    print("\nGraph: 0 → 1 (0 must be taken before 1)")

    print("\nBFS Topological Sort Execution:")
    print("1. Build graph:")
    print("   adj[0] = [1], adj[1] = []")
    print("   indegree[0] = 0, indegree[1] = 1")
    print("\n2. Initialize queue with nodes having indegree 0:")
    print("   queue = [0]")
    print("\n3. Process queue:")
    print("   - Pop 0: completed = 1")
    print("   - Process neighbors of 0: [1]")
    print("   - indegree[1]-- → indegree[1] = 0")
    print("   - Add 1 to queue")
    print("   - Pop 1: completed = 2")
    print("\n4. Check: completed (2) == numCourses (2) → True")

    result = solution_bfs.canFinish(numCourses, prerequisites)
    print(f"\nActual Result: {result}")

    print("\n" + "=" * 70)

    print("\nStep-by-step for Example 2 (Cycle):")
    print("=" * 70)

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    print(f"prerequisites: {prerequisites}")
    print("\nGraph: 0 ⇄ 1 (cycle)")

    print("\nBFS Topological Sort Execution:")
    print("1. Build graph:")
    print("   adj[0] = [1], adj[1] = [0]")
    print("   indegree[0] = 1, indegree[1] = 1")
    print("\n2. Initialize queue:")
    print("   No nodes with indegree 0 → queue = []")
    print("\n3. Process queue: queue is empty")
    print("   completed = 0")
    print("\n4. Check: completed (0) != numCourses (2) → False")

    result = solution_bfs.canFinish(numCourses, prerequisites)
    print(f"\nActual Result: {result}")

    print("\n" + "=" * 70)

    # Complexity analysis
    print("\nComplexity Analysis:")
    print("=" * 70)

    print("""
Time Complexity: O(V + E)
- V = numCourses (vertices)
- E = prerequisites.length (edges)
- Each node and edge processed once

Space Complexity: O(V + E)
- Adjacency list: O(V + E)
- Indegree array: O(V)
- Queue/Stack: O(V)

All solutions have same time and space complexity.
""")

    print("\n" + "=" * 70)

    # Common mistakes
    print("\nCommon Mistakes to Avoid:")
    print("=" * 70)

    print("""
1. Not handling empty prerequisites list
2. Building graph in wrong direction
3. Forgetting to initialize data structures properly
4. Not checking all courses (some might be disconnected)
5. Incorrect cycle detection logic
6. Not updating indegree correctly in BFS
""")

    print("\nGraph Direction Important:")
    print("-" * 40)
    print("""
prerequisites[i] = [ai, bi] means "ai requires bi"

Correct: bi → ai (edge from bi to ai)
Wrong:   ai → bi (would give wrong results)

Think: "To take course ai, you need bi first"
      So bi is prerequisite, comes before ai
      Graph edge: bi → ai
""")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)

    print("""BFS Topological Sort (Kahn's Algorithm):""")
    print("""
from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Create adjacency list and indegree array
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph: prereq → course
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        # Process courses
        while queue:
            course = queue.popleft()
            completed += 1

            # Decrease indegree of neighbors
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
    """)

    print("\nDFS Cycle Detection:")
    print("""
class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Create adjacency list
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def hasCycle(course):
            if state[course] == 1:  # Found a cycle
                return True
            if state[course] == 2:  # Already processed
                return False

            # Mark as visiting
            state[course] = 1

            # Check all neighbors
            for neighbor in adj[course]:
                if hasCycle(neighbor):
                    return True

            # Mark as visited
            state[course] = 2
            return False

        # Check each course for cycles
        for course in range(numCourses):
            if state[course] == 0:
                if hasCycle(course):
                    return False

        return True
    """)

    print("\nNote: Both solutions are valid.")
    print("BFS is more intuitive for topological sort.")
    print("DFS is more elegant for cycle detection.")