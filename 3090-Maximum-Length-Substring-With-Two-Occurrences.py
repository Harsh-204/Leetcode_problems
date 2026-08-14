class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            
            # If any character count exceeds 2, shrink the window from the left
            while counts[char] > 2:
                counts[s[left]] -= 1
                left += 1
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len