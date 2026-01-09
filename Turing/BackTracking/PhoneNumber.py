class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        # Mapping of digits to letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(index, current):
            # Base case: if we've processed all digits
            if index == len(digits):
                result.append(current)
                return

            # Get letters for current digit
            digit = digits[index]
            letters = phone_map[digit]

            # Try each letter
            for letter in letters:
                backtrack(index + 1, current + letter)

        backtrack(0, "")
        return result