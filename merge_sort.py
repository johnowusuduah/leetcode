#Given an array of integers nums, sort the array in ascending order and return it.
#You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # MERGE SORT - O(nlogn))
        if len(nums)>1:
            # DIVIDE
            # divide array right down the middle to left and right
            L = nums[:len(nums)//2]
            R = nums[len(nums)//2:]
            # divide left and right recursively until one element remains in subarrays
            self.sortArray(L)
            self.sortArray(R)
            # MERGE
            # at this point all subarrays have a singular element
            # initialize pointers to parent subarray, left child subarray and right child subarray
            # remember that parent subarray is nums
            k, i, j = 0, 0, 0
            while (i < len(L) and j < len(R)):
                if R[j] < L[i]:
                    nums[k] = R[j]
                    #k += 1
                    j += 1
                else:
                    nums[k] = L[i]
                    #k += 1
                    i += 1
                k += 1 # in both if statements in the while loop we will be 

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = L[j]
                j += 1
                k += 1

        return nums