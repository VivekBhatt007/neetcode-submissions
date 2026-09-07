class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        param = [[]]

        for n in nums:
            temp = []
            for p in param:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    temp.append(pCopy)
            param = temp
        return param
        