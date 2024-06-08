def performBubbleSort(nums):
    n = len(nums)
    fixThisIndex = n-1

    while fixThisIndex >0:
        for index in range(fixThisIndex):
            if nums[index] > nums[index + 1]:
                temp = nums[index]
                nums[index] = nums[index + 1]
                nums[index + 1] = temp
        print(nums)
        fixThisIndex-=1
# nums = [10,8,20,14,12,7]
nums = list(map(int,input("enter list:").split()))
print("Before sorting:",nums)
performBubbleSort(nums)
print("After sorting:",nums)