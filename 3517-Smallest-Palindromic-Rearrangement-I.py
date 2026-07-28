from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Count the frequency of each character
        counts = Counter(s)
        
        first_half = []
        middle_char = ""
        
        # Iterate through characters in alphabetical order
        for char in sorted(counts.keys()):
            # If the count is odd, this character will be in the middle
            if counts[char] % 2 != 0:
                middle_char = char
            
            # Add half of the character's occurrences to the first half
            first_half.append(char * (counts[char] // 2))
            
        first_half_str = "".join(first_half)
        
        # Combine the first half, the middle character (if any), and the reversed first half
        return first_half_str + middle_char + first_half_str[::-1]