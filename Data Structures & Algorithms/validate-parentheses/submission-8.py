class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        # for ch in s:
        #     if ch == '(' or ch == '[' or ch == '{':
        #         st.append(ch)
        #     elif ch == ']':
        #         if st == [] or st[-1] != '[':
        #             return False
        #         st.pop()
        #     elif ch == ')':
        #         if st == [] or st[-1] != '(':
        #             return False
        #         st.pop()
        #     elif ch == '}':
        #         if st == [] or st[-1] != '{':
        #             return False
        #         st.pop()
        # if st != [] :
        #     return False
        cToO = {")": "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in cToO:
                if st and st[-1] == cToO[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False
        