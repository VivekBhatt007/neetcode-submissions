# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def myMergeSort(paris, start, end):
            if end - start + 1 <= 1:
                return paris
            
            mid = (start + end) // 2
            myMergeSort(paris, start, mid)
            myMergeSort(paris, mid + 1, end)

            merge(paris, start, mid, end)
            return paris
        
        def merge(paris, start, mid, end):
            L = paris[start: mid+1]
            R = paris[mid+1 : end + 1]

            l_idx = 0
            r_idx = 0
            i = start
            while l_idx < len(L) and r_idx < len(R):
                if L[l_idx].key <= R[r_idx].key:
                    paris[i] = L[l_idx]
                    l_idx += 1
                else:
                    pairs[i] = R[r_idx]
                    r_idx += 1
                i += 1
            while l_idx < len(L):
                paris[i] = L[l_idx]
                i += 1
                l_idx += 1
            while r_idx < len(R):
                pairs[i] = R[r_idx]
                i += 1
                r_idx += 1

        return myMergeSort(pairs, 0, len(pairs))
