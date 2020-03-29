
// First and last position of X in sorted array

#include <vector>

class Solution {
    int first_pos(std::vector<int>& a, int x) {
        int n = a.size();
        int first_pos = n; // first >= x
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (a[mid] >= x) {
                first_pos = mid;
                high = mid -1;
            }
            else {
                low = mid + 1;
            }
        }
        return first_pos;
    }

public:
    std::vector<int> searchRange(std::vector<int>& a, int x) {
        // lower_bound(a.begin(), a.end(), x);
        int first = first_pos(a, x); // the lower boundary
        int last = first_pos(a, x + 1) - 1;  // the large boundary
        if (first <= last) {
            return {first, last};
        }
        return {-1, -1};
    }
};