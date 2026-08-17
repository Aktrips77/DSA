class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def is_prime(x):
            if x<2:
                return False
            i=2
            while i*i<=x:
                if x%i==0:
                    return False
                i+=1
            return True
        prime_cache={}
        non_prime_cache={}
        def costprime(x):
            if x in prime_cache:
                return prime_cache[x]
            og=x
            cost=0
            while not is_prime(x):
                x+=1
                cost+=1
            prime_cache[og]=cost
            return cost
        def costnonp(x):
            if x in non_prime_cache:
                return non_prime_cache[x]
            og=x
            cost=0
            while is_prime(x):
                x+=1
                cost+=1
            non_prime_cache[og]=cost
            return cost
        ans=0
        
        for i , num in enumerate(nums):
            if i%2==0:
                ans+=costprime(num)
            else:
                ans+=costnonp(num)
        return ans

        
        