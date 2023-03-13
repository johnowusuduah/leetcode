#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in 
#nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # example
        # nums = [2,3,4,6,7]
        l, r = 0, len(nums)-1

        # what is this while loop for?
        while l <= r: 
            mid = (l+r)//2
        
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid -1
            else:
                return mid

        return -1