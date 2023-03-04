# Implement quicksort
# Has a worst case O(n) and is not stable becasue it will swap integers of the same value


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        e = len(nums) - 1

        self.quicksort(nums, s, e) # 1st recursive call

    def quicksort(self, nums, s, e):
        """
        Helper function to sort left and right of pivot element recursively
        """
        if (e-s+1)<=1: return nums # base case

        piv = nums[e]
        p = s
        #partition elements smaller than pivot to the leftmost side and vice versa
        for i in range(s, e):
            if (nums[i] <= piv):
               nums[p], nums[i] = nums[i], nums[p]
               left+=1

        #move pivot in between and left and right side and move current element pointed
        nums[e] = nums[p]
        nums[p] = piv

        #recursive calls on left and right side
        self.quicksort(nums, s, left-1)
        self.quicksort(nums, left+1, e)

    