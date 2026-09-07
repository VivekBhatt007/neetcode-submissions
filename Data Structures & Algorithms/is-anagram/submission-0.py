class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        for c in s:
            if c not in mp:
                mp[c] = 1
            else:
                mp[c] += 1
        
        for c in t:
            if c not in mp:
                return False
            if mp[c] == 1:
                mp.pop(c, None)
            elif mp[c] > 1:
                mp[c] -= 1
        return True if not mp else False
        