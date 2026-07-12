class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1 & 2: Get unique elements and sort them
        unique_sorted_elements = sorted(set(arr))
        
        # Step 3: Create a mapping of the element to its rank (1-indexed)
        rank_map = {val: index + 1 for index, val in enumerate(unique_sorted_elements)}
        
        # Step 4: Map the original array to their respective ranks
        return [rank_map[num] for num in arr]