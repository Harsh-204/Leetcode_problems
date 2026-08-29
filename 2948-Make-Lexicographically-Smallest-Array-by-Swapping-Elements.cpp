#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();
        
        // Store value and original index pairs
        vector<pair<int, int>> sorted_nums(n);
        for (int i = 0; i < n; ++i) {
            sorted_nums[i] = {nums[i], i};
        }
        
        // Sort pairs by value
        sort(sorted_nums.begin(), sorted_nums.end());
        
        vector<int> result(n);
        int i = 0;
        
        while (i < n) {
            int j = i;
            // Group elements that differ by <= limit
            while (j + 1 < n && sorted_nums[j + 1].first - sorted_nums[j].first <= limit) {
                j++;
            }
            
            // Extract the original indices for this component
            vector<int> indices;
            for (int k = i; k <= j; ++k) {
                indices.push_back(sorted_nums[k].second);
            }
            
            // Sort indices so smaller values go to smaller indices
            sort(indices.begin(), indices.end());
            
            // Place sorted values into sorted indices
            for (int k = i; k <= j; ++k) {
                result[indices[k - i]] = sorted_nums[k].first;
            }
            
            i = j + 1;
        }
        
        return result;
    }
};