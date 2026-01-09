class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        return self._search_in_node(word, self.root)

    def _search_in_node(self, word, node):
        for i, ch in enumerate(word):
            if ch == '.':
                for child in node.children.values():
                    if self._search_in_node(word[i + 1:], child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                node = node.children[ch]
        return node.is_end+8

dict = WordDictionary()
dict.addWord("bad")
dict.addWord("dad")
dict.addWord("mad")

dict.search("pad")
# False (no 'p' child in root)
dict.search("bad")
#→ True (path exists and ends)
dict.search(".ad")
#→ True (tries 'b', 'd', 'm' → finds 'bad', 'dad', 'mad')
dict.search("b..")
#→ True ('b' → 'a' → 'd')