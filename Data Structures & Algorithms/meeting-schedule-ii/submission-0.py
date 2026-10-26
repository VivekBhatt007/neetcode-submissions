"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = {}
        for interval in intervals:
            mp[interval.start] = mp.get(interval.start, 0) + 1
            mp[interval.end] = mp.get(interval.end, 0) - 1
        
        curr_rooms = 0
        max_rooms = 0
        for i in sorted(mp.keys()):
            curr_rooms += mp[i]
            max_rooms = max(max_rooms, curr_rooms)
        return max_rooms