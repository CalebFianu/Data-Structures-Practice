def two_sum(nums, target):
    seen = set()
    for i in nums:
        compliment = target - i
        if compliment in seen:
            return True
        else:
            seen.add(i)
    return False

nums = [1,3,4,5,2,4]
target = 20
print(two_sum(nums, target))