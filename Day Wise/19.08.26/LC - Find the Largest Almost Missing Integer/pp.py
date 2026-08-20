nums = [3,9,2,1,7]
k = 3

subarray = []
largest = 0
dict1 = {}



for i in range(len(nums) - k + 1):
    subarray.append(nums[i:i+k])

if k == 1:
    print(max(nums))
if k == len(nums):
    print(max(nums))
for num in nums:
    if num not in dict1:
        dict1[num] = 0
    for i in subarray:
        if num in i:
            dict1[num] += 1

for i in dict1:
    if dict1[i] == 1:
        largest = max(largest, i)

print(largest)