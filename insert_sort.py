#Given an array of integers nums, sort the array in ascending order and return it.
# Use Insert Sort with O(n**2)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # INSERTION SORT - O(n**2)
        # start loop at index 1 becasue the second pointer will be one step behind
        for i in range(len(nums)):
            # initialize a pointer one step behind the main loop pointer
            j = i-1
            # create a condition (if the next element) to rearrange elements and a stopping condition
            while (j>=0 and nums[j+1]<nums[j]):
                tmp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tmp
                j -= 1

        return nums