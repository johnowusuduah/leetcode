#1. Two Sum

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # strategy is to use a hashmap to store every element of the array and its index
        # while doing so, find the difference between the target tand the current element
        # if the difference is in the hashmap, return the index of the difference and the current
        # index, we can see that the enumerate method will help us here

        hmap= {} # element : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i]
            hmap[n] = i
        return 