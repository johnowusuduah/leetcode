#Koko Eating Bananas

#Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come 
#back in h hours.
#Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that 
#pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#Return the minimum integer k such that she can eat all the bananas within h hours.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)    
        result = r 

        while l <= r:
            #find the middle index of the array
            k = (l + r) // 2
            hours = 0 # stores how many hours it will take with selected k value
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h: # if koko can eat all the bananas in less than h hours find a lower k value
                result = min(result, k) # save k value that achieves hours that is less than h
                r = k - 1 # search to the left of k
            else:# if koko cannot eat all the bananas in less than h hours
                l = k + 1 # search to the right of k
            
        return result