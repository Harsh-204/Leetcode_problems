#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumDeletions(std::vector<int>& nums) {
        int n = nums.size();
        
        int minIdx = 0;
        int maxIdx = 0;
        for (int k = 0; k < n; ++k) {
            if (nums[k] < nums[minIdx]) minIdx = k;
            if (nums[k] > nums[maxIdx]) maxIdx = k;
        }
        
        int i = std::min(minIdx, maxIdx);
        int j = std::max(minIdx, maxIdx);
        
        int option1 = j + 1;               // Delete both from front
        int option2 = n - i;               // Delete both from back
        int option3 = (i + 1) + (n - j);   // Delete one from front, one from back
        
        return std::min({option1, option2, option3});
    }
};