from collections import deque


class Solution:
    def numIslands(self, grid):
        """DFS Solution"""
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Check boundaries and if current cell is land
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return

            # Mark current cell as visited by changing it to '0'
            grid[r][c] = '0'

            # Visit all adjacent cells
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands


class Solution2:
    def numIslands(self, grid):
        """BFS Solution"""
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'  # Mark as visited

            while queue:
                row, col = queue.popleft()

                # Check all 4 directions
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)

        return islands


class UnionFind:
    """Union-Find data structure for Solution3"""

    def __init__(self, grid):
        rows, cols = len(grid), len(grid[0])
        self.parent = [-1] * (rows * cols)
        self.rank = [0] * (rows * cols)
        self.count = 0

        # Initialize parent for each land cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    idx = r * cols + c
                    self.parent[idx] = idx
                    self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1


class Solution3:
    def numIslands(self, grid):
        """Union-Find Solution"""
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(grid)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    idx = r * cols + c

                    # Check right neighbor
                    if c + 1 < cols and grid[r][c + 1] == '1':
                        uf.union(idx, r * cols + (c + 1))

                    # Check down neighbor
                    if r + 1 < rows and grid[r + 1][c] == '1':
                        uf.union(idx, (r + 1) * cols + c)

        return uf.count


def print_grid(grid):
    """Helper to print grid nicely"""
    for row in grid:
        print("  " + " ".join(row))


