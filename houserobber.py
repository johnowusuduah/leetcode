# HOUSE ROBBER
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
#the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
#it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can 
#rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0 #the last two max amt we can rob

        #now are max array looks like this
        #[rob1, rob2, n, n + 1, ...]

        for n in nums:
            tmp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = tmp
        #at the end of the for loop, rob2 will be at the last location and will have 
        #the maximum amount we can rob
        return rob2