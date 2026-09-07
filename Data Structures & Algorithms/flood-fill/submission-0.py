class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orgColor = image[sr][sc]
        if orgColor == color:
            return image

        def dfsHelper(image, r, c, color, orgColor):
            Rows = len(image)
            Cols = len(image[0])
            if min(r,c) < 0:
                return
            if r == Rows or c == Cols:
                return
            if image[r][c] != orgColor:
                return
            
            image[r][c] = color
            dfsHelper(image, r + 1, c, color, orgColor)
            dfsHelper(image, r - 1, c, color, orgColor)
            dfsHelper(image, r, c + 1, color, orgColor)
            dfsHelper(image, r, c - 1, color, orgColor)

        dfsHelper(image, sr, sc, color, orgColor)
        return image
        