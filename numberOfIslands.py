# https://leetcode.com/problems/number-of-islands/submissions/

# Solution 1

# Depth first search

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedX = {}
        numIslands = 0

        def findWholeIsland(grid, visited, x, y):
            if ((x in visited) and (y in visited[x])) or y not in range(len(grid)) or x not in range(len(grid[y])) or grid[y][x] == '0':
                return
            else:
                if x not in visitedX:
                    visitedX[x] = {y}
                else:
                    visitedX[x].add(y)

                findWholeIsland(grid, visited, x+1, y)
                findWholeIsland(grid, visited, x-1, y)
                findWholeIsland(grid, visited, x, y+1)
                findWholeIsland(grid, visited, x, y-1)

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if x in visitedX and y in visitedX[x]:
                    continue

                if grid[y][x] == '1' and ((x not in visitedX) or (y not in visitedX[x])):
                    numIslands += 1
                    findWholeIsland(grid, visitedX, x, y)

                if x not in visitedX:
                    visitedX[x] = {y}
                else:
                    visitedX[x].add(y)
        return numIslands
