from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        counts = Counter(word)
        
        # Sort the frequencies in descending order
        freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        
        # Calculate the minimum pushes
        for i, freq in enumerate(freqs):
            # The multiplier increases every 8 characters
            # i = 0-7 -> cost = 1
            # i = 8-15 -> cost = 2, etc.
            multiplier = (i // 8) + 1
            total_pushes += freq * multiplier
            
        return total_pushes