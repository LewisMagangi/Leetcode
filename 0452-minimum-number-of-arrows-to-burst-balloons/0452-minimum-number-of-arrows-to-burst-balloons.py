class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key=lambda x: x[1])

        end = points[0][1]
        arrows = 1

        for x_start, x_end in points[1:]:
            if x_start > end:
                arrows += 1
                end = x_end

        return arrows

        