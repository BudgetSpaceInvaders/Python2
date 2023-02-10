"""
#Task 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

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


#Task 2
lennum = int(input("How many variables will be in your list --> "))
list123 = []
while lennum > 0:
    fallsen = int(input("Please enter a number: "))
    list123.append(fallsen)
    lennum -= 1
for x in range(0, lennum-1):
    if list123[x] < 0 and list123[x+1] < 0:
        print(list123[x], list123[x+1])
    if list123[x] > 0 and list123[x + 1] > 0:
        print(list123[x], list123[x + 1])

#Task 3
lenlist10 = int(input("How many variables will be in your list --> "))
list10 = []
for x in range(0, lenlist10):
    apple = int(input("Please enter a number: "))
    list10.append(apple)
    lenlist10 -= 1
curnum = ""
list11 = []
for x in range(0, len(list10)-1):
    if list10[x] < list10[x+1]:
        list11.append(list10[x+1])
print(list11)"""


#Task 4
lenlist12 = int(input("How many variables will be in your list --> "))
list12 = []
for x in range(0, lenlist12):
    banana = int(input("Please enter a number: "))
    list12.append(banana)
    lenlist12 -= 1
list12.sort()
list12 = set(list12)
print(list12)
print(len(list12))
