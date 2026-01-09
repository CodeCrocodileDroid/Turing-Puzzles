from collections import deque
import copy


class Solution:
    def solve(self, board):
        """DFS Solution"""
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = 'S'  # Mark as safe

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Mark border-connected 'O's as safe
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        for r in range(1, rows - 1):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # Convert remaining 'O's to 'X', restore safe 'S' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'


class Solution2:
    def solve(self, board):
        """BFS Solution"""
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def bfs(r, c):
            queue = deque([(r, c)])
            board[r][c] = 'S'

            while queue:
                row, col = queue.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                        board[nr][nc] = 'S'
                        queue.append((nr, nc))

        # Mark border-connected 'O's as safe
        for c in range(cols):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[rows - 1][c] == 'O':
                bfs(rows - 1, c)

        for r in range(1, rows - 1):
            if board[r][0] == 'O':
                bfs(r, 0)
            if board[r][cols - 1] == 'O':
                bfs(r, cols - 1)

        # Convert remaining 'O's to 'X', restore safe 'S' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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


class Solution3:
    def solve(self, board):
        """Union-Find Solution"""
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        uf = UnionFind(rows * cols + 1)
        dummy = rows * cols

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    idx = r * cols + c

                    # Connect border 'O's to dummy
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        uf.union(idx, dummy)

                    # Connect to neighbors
                    if r + 1 < rows and board[r + 1][c] == 'O':
                        uf.union(idx, (r + 1) * cols + c)
                    if c + 1 < cols and board[r][c + 1] == 'O':
                        uf.union(idx, r * cols + c + 1)

        # Flip 'O's not connected to dummy
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    idx = r * cols + c
                    if uf.find(idx) != uf.find(dummy):
                        board[r][c] = 'X'


def print_board(board):
    """Helper to print board"""
    for row in board:
        print("  " + " ".join(row))


# Test cases
if __name__ == "__main__":
    solution_dfs = Solution()
    solution_bfs = Solution2()
    solution_uf = Solution3()

    test_cases = [
        # (board, expected, test_name)
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"]
            ],
            "Example 1"
        ),
        (
            [["X"]],
            [["X"]],
            "Single cell"
        ),
        (
            [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"]
            ],
            [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"]
            ],
            "All O's touching borders"
        ),
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "X", "X"]
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"]
            ],
            "O's completely surrounded"
        ),
        (
            [
                ["X", "O", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]
            ],
            [
                ["X", "O", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]
            ],
            "O's connected to border"
        ),
        (
            [
                ["O", "X", "X", "O", "X"],
                ["X", "O", "O", "X", "O"],
                ["X", "O", "X", "O", "X"],
                ["O", "X", "O", "O", "O"],
                ["X", "X", "O", "X", "O"]
            ],
            [
                ["O", "X", "X", "O", "X"],
                ["X", "X", "X", "X", "O"],
                ["X", "X", "X", "O", "X"],
                ["O", "X", "O", "O", "O"],
                ["X", "X", "O", "X", "O"]
            ],
            "Complex pattern"
        ),
        (
            [
                ["X", "O", "X"],
                ["O", "X", "O"],
                ["X", "O", "X"]
            ],
            [
                ["X", "O", "X"],
                ["O", "X", "O"],
                ["X", "O", "X"]
            ],
            "Checkerboard pattern"
        ),
        (
            [
                ["X", "X", "X", "X", "O"],
                ["X", "O", "O", "X", "O"],
                ["X", "X", "O", "X", "O"],
                ["X", "O", "X", "O", "X"],
                ["O", "O", "X", "X", "X"]
            ],
            [
                ["X", "X", "X", "X", "O"],
                ["X", "X", "X", "X", "O"],
                ["X", "X", "X", "X", "O"],
                ["X", "O", "X", "O", "X"],
                ["O", "O", "X", "X", "X"]
            ],
            "Multiple regions"
        ),
    ]

    print("Testing Surrounded Regions")
    print("=" * 70)

    for i, (board_input, expected, test_name) in enumerate(test_cases):
        print(f"\nTest {i + 1}: {test_name}")
        print("Input board:")
        print_board(board_input)

        # Test all solutions
        board1 = copy.deepcopy(board_input)
        board2 = copy.deepcopy(board_input)
        board3 = copy.deepcopy(board_input)

        solution_dfs.solve(board1)
        solution_bfs.solve(board2)
        solution_uf.solve(board3)

        print("\nDFS Result:")
        print_board(board1)

        print("\nBFS Result:")
        print_board(board2)

        print("\nUnion-Find Result:")
        print_board(board3)

        print("\nExpected:")
        print_board(expected)

        dfs_match = board1 == expected
        bfs_match = board2 == expected
        uf_match = board3 == expected

        if dfs_match and bfs_match and uf_match:
            print("✓ ALL SOLUTIONS PASS")
        else:
            print("✗ SOME SOLUTIONS FAIL")
            if not dfs_match:
                print("  DFS failed")
            if not bfs_match:
                print("  BFS failed")
            if not uf_match:
                print("  Union-Find failed")

        # Show explanation for examples
        if test_name in ["Example 1", "O's completely surrounded", "All O's touching borders"]:
            print("\nExplanation:")
            if test_name == "Example 1":
                print("""
    Input has 2 regions of 'O':
    1. Region 1: (1,1), (1,2), (2,2) - Surrounded by 'X' ✓
    2. Region 2: (3,1) - On border, cannot be surrounded ✗

    Result: Only region 1 gets flipped to 'X'
                """)
            elif test_name == "O's completely surrounded":
                print("""
    All 'O's are completely surrounded by 'X':
    - No 'O' touches the border
    - All 'O's can be captured
    - All get flipped to 'X'
                """)
            elif test_name == "All O's touching borders":
                print("""
    All 'O's touch at least one border:
    - No 'O' is completely surrounded
    - None can be captured
    - All remain 'O'
                """)

    print("\n" + "=" * 70)

    # Algorithm explanations
    print("\nAlgorithm Explanations:")
    print("=" * 70)

    print("""
Key Insight: Instead of finding surrounded regions, find regions that are NOT surrounded.
            Regions that touch borders cannot be surrounded.

Solution 1 (DFS from borders):
1. Start DFS from all 'O's on borders
2. Mark all connected 'O's as safe (temporarily as 'S')
3. All remaining 'O's are surrounded → flip to 'X'
4. Restore safe 'S' back to 'O'

Solution 2 (BFS from borders):
1. Same logic as DFS but uses BFS
2. Better for avoiding recursion depth issues

Solution 3 (Union-Find):
1. Create Union-Find with dummy node for borders
2. Connect all border 'O's to dummy node
3. Connect all adjacent 'O's to each other
4. Any 'O' not connected to dummy is surrounded → flip to 'X'
""")

    print("\nTime & Space Complexity:")
    print("-" * 40)
    print("""
DFS/BFS: O(m×n) time, O(m×n) space worst case (recursion/queue)
Union-Find: O(m×n×α(m×n)) time, O(m×n) space
where α is inverse Ackermann function (very slow growing)
""")

    print("\n" + "=" * 70)

    # Step-by-step demonstration
    print("\nStep-by-step Demonstration for Example 1:")
    print("=" * 70)

    demo_board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]

    print("Initial board:")
    print_board(demo_board)

    print("\nDFS Solution Steps:")
    print("1. Scan borders for 'O':")
    print("   - Top row: no 'O'")
    print("   - Bottom row: (3,1) is 'O' → start DFS")
    print("   - Left column: (1,0), (2,0), (3,0) are 'X'")
    print("   - Right column: (1,3), (2,3), (3,3) are 'X'")
    print("\n2. Mark border-connected 'O's as 'S':")
    print("   - DFS from (3,1): only (3,1) itself (no other connected 'O's)")
    print("   - Mark (3,1) as 'S'")
    print("\n3. Current board (after marking safe):")
    intermediate = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "S", "X", "X"]
    ]
    print_board(intermediate)
    print("\n4. Final conversion:")
    print("   - All remaining 'O' → 'X': (1,1), (1,2), (2,2)")
    print("   - All 'S' → 'O': (3,1)")

    test_board = copy.deepcopy(demo_board)
    solution_dfs.solve(test_board)
    print("\nActual Result:")
    print_board(test_board)

    print("\n" + "=" * 70)

    # Common mistakes
    print("\nCommon Mistakes to Avoid:")
    print("=" * 70)

    print("""
1. Trying to find surrounded regions directly:
   - Hard to determine if region is completely surrounded
   - Reverse approach (find non-surrounded) is easier

2. Not handling border cases:
   - Must check all 4 borders
   - 'O's on borders can never be surrounded

3. Modifying while traversing:
   - Need temporary marker ('S') to avoid confusion
   - Or use separate visited set

4. Forgetting to restore markers:
   - After marking safe regions, restore them to 'O'

5. Union-Find implementation errors:
   - Forgetting dummy node for borders
   - Not connecting adjacent cells properly
""")

    print("\n" + "=" * 70)

    # For LeetCode submission
    print("\nRecommended Code for LeetCode Submission:")
    print("=" * 70)

    print("""DFS Solution:""")
    print("""
class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = 'S'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Mark border-connected 'O's
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        for r in range(1, rows - 1):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # Convert remaining 'O's to 'X', restore 'S' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
    """)

    print("\nNote: This modifies board in-place as required.")
    print("The algorithm runs in O(m×n) time and uses O(m×n) space for recursion stack.")