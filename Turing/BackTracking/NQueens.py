class Solution:
    def totalNQueens(self, n):
        self.count = 0

        # sets to track attacked columns and diagonals
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def backtrack(r):
            if r == n:
                self.count += 1
                return
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                # place queen
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                backtrack(r + 1)

                # remove queen
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return self.count

def test_nqueensII():
    sol = Solution()

    # Testcase 1
    n1 = 4
    output1 = sol.totalNQueens(n1)
    print("Input:", n1)
    print("Test Result:", output1)
    # Expected: 2

    # Testcase 2
    n2 = 1
    output2 = sol.totalNQueens(n2)
    print("\nInput:", n2)
    print("Test Result:", output2)
    # Expected: 1

    # Custom Testcase 3
    n3 = 5
    output3 = sol.totalNQueens(n3)
    print("\nInput:", n3)
    print("Test Result:", output3)
    # Expected: 10

    # Custom Testcase 4
    n4 = 6
    output4 = sol.totalNQueens(n4)
    print("\nInput:", n4)
    print("Test Result:", output4)
    # Expected: 4

if __name__ == "__main__":
    test_nqueensII()
