class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [False for i in range(len(grid) * len(grid[0]))]
        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i*len(grid[0]) + j] and grid[i][j] == '1':
                    numIslands += 1
                    self.explore(i, j, visited, grid)
        return numIslands
    def explore(self, i, j, visited, grid):
        visited[i*len(grid[0]) + j] = True
        if i != 0 and not visited[(i-1)*len(grid[0]) + j] and grid[i][j] == grid[i-1][j]:
            self.explore(i-1, j, visited, grid)
        if i != (len(grid)-1) and not visited[(i+1)*len(grid[0]) + j] and grid[i][j] == grid[i+1][j]:
            self.explore(i+1, j, visited, grid)
        if j != 0 and not visited[i*len(grid[0]) + j - 1] and grid[i][j] == grid[i][j-1]:
            self.explore(i, j-1, visited, grid)
        if j != (len(grid[0]) - 1) and not visited[i*len(grid[0]) + j + 1] and grid[i][j] == grid[i][j+1]:
            self.explore(i, j+1, visited, grid)
        