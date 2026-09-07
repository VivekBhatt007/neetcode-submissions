class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row -1
        while l <= r:
            r_m = (l + r) // 2
            if target >= matrix[r_m][0] and target <= matrix[r_m][col -1]:
                break
            elif target > matrix[r_m][col - 1]:
                l = r_m + 1
            else:
                r = r_m - 1
        
        if not l <= r:
            return False
        l = 0
        r = col - 1
        while l <= r:
            c_m = (l + r) // 2
            if target == matrix[r_m][c_m]:
                return True
            elif target > matrix[r_m][c_m]:
                l = c_m + 1
            else:
                r = c_m - 1
        return False
        