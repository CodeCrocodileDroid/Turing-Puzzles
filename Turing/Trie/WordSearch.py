class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word at terminal node

class Solution:
    def findWords(self, board, words):
        # Step 1: Build Trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w  # mark end of word

        rows, cols = len(board), len(board[0])
        result = []

        # Step 2: DFS
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]

            if nxt.word:
                result.append(nxt.word)
                nxt.word = None  # avoid duplicates

            # mark visited
            board[r][c] = "#"
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch  # restore

            # optimization: prune empty nodes
            if not nxt.children:
                node.children.pop(ch)

        # Step 3: Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result









board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
def test_word_search():
    sol = Solution()

    # Example 1
    board1 = [["o","a","a","n"],
              ["e","t","a","e"],
              ["i","h","k","r"],
              ["i","f","l","v"]]
    words1 = ["oath","pea","eat","rain"]
    print("Test 1 Output:", sol.findWords(board1, words1))
    # Expected: ["eat","oath"]

    # Example 2
    board2 = [["a","b"],
              ["c","d"]]
    words2 = ["abcb"]
    print("Test 2 Output:", sol.findWords(board2, words2))
    # Expected: []

    # Custom Test 3
    board3 = [["a","a"]]
    words3 = ["aaa"]
    print("Test 3 Output:", sol.findWords(board3, words3))
    # Expected: [] (cannot reuse same cell twice)

    # Custom Test 4
    board4 = [["a","b","c"],
              ["a","e","d"],
              ["a","f","g"]]
    words4 = ["abcdefg","aed","abcf"]
    print("Test 4 Output:", sol.findWords(board4, words4))
    # Expected: ["abcdefg","aed","abcf"]

if __name__ == "__main__":
    test_word_search()
