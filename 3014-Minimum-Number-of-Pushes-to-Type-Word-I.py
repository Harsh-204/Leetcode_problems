class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        
        for i in range(n):
            # i // 8 determines which "level" or "position" on the key we are at.
            # Adding 1 converts 0-indexed levels to 1-based push counts.
            total_pushes += (i // 8) + 1
            
        return total_pushes