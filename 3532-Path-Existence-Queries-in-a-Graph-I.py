class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # component_id[i] will store the ID of the component that node i belongs to
        component_id = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            # If the gap between adjacent elements is larger than maxDiff,
            # it starts a new connected component.
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            component_id[i] = curr_id
            
        # For each query, a path exists if both nodes share the same component ID
        return [component_id[u] == component_id[v] for u, v in queries]