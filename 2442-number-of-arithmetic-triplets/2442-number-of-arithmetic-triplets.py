class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        """
        You are given a 0-indexed, strictly increasing integer array nums 
        and a positive integer diff.
        A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

        i < j < k,
        nums[j] - nums[i] == diff, and
        nums[k] - nums[j] == diff.
        Return the number of unique arithmetic triplets.
        """

        '''
        steps
        1. check if nums >= to three if true proceed if false return 0
        2. the distance between the num's at this sorted indices must meet this
        3. create a scope to check for the eligibility of this three condtions
        4. if false continue to the next iteration ie increase i and j and k.
         - we must check the differnce between nums[j] - nums[i] and if it's small we increment j, 
         - three pointers while checking the difference btwn the numbers this works becuase the numbers are sorted
         - if the window is smaller that diff move the right pointer,
         - if it's equal proceed to find out if it captures all the condtions
         - 
        5. if true increment the counter of the unique arithmetic triplets.
        [0,1,4,6,7,10] diff = 3
        0 < 1 < 2,
        nums[1] - nums[0] == 3 false difference = 1 j += 1 and k += 1 :if j == k, and
        nums[k] - nums[j] == diff.
        '''
        n = len(nums)

        if n < 3:
            return 0

        left, middle, right = 0, 1, 2 # indices of this three pointers
        self.count = 0
        
        def helper(left, middle, right):
            if nums[right] - nums[middle] < diff:
                return left, middle, right + 1
            elif nums[right] - nums[middle] == diff:
                return helper2(left, middle, right)
            else: # nums[right] - nums[middle] > diff
                return left, middle + 1, right

        # self.helper2 = helper2
        
        def helper2(left, middle, right):
            if nums[middle] - nums[left] > diff:
                return left + 1, middle, right
            elif nums[middle] - nums[left] == diff:
                self.count += 1
                # Move right to look for overlapping triplets
                return left, middle + 1, right
            else: # nums[middle] - nums[left] < diff
                return left, middle + 1, right

        while right < n:
            
            left, middle, right = helper(left, middle, right)

            # Ensure correct ordering: left < middle < right
            if middle <= left:
                middle = left + 1
            if right <= middle:
                right = middle + 1
        
        return self.count
                    