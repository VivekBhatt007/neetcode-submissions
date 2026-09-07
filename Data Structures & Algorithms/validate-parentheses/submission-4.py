class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            elif ch == ']':
                if st == [] or st[-1] != '[':
                    return False
                st.pop()
            elif ch == ')':
                if st == [] or st[-1] != '(':
                    return False
                st.pop()
            elif ch == '}':
                if st == [] or st[-1] != '{':
                    return False
                st.pop()
        if st != [] :
            return False
        return True
        