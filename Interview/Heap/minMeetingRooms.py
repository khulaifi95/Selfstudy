class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        end_p = start_p = 0

        while start_p < len(intervals):
            if start[start_p] >= end[end_p]:
                used_rooms -= 1
                end_p += 1
            used_rooms += 1
            start_p += 1

        return used_rooms