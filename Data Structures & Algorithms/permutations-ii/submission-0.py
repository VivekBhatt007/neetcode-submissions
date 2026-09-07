class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        param = [[]]
        seen = set()  # Store as tuples for hashability

        for n in nums:
            temp = []
            for p in param:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    perm_tuple = tuple(pCopy)
                    if perm_tuple not in seen:
                        seen.add(perm_tuple)
                        temp.append(pCopy)
            param = temp

        return param    