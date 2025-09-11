class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        enum = [(value, index) for index, value in enumerate(nums)]   # (value, original index)

        def mergesort(l, r):

            if l == r:
                return [enum[l]]
                
            mid = (l + r) // 2
            left = mergesort(l, mid)
            right = mergesort(mid + 1, r)
            return merge(left, right)

        def merge(left, right):
            arr = [None] * (len(left) + len(right))  # final merged array
            i = j = k = 0
           
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    res[left[i][1]] += j
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j] 
                    j += 1
                k += 1

            while i < len(left):
                res[left[i][1]] += j
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

            return arr

        mergesort(0, n - 1)
        return res # Working on this to make sure it renders the right list

            

            