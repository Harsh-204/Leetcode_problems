from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Get coordinates of all 1s in img1 and img2
        p1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        p2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count frequencies of displacement vectors
        count = Counter((r1 - r2, c1 - c2) for r1, c1 in p1 for r2, c2 in p2)
        
        # Return max overlap frequency (or 0 if no 1s match)
        return max(count.values(), default=0)