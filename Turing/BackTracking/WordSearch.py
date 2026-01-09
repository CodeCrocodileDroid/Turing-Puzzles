class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            # If all characters matched
            if idx == len(word):
                return True
            # Out of bounds or mismatch
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False

            # Mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore neighbors
            found = (dfs(r+1, c, idx+1) or
                     dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or
                     dfs(r, c-1, idx+1))

            # Restore cell
            board[r][c] = temp
            return found

        # Try starting from each cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


def test_word_search():
    sol = Solution()

    # Testcase 1
    board1 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word1 = "ABCCED"
    print("Input:", word1)
    print("Test Result:", sol.exist(board1, word1))
    # Expected: True

    # Testcase 2
    board2 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word2 = "SEE"
    print("\nInput:", word2)
    print("Test Result:", sol.exist(board2, word2))
    # Expected: True

    # Testcase 3
    board3 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word3 = "ABCB"
    print("\nInput:", word3)
    print("Test Result:", sol.exist(board3, word3))
    # Expected: False

if __name__ == "__main__":
    test_word_search()
