class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols= len(image), len(image[0])
        new_image = [row[:] for row in image]

        initial_color = image[sr][sc]

        # if the start_color is same as color return
        if initial_color == color:
            return new_image
        
        def dfs(r,c):
            # out of bound
            if r <0 or r >= rows or c<0 or c>=cols:
                return
            
            # if the start color is different return
            if new_image[r][c] != initial_color:
                return
            
            # Already in new color
            # if new_image[r][c] == color:
            #     return
            
            # change color
            new_image[r][c] = color

            # call neighbouring dfs
            dfs(r+1, c) #--> down
            dfs(r-1, c) #---> up
            dfs(r, c+1) #---> right
            dfs(r, c-1) #---> left
        dfs(sr, sc)
        return new_image
        