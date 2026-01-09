from collections import deque

# LeetCode already provides TreeNode, but for local testing we define it here:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)

# Helper: level-order traversal to visualize tree like LeetCode output
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Test harness
def test_convert_sorted_array_to_bst():
    sol = Solution()

    # Testcase 1
    nums1 = [-10,-3,0,5,9]
    root1 = sol.sortedArrayToBST(nums1)
    print("Input:", nums1)
    print("Test Result:", level_order(root1))
    # Expected: [0,-3,9,-10,None,5]

    # Testcase 2
    nums2 = [1,3]
    root2 = sol.sortedArrayToBST(nums2)
    print("\nInput:", nums2)
    print("Test Result:", level_order(root2))
    # Expected: [3,1] or [1,None,3]

    # Testcase 3
    nums3 = [1,2,3,4,5,6,7]
    root3 = sol.sortedArrayToBST(nums3)
    print("\nInput:", nums3)
    print("Test Result:", level_order(root3))
    # Expected: [4,2,6,1,3,5,7]

if __name__ == "__main__":
    test_convert_sorted_array_to_bst()
