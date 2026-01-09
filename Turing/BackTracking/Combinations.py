class Solution:
    def combine(self, n, k):
        result = []
        path = []

        def backtrack(start):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return result



sol = Solution()
print(sol.combine(4, 2))  # Expected [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(sol.combine(1, 1))  # Expected [[1]]
