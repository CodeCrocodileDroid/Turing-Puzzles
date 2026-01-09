class Solution:
    def permute(self, nums):
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            # If path has all numbers, add to result
            if len(path) == len(nums):
                result.append(path[:])
                return
            # Try each unused number
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False

        backtrack()
        return result


def test_permutations():
    sol = Solution()

    # Testcase 1
    nums1 = [1,2,3]
    output1 = sol.permute(nums1)
    print("Input:", nums1)
    print("Test Result:", output1)
    # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    # Testcase 2
    nums2 = [0,1]
    output2 = sol.permute(nums2)
    print("\nInput:", nums2)
    print("Test Result:", output2)
    # Expected: [[0,1],[1,0]]

    # Testcase 3
    nums3 = [1]
    output3 = sol.permute(nums3)
    print("\nInput:", nums3)
    print("Test Result:", output3)
    # Expected: [[1]]

if __name__ == "__main__":
    test_permutations()
