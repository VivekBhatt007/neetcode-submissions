class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        res = 0
        s_len = len(s)
        st = set()
        while r < s_len:
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            res = max(res, r - l +1)
            r += 1
        return res

        