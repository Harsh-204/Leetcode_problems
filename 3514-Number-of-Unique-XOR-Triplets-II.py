class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Step 1: Remove duplicates to minimize unnecessary operations
        unique_nums = set(nums)
        
        # Step 2: Initialize our set of results with 0
        current_xors = {0}
        
        # Step 3: Expand 3 times to simulate picking 3 elements
        for _ in range(3):
            # Use set comprehension for highly optimized C-level iteration in Python
            current_xors = {x ^ y for x in current_xors for y in unique_nums}
            
        # Step 4: The size of the set is the number of unique XOR triplets
        return len(current_xors)