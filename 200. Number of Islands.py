class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w = len(grid[0])
        h = len(grid)
        
        def dfs(x, y):
            if (0 <= x < h and 0 <= y < w) and (grid[x][y] == "1"):
                grid[x][y] = "0"
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
                return True
            return False
    
        res = 0

        for i in range(h):
            for j in range(w):
                if dfs(i, j) == True:
                    res += 1
                
        return res