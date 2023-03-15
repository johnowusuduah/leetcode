#Contains Duplicate

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countMap = set()

        for n in nums:
            if n in countMap: 
                return True
            countMap.add(n)

        return False