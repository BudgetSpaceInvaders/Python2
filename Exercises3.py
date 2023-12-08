nums = [5, 8, 3, 3, 9, 1, 0, 5, 9, 5, 7, 2]

nums = sorted(nums)
"""
print(nums)


def rm_dupes(nums):
    nums_2 = []
    for_len = len(nums) - 1
    for x in range(for_len):
        if nums[x] != nums[x + 1]:
            nums_2.append(nums[x])
        elif x == for_len and nums[x] == nums[for_len]:
            nums_2.append(nums[x])
    return nums_2


print(rm_dupes(nums))"""

tuple1 = tuple(nums)
list1 = list(tuple1)

print(tuple1)
