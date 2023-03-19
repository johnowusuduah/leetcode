# UNIQUE PATHS
#There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot 
#tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # rows, cols = m, n
        # prevRow = [0]*cols #initialize row of zeros to indicate out of bounds

        #TWO ARRAY DP SOLUTION
        # for _ in range(rows): # initialize current as the last row with first loop and shift upwards
        #     curRow = [0]*cols #same size as previous row
        #     curRow[cols-1] = 1 #the last element of each row which is the same as the last column in

        #     #loop backwards starting from the penultimate element in each curRow and update values in curRow
        #     #we start from the penultimate element because we have already defined the last element as 1
        #     for c in range(cols-2, -1, -1):
        #         #each value of curRow is equal to the sum of the value to it's right and the value at the same
        #         #index of the prevRow or the row below it
        #         curRow[c] = curRow[c+1] + prevRow[c]
        #     prevRow = curRow
            
        # return prevRow[0]

        #INPLACE DP SOLUTION
        rows, cols = m, n
        curRow = [0] * cols

        for _ in range(rows):
            curRow[cols-1] = 1

            for c in range(cols-2, -1, -1):
                curRow[c] = curRow[c + 1] + curRow[c]

        return curRow[0]