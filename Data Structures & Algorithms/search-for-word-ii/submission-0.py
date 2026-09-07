class TrieNode:
    def __init__(self):
        self.childs = {}
        self.word = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.childs:
                curr.childs[c] = TrieNode()
            curr = curr.childs[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for w in words:
            root.addWord(w)

        R, C = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):

            if (r < 0 or c < 0 or
            r >= R or c >= C or
            (r, c) in visit or
            board[r][c] not in node.childs):
                return

            visit.add((r,c))
            node = node.childs[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c))

        for r in range(R):
            for c in range(C):
                dfs(r, c, root, "")
        return list(res)
            







