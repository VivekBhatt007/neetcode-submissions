class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        max_f = 0
        l = 0
        max_len = 0
        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            max_f = max(max_f, mp[s[r]])
            if (r - l + 1) - max_f > k:
                if mp[s[l]] == 1:
                    del mp[s[l]]
                else:
                    mp[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
        