#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = target.size();
        vector<int> cnt(26, 0);
        
        // Net balance: available from s minus required by target
        for (char c : s) cnt[c - 'a']++;
        for (char c : target) cnt[c - 'a']--;

        // Iterate right-to-left to find the rightmost pivot position
        for (int i = n - 1; i >= 0; i--) {
            // Reclaim the character used at target[i]
            cnt[target[i] - 'a']++;

            // Check if the prefix s[0...i-1] is valid (no character count is negative)
            bool can_match_prefix = true;
            for (int k = 0; k < 26; k++) {
                if (cnt[k] < 0) {
                    can_match_prefix = false;
                    break;
                }
            }

            if (!can_match_prefix) continue;

            // Find the smallest character > target[i] available in pool
            for (int j = target[i] - 'a' + 1; j < 26; j++) {
                if (cnt[j] > 0) {
                    // Place 'a' + j at target[i]
                    cnt[j]--;

                    // Build the result prefix: target[0...i-1] + ('a' + j)
                    string res = target.substr(0, i);
                    res.push_back('a' + j);

                    // Append all remaining available characters in ascending order
                    for (int k = 0; k < 26; k++) {
                        while (cnt[k] > 0) {
                            res.push_back('a' + k);
                            cnt[k]--;
                        }
                    }
                    return res;
                }
            }
        }

        return "";
    }
};