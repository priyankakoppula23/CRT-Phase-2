def performSelectionSort(nums):
    n = len(nums)
    fixThisIndex = n-1
    while fixThisIndex >0:
        maxIndex = fixThisIndex

        for index in range(fixThisIndex):
            if nums[index]>nums[maxIndex]:
                maxIndex = index
            
        if maxIndex!=fixThisIndex:
            temp=nums[maxIndex]
            nums[maxIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp
        print(nums)
        fixThisIndex-=1
nums = list(map(int,input("enter list:").split()))
print("Before sorting:",nums)
performSelectionSort(nums)
print("After sorting:",nums)