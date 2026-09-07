class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.end            
            c = word[idx]
            if c == '.':
                for child in node.child.values():
                    if dfs(idx+1, child):
                        return True
                return False
            else:
                if c not in node.child:
                    return False
                return dfs(idx+1, node.child[c])
        return dfs(0, self.root)
        
