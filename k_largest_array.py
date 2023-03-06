#Given an integer array nums and an integer k, return the kth largest element in the array.
#Note that it is the kth largest element in the sorted order, not the kth distinct element.
#You must solve it in O(n) time complexity.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            """
            Helper function to partition array by pivot
            depending on the comparison of k and p
            """
            #initialize pointer used to place values less than pivot in array inplace and pivot
            p, pivot = l, nums[r] 
            for i in range(l, r):
                if nums[i] <= pivot: #if an element is less than the pivot, swap it with the next element
                    #place the element on the left of pivot inplace at the end of the loop p will be one step ahead
                    nums[p], nums[i] = nums[i], nums[p] 
                    p += 1 
            #point p to the pivot and and the last element of the array to be the element that p was pointing to
            nums[p], nums[r] = pivot, nums[p] 

            # remember indices less than p are to the left of p and vice versa
            # if the index we are searching for is on the left side of p
            # make sure not to include the partition element
            if k < p: return quickselect(l, p-1)
            elif k > p: return quickselect(p+1, r) 
            else: return nums[p]

        return quickselect(0, len(nums)-1)