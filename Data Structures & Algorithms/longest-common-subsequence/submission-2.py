class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        def dfs(n1, n2, cache) -> int:
            if n1 == l1 or n2 == l2:
                return 0
            
            if (n1,n2) in cache:
                return cache[(n1,n2)]
            count = 0
            if text1[n1] == text2[n2]:
                count = 1 + dfs(n1+1, n2+1, cache)
            else:
                count += max(dfs(n1+1, n2, cache), dfs(n1, n2+1, cache))
            cache[(n1,n2)] = count
            return count
        
        return dfs(0, 0, {})
        