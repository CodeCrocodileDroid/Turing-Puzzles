class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, left, right):
            # If string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still can
            if left < n:
                backtrack(current + "(", left + 1, right)

            # Add ')' if valid
            if right < left:
                backtrack(current + ")", left, right + 1)

        backtrack("", 0, 0)
        return result


def test_generate_parentheses():
    sol = Solution()

    # Testcase 1
    n1 = 3
    output1 = sol.generateParenthesis(n1)
    print("Input:", n1)
    print("Test Result:", output1)
    # Expected: ["((()))","(()())","(())()","()(())","()()()"]

    # Testcase 2
    n2 = 1
    output2 = sol.generateParenthesis(n2)
    print("\nInput:", n2)
    print("Test Result:", output2)
    # Expected: ["()"]

    # Custom Testcase 3
    n3 = 2
    output3 = sol.generateParenthesis(n3)
    print("\nInput:", n3)
    print("Test Result:", output3)
    # Expected: ["(())","()()"]

if __name__ == "__main__":
    test_generate_parentheses()
