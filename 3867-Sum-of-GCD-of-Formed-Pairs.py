import math
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd = []
        mx = 0
        
        # Step 1: Construct prefixGcd
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(math.gcd(num, mx))
            
        # Step 2: Sort the array
        prefixGcd.sort()
        
        # Step 3: Form pairs and compute the sum of their GCDs
        left = 0
        right = len(prefixGcd) - 1
        total_sum = 0
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum