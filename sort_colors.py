#SORT COLORS

#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors 
#in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #essentially sort arrays with a fixed range of 0 to 1
        counter = [0]*3 # initialize counter array to store the no. of times each color appears

        # populate counter bucket
        for num in nums: # loop through nums with elements
            counter[num] += 1 # count the no. of elements using values as indices in counter

        # sort inplace from counter bucket
        i = 0 # pointer to place sorted elements in array inplace
        for n in range(len(counter)): # n is an index but it also the corresponding val of the counter
            for _ in range(counter[n]):
                nums[i] = n
                i += 1