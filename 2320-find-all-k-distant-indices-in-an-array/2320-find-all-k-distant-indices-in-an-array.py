class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        '''
        steps
        1. Find the indices j where nums[j] == key, 

        fill the num_index hashmap and 
        find the indices of all appearance of something equal to the key.
        so the values are the list_of_indices and the keys are num's from the nums
        
        we'll be given the key, we'll use a hashmap 
        for constant lookup. Note if we just look up using the find or index funct,
        the lookup will be linear. 

        2. Take the j indices and find out if there are k distant

        3. fill j and i here |i - j| <= k note that we've been given k too.
        For the iteration note that we'll have to check for all indices of j in a single i index ie 
        check for at least one j that satisifies |i - j| <= k this expression. 
        proceed once found if not iterate through all j's until one is found
        . Once we find an index that makes the two condition true we'll 
        fill list of k indices with the index.
        
        4. We'll return the list of k indices it'll be sorted we'll be traversing the list
        from index 0.

        nums = [2,2,2,2,2]
        key = 2
        k = 2

        nums[j] == 2, it's all indices. [0, 1, 2, 3, 4]
        i = 0, j = 0, ki = []
        |0 - 0| <= 2 true  ki = [0]
        i = 1, j = 1, ki = [0]
        |1 - 1| <= 2 true ki = [0, 1]
        i = 2, j = 2, ki = [0, 1]
        |2 - 2| <= 2 true ki = [0, 1, 2]
        i = 3, j = 3, ki = [0, 1, 2]
        |3 - 3| <= 2 true  ki = [0, 1, 2, 3]
        i = 4, j = 4, ki = [0, 1, 2, 3]
        |4 - 4| <= 2 true  ki = [0, 1, 2, 3, 4] Right

        nums = [3,4,9,1,3,9,5], key = 9, k = 1  expression |i - j| <= k
        1. 2 and 5 so j indices are [2, 5]
        i = 0, j = [2, 5], ki = []
        |0 - 2| <= 1 false proceed to next iteration, ki = []
        i = 1, j = [2, 5], ki = []
        |1 - 2| <= 1 true, ki = [1]
        i = 2, j = [2, 5], ki = []
        |2 - 2| <= 1 true, ki = [1, 2]
        i = 3, j = [2, 5], ki = []
        |3 - 2| <= 1 true, ki = [1, 2, 3]
        i = 4, j = [2, 5], ki = []
        |4 - 2| <= 1 false, |4 - 5| <= 1 true, ki = [1, 2, 3, 4]
        i = 5, j = [2, 5], ki = []
        |5 - 2| <= 1 false, |5 - 5| <= 1 true, ki = [1, 2, 3, 4, 5]
        i = 6, j = [2, 5], ki = []
        |6 - 2| <= 1 false, |6 - 5| <= 1 true, ki = [1, 2, 3, 4, 5, 6]
        '''

        num_index = {}
        # j_indices = []
        k_distance_indices = []

        """
        for index, num in enumerate(nums):
            # No need for this check will fix later
            if num in num_index:
                num_index[num] += [index]
            else:
                num_index[num] += [index]
        """

        j_indices = [j for j in range(len(nums)) if nums[j] == key]

        """
        for ky, value in num_index:
            if ky == key:
                j_indices += value
        """

        for i in range(len(nums)):
            for j in j_indices:
                if abs(i - j) <= k:
                    k_distance_indices += [i]
                    i += 1
                    break

        return k_distance_indices
                
        