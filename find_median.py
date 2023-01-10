import random


def find_median(nums):
    def partition(nums,target, l, r):
        k = random.randint(l, r)
        print(k, nums)
        nums[k], nums[r] = nums[r], nums[k]
        left = l - 1
        for right in range(l, r):
            if nums[right] < nums[r]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
        left += 1
        nums[left], nums[r] = nums[r], nums[left]
        print(nums,left)
        if target == left:
            return nums[target]
        elif left < target:
            return partition(nums, target, left, r)
        else:
            return partition(nums, target, l, left)



    n = len(nums)
    if n % 2 == 1:
        return partition(nums, n//2, 0, n-1)
    else:
        a = partition(nums, n//2, 0, n-1)
        b = partition(nums, n//2-1, 0, n-1)
        return (a + b) / 2



nums = [2, 5, 4, 9, 3, 6, 8, 7, 1]
#nums = [4,2,3,2,4]
res = find_median(nums)
print(res)