# Test cases
if __name__ == "__main__":
    solution_dfs = Solution()
    solution_bfs = Solution2()
    solution_uf = Solution3()

    test_cases = [
        # (grid, expected, test_name)
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            1,
            "Example 1"
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            3,
            "Example 2"
        ),
        (
            [
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            0,
            "All water"
        ),
        (
            [
                ["1", "1", "1"],
                ["1", "1", "1"],
                ["1", "1", "1"]
            ],
            1,
            "All land - single island"
        ),
        (
            [
                ["1", "0", "1", "0", "1"],
                ["0", "1", "0", "1", "0"],
                ["1", "0", "1", "0", "1"],
                ["0", "1", "0", "1", "0"]
            ],
            10,
            "Checkerboard pattern"
        ),
        (
            [
                ["1", "0", "0", "0", "1"],
                ["0", "1", "0", "1", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "1", "0", "1", "0"],
                ["1", "0", "0", "0", "1"]
            ],
            9,
            "Diagonal islands"
        ),
        (
            [
                ["1", "1", "0", "0", "0", "1"],
                ["1", "1", "0", "0", "0", "0"],
                ["0", "0", "1", "0", "1", "0"],
                ["0", "0", "0", "1", "1", "0"],
                ["1", "0", "1", "0", "0", "1"]
            ],
            5,
            "Complex pattern"
        ),
        (
            [["1"]],
            1,
            "Single cell land"
        ),
        (
            [["0"]],
            0,
            "Single cell water"
        ),
    ]

    print("Testing Number of Islands")
    print("=" * 70)

    for i, (grid_input, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print("Grid:")
        print_grid(grid_input)

        # Need to create copies since solutions modify the grid
        import copy

        grid1 = copy.deepcopy(grid_input)
        grid2 = copy.deepcopy(grid_input)
        grid3 = copy.deepcopy(grid_input)

        result_dfs = solution_dfs.numIslands(grid1)
        result_bfs = solution_bfs.numIslands(grid2)
        result_uf = solution_uf.numIslands(grid3)

        print(f"\nDFS Result:  {result_dfs}")
        print(f"BFS Result:  {result_bfs}")
        print(f"Union-Find:  {result_uf}")
        print(f"Expected:    {expected}")

        if result_dfs == expected and result_bfs == expected and result_uf == expected:
            print("✓ ALL SOLUTIONS PASS")
        else:
            print("✗ SOME SOLUTIONS FAIL")
            if result_dfs != expected:
                print(f"  DFS failed: got {result_dfs}, expected {expected}")
            if result_bfs != expected:
                print(f"  BFS failed: got {result_bfs}, expected {expected}")
            if result_uf != expected:
                print(f"  Union-Find failed: got {result_uf}, expected {expected}")

        # Show island detection for small examples
        if test_name in ["Example 1", "Example 2", "Single cell land"]:
            print("\nIsland Detection Process:")
            if test_name == "Example 1":
                print("""
    Starting grid (1 island):
      1 1 1 1 0
      1 1 0 1 0
      1 1 0 0 0
      0 0 0 0 0

    DFS/BFS process:
    1. Start at (0,0) - find '1'
    2. Mark all connected '1's as visited (change to '0')
    3. Connected region includes all land cells
    4. Count = 1 island
                """)
            elif test_name == "Example 2":
                print("""
    Starting grid (3 islands):
      1 1 0 0 0
      1 1 0 0 0
      0 0 1 0 0
      0 0 0 1 1

    DFS/BFS process:
    1. Start at (0,0) - find '1'
    2. Mark top-left 2x2 block as visited
    3. Count island #1
    4. Continue scanning, find (2,2) - '1'
    5. Mark single cell as visited
    6. Count island #2
    7. Continue scanning, find (3,3) - '1'
    8. Mark bottom-right 2x1 block as visited
    9. Count island #3
                """)

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Solution 1 (DFS - Depth-First Search):
1. Scan grid cell by cell
2. When find '1' (land):
   - Increment island count
   - Perform DFS to mark all connected land cells as visited
3. DFS recursively visits up, down, left, right
4. Mark visited cells by changing '1' to '0'
5. Time: O(m×n), Space: O(m×n) worst case (recursion stack)

Solution 2 (BFS - Breadth-First Search):
1. Similar to DFS but uses queue instead of recursion
2. When find '1':
   - Increment island count
   - Perform BFS to mark connected land cells
3. BFS uses queue to visit cells level by level
4. Time: O(m×n), Space: O(min(m,n)) for queue

Solution 3 (Union-Find / Disjoint Set Union):
1. Initialize each land cell as separate set
2. Union adjacent land cells (right and down only)
3. Number of islands = number of sets
4. Time: O(m×n×α(m×n)) where α is inverse Ackermann (very slow growing)
5. Space: O(m×n)
""")

    print("\n" + "=" * 70)

    # Step-by-step DFS demonstration
    print("\nStep-by-step DFS Demonstration for Example 1:")
    print("=" * 70)

    demo_grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print("Initial grid:")
    print_grid(demo_grid)

    print("\nDFS Execution:")
    print("1. Start at (0,0): find '1' → island count = 1")
    print("2. Call dfs(0,0):")
    print("   - Mark (0,0) as visited → change to '0'")
    print("   - Recursively call neighbors:")
    print("     dfs(1,0) → dfs(2,0) → dfs(1,1) → dfs(0,1) → dfs(0,2) → dfs(0,3)")
    print("     dfs(1,3) → ... (all connected land)")
    print("3. All connected land marked as '0'")
    print("4. Continue scanning, no more '1's found")
    print("5. Return count = 1")

    result = solution_dfs.numIslands([row[:] for row in demo_grid])
    print(f"\nActual Result: {result}")

    print("\n" + "=" * 70)

    # Complexity comparison
    print("\nComplexity Comparison:")
    print("=" * 70)

    print("""
| Algorithm  | Time Complexity | Space Complexity | Best For          |
|------------|-----------------|------------------|-------------------|
| DFS        | O(m×n)          | O(m×n) worst*    | Simple, recursive |
| BFS        | O(m×n)          | O(min(m,n))      | Avoid recursion   |
| Union-Find | O(m×n×α(n))     | O(m×n)           | Dynamic updates   |

* DFS recursion stack could be O(m×n) in worst case (all land)
  but typically O(min(m,n)) for grid problems
""")

    print("\nNote: α(n) is inverse Ackermann function, grows very slowly")
    print("      For practical purposes, α(n) ≤ 5 for n < 2^65536")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)

    print("""DFS Solution (most common):""")
    print("""
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands
    """)

    print("\nBFS Solution (avoids recursion depth issues):")
    print("""
from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'

            while queue:
                row, col = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)

        return islands
    """)