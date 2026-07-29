import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Calculate available counts for the first half of the palindrome
        half_counts = {c: count // 2 for c, count in counts.items()}
        
        # Identify the middle character if the string length is odd
        mid_char = ""
        for c, count in counts.items():
            if count % 2 != 0:
                mid_char = c
                break
                
        half_len = n // 2
        
        # Calculate the initial total permutations for the half string
        total_perms = math.factorial(half_len)
        for count in half_counts.values():
            total_perms //= math.factorial(count)
            
        # If k is strictly greater than all unique permutations, return empty string
        if k > total_perms:
            return ""
            
        current_ways = total_perms
        remaining_len = half_len
        half_res = []
        
        # Build the first half of the string character by character
        for _ in range(half_len):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if half_counts.get(c, 0) > 0:
                    # Calculate permutations if we choose character `c` for this position
                    # W' = W * C_c / L
                    ways_if_c = current_ways * half_counts[c] // remaining_len
                    
                    if k <= ways_if_c:
                        # The k-th permutation falls under this character branch
                        half_res.append(c)
                        half_counts[c] -= 1
                        current_ways = ways_if_c
                        remaining_len -= 1
                        break
                    else:
                        # Skip this branch and shrink k
                        k -= ways_if_c
                        
        # Construct the final palindromic string
        first_half = "".join(half_res)
        return first_half + mid_char + first_half[::-1]