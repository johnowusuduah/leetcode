#You are given an m x n integer matrix matrix with the following two properties:

#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.

#You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # apply binary search to the last element in each subarray to find
        # the subarray that has the range of values that have the target
        ROWS, COLS = len(matrix), len(matrix[0])

        # use ROW to loop through subarrays to select the subarrays with range 
        # of values of the target
        top, bot = 0, ROWS - 1
        while top <= bot:
            midrow = (top + bot) // 2
            if target > matrix[midrow][-1]:
                top = midrow + 1
            elif target < matrix[midrow][-1]:
                bot = midrow - 1
            else:
                break # break when we find midrow

            if not (top <= bot): # if none of the rows are in the range of the target
                return False

            row = (top + bot) // 2
            l, r = 0, COLS - 1
            while l <= r:
                m = (l + r)//2
                if target > matrix[row][m]:
                    l = m + 1
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    return True

            return False
