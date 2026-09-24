class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        self.max_word_length = 0

    def addWord(self, word: str) -> None:
        curr = self.root
        self.max_word_length = max(self.max_word_length, len(word))

        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        if len(word) > self.max_word_length:
            return False

        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.end
        return dfs(0, self.root)
            
