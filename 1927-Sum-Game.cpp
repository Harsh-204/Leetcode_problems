class Solution {
public:
    bool sumGame(string num) {
        int n = num.length();
        double sum_diff = 0;
        int q_diff = 0;

        for (int i = 0; i < n / 2; ++i) {
            if (num[i] == '?') q_diff++;
            else sum_diff += num[i] - '0';
        }

        for (int i = n / 2; i < n; ++i) {
            if (num[i] == '?') q_diff--;
            else sum_diff -= num[i] - '0';
        }

        // Bob wins if and only if the difference can be neutralized
        return sum_diff + (q_diff / 2.0) * 9 != 0;
    }
};