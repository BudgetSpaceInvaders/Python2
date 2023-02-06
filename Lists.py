#Task 1
"""
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order."""

target = input("Enter a number: ")
lenum = int(input("How many numbers do you want to check if they add to the number " + target + " --> "))
nums = []
falsen = 0
target = int(target)
while lenum > 0:
    falsen = int(input("Please enter a number: "))
    nums.append(falsen)
    lenum -= 1
print(nums)
for x in range(0, len(nums)):
    z = target - nums[x]
    if z in nums and x != nums.index(z):
        print(x)
        print(nums.index(z))
        break
