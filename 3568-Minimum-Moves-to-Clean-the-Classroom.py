from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r = start_c = -1
        litter_coords = []
        
        # Parse grid for start position and litter locations
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start_r, start_c = r, c
                elif ch == 'L':
                    litter_coords.append((r, c))
        
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        num_litter = len(litter_coords)
        target_mask = (1 << num_litter) - 1
        
        # Check if start cell is already on litter (edge case)
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        if initial_mask == target_mask:
            return 0
        
        # best_energy[r][c][mask] stores maximum remaining energy reached for state (r, c, mask)
        best_energy = {}
        
        queue = deque([(start_r, start_c, initial_mask, energy, 0)])
        best_energy[(start_r, start_c, initial_mask)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, rem_energy, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
            
            if rem_energy == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    next_mask = mask
                    next_energy = rem_energy - 1
                    
                    # Update bitmask if we hit a litter cell
                    if cell == 'L':
                        litter_idx = litter_map[(nr, nc)]
                        next_mask |= (1 << litter_idx)
                    
                    # Reset energy if we hit a reset cell
                    if cell == 'R':
                        next_energy = energy
                    
                    if next_mask == target_mask:
                        return steps + 1
                    
                    # Push to queue only if we found a path with higher remaining energy
                    state_key = (nr, nc, next_mask)
                    if next_energy > best_energy.get(state_key, -1):
                        best_energy[state_key] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))
                        
        return -1