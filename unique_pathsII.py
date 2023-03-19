#UNIQUE PATHS II
#You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
#The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right 
#at any point in time.
#An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that 
#is an obstacle.

#Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#The testcases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        curRow = [0] * cols
        curRow[cols-1] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c]:
                    curRow[c] = 0
                elif c + 1 < cols: #run this block when we are not out of bounds
                    curRow[c] = curRow[c] + curRow[c+1] #c+1 = N we go out of bounds and we add 0 as shown below
                #else:
                #    curRow[c] = curRow[c] + 0 #this is just an assignment so we can comment it out

        return curRow[0]