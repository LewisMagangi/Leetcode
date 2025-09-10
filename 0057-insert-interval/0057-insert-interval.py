class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        """
        Pseudo Code
        1. Iterate through the list
        2. Add all intervals ending before newInterval starts.
        3. Merge overlapping intervals with newInterval.
        4. Add the remaining intervals after newInterval
        """

        n = len(intervals)
        i = 0
        res = []

        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i]) 
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])

            i += 1
        
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1

        return res