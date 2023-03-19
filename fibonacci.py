#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
#such that each number is the sum of the two preceding ones, 
#starting from 0 and 1. That is,

#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.
#Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        #iterative approach
        # a,b = 0,1
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     for i in range(2,n+1):
        #         a,b = b,a+b
        #     return b

        # recursive approach
        # if n <= 1:
        #     return n
        # return self.fib(n-2) + self.fib(n-1)

        # dynamic programming approach
        if n < 2: return n

        dp = [0,1]
        i = 2
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1
        return dp[1]