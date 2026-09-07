class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.preMat = [ [0] * (cols + 1) for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                self.preMat[r+1][c+1] = (matrix[r][c] + 
                                         self.preMat[r][c+1] +
                                         self.preMat[r+1][c] -
                                         self.preMat[r][c])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1 , col1+1 , row2+1, col2+1
        bottom = self.preMat[r2][c2]
        above = self.preMat[r1-1][c2]
        left = self.preMat[r2][c1-1]
        top = self.preMat[r1-1][c1-1]
        return bottom - above - left + top
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)