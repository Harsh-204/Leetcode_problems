class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        vector<int> ones;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '1') {
                ones.push_back(i);
            }
        }
        
        if (ones.size() < k) return "";
        
        string result = "";
        
        for (int i = 0; i <= ones.size() - k; ++i) {
            int start = ones[i];
            int end = ones[i + k - 1];
            string candidate = s.substr(start, end - start + 1);
            
            if (result.empty() || 
                candidate.length() < result.length() || 
                (candidate.length() == result.length() && candidate < result)) {
                result = candidate;
            }
        }
        
        return result;
    }
};