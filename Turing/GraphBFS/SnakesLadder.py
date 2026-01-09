from collections import deque


class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        target = n * n

        def get_coordinates(square):
            """Convert square number (1-indexed) to board coordinates (0-indexed)"""
            # Convert to 0-indexed
            square -= 1

            # Calculate row and column in the "unwrapped" board
            row = square // n
            col = square % n

            # Boustrophedon pattern: odd rows are reversed
            if row % 2 == 1:
                col = n - 1 - col

            # Convert to actual board indices (board is given top to bottom)
            row = n - 1 - row

            return row, col

        # BFS for shortest path
        visited = [False] * (target + 1)
        queue = deque([(1, 0)])  # (square, moves)
        visited[1] = True

        while queue:
            square, moves = queue.popleft()

            # Try all possible dice rolls
            for dice in range(1, 7):
                next_square = square + dice

                # Check bounds
                if next_square > target:
                    break

                # Check for snake or ladder
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]

                # Check if we reached the target
                if next_square == target:
                    return moves + 1

                # Add to queue if not visited
                if not visited[next_square]:
                    visited[next_square] = True
                    queue.append((next_square, moves + 1))

        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print(f"Example 1: {solution.snakesAndLadders(board1)}")  # Expected: 4

    # Example 2
    board2 = [[-1, -1], [-1, 3]]
    print(f"Example 2: {solution.snakesAndLadders(board2)}")  # Expected: 1

    # Additional test cases
    board3 = [[-1, 4], [-1, 3]]  # Simple ladder
    print(f"Test 3: {solution.snakesAndLadders(board3)}")  # Expected: 1

    board4 = [
        [-1, -1, -1],
        [-1, 9, 8],
        [-1, 7, -1]
    ]
    print(f"Test 4: {solution.snakesAndLadders(board4)}")  # 3x3 board

    # No snakes or ladders
    board5 = [[-1] * 4 for _ in range(4)]
    print(f"Test 5 (no snakes/ladders): {solution.snakesAndLadders(board5)}")  # 4 moves minimum

    # Impossible board
    board6 = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]
    print(f"Test 6 (all -1): {solution.snakesAndLadders(board6)}")  # Should be possible