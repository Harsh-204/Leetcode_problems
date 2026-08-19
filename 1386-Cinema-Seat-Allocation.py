import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Dictionary to store the reserved seats for each row (only caring about seats 2-9)
        reserved_map = collections.defaultdict(set)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_map[row].add(seat)
        
        # Max families for completely untouched rows
        max_families = (n - len(reserved_map)) * 2
        
        # Check rows with at least one reservation in columns 2-9
        for row, seats in reserved_map.items():
            left_free = not bool(seats & {2, 3, 4, 5})
            right_free = not bool(seats & {6, 7, 8, 9})
            middle_free = not bool(seats & {4, 5, 6, 7})
            
            if left_free and right_free:
                max_families += 2
            elif left_free or right_free or middle_free:
                max_families += 1
                
        return max_families