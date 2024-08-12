def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

#Test cases 
assert twoSum([2,7,11,15], 9) == [0, 1], 'Test 1 Failed'
assert twoSum([3, 2, 4], 6) == [1, 2], 'Test 2 Failed'
assert twoSum([3, 3], 6) == [0, 1], 'Test 3 Failed'

print('All testcases passed')
