from math import isqrt
from typing import List

class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:

        left, right = 0, min(ranks) * cars * cars

        while left < right:

            mid = (right + left) // 2

            repaired_cars = 0

            for rank in ranks:
                repaired_cars += isqrt(mid // rank)
            
            if repaired_cars >= cars:
                right = mid
            
            else:
                left = mid + 1
        
        return left