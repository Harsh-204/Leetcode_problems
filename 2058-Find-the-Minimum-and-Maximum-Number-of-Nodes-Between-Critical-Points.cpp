class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        // A critical point requires a prev and next node, 
        // so lists with fewer than 3 nodes cannot have 2 critical points.
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        }

        ListNode* prev = head;
        ListNode* curr = head->next;
        ListNode* next = curr->next;

        int first_idx = -1;
        int prev_idx = -1;
        int min_dist = INT_MAX;
        int index = 2; // curr is the 2nd node (1-based index)

        while (next != nullptr) {
            // Check if curr is a local maxima or minima
            if ((curr->val > prev->val && curr->val > next->val) ||
                (curr->val < prev->val && curr->val < next->val)) {
                
                if (first_idx == -1) {
                    first_idx = index;
                } else {
                    min_dist = min(min_dist, index - prev_idx);
                }
                prev_idx = index;
            }

            // Move pointers forward
            prev = curr;
            curr = next;
            next = next->next;
            index++;
        }

        // Return [-1, -1] if fewer than 2 critical points exist
        if (first_idx == -1 || prev_idx == first_idx) {
            return {-1, -1};
        }

        return {min_dist, prev_idx - first_idx};
    }
};