class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # If the minimum element is odd, we can always make all elements odd or all elements even.
        if min_val % 2 != 0:
            return True
        
        # If the minimum element is even, all elements must already share the same parity.
        has_even = any(x % 2 == 0 for x in nums1)
        has_odd = any(x % 2 != 0 for x in nums1)
        
        return not (has_even and has_odd)