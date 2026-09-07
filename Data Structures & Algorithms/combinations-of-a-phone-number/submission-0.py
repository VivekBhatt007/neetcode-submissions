class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        res = []
        digitStr = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8":"tuv", "9":"wxyz"
            }
        
        def helper(idx, combi):
            if idx == len(digits):
                res.append(combi)
                return
            
            chars = digitStr[digits[idx]]
            for char in chars:
                helper(idx +1, combi + char)
        
        helper(0, "")
        return res