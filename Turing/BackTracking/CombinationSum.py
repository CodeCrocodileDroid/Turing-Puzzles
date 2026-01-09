class Solution:
    def combinationSum(self, candidates, target):
        result = []
        path = []

        def backtrack(start, total):
            # If total equals target, add current path
            if total == target:
                result.append(path[:])
                return
            # If total exceeds target, stop
            if total > target:
                return

            # Explore candidates starting from 'start'
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, total + candidates[i])  # allow reuse of same candidate
                path.pop()

        backtrack(0, 0)
        return result


def test_combination_sum():
    sol = Solution()

    # Testcase 1
    candidates1, target1 = [2,3,6,7], 7
    output1 = sol.combinationSum(candidates1, target1)
    print("Input:", candidates1, target1)
    print("Test Result:", output1)
    # Expected: [[2,2,3],[7]]

    # Testcase 2
    candidates2, target2 = [2,3,5], 8
    output2 = sol.combinationSum(candidates2, target2)
    print("\nInput:", candidates2, target2)
    print("Test Result:", output2)
    # Expected: [[2,2,2,2],[2,3,3],[3,5]]

    # Testcase 3
    candidates3, target3 = [2], 1
    output3 = sol.combinationSum(candidates3, target3)
    print("\nInput:", candidates3, target3)
    print("Test Result:", output3)
    # Expected: []

    # Custom Testcase 4
    candidates4, target4 = [1], 2
    output4 = sol.combinationSum(candidates4, target4)
    print("\nInput:", candidates4, target4)
    print("Test Result:", output4)
    # Expected: [[1,1]]

if __name__ == "__main__":
    test_combination_sum()
