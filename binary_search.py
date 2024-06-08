#binary search
nums=[12,34,10,23,45,38]
target = 34
nums = sorted(nums)
print(nums)

left = 0
right=len(nums)-1
flag= -1

while left <= right:
    mid = (left + right)//2
    if nums[mid] == target:
        flag = mid
        break
    elif nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
if flag == -1:
    print("Not found")
else:
    print("Target found at:",flag)