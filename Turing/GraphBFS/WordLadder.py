from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # Convert wordList to a set for O(1) lookups
        word_set = set(wordList)

        # If endWord is not in the wordList, return 0
        if endWord not in word_set:
            return 0

        # BFS initialization
        queue = deque()
        queue.append((beginWord, 1))  # (word, level)
        visited = set([beginWord])

        # BFS traversal
        while queue:
            current_word, level = queue.popleft()

            # If we found the endWord, return the level
            if current_word == endWord:
                return level

            # Try all possible transformations
            for i in range(len(current_word)):
                # Try all 26 lowercase letters
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # Skip if it's the same character
                    if char == current_word[i]:
                        continue

                    # Create the new word
                    new_word = current_word[:i] + char + current_word[i + 1:]

                    # Check if new_word is valid and not visited
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, level + 1))

        return 0


sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Should print 5
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # Should print 0