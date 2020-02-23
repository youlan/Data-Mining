
nums = [3,4,5,1,2]
l = 0
r = len(nums ) -1

while l <r:
    mid = int(l + (r - l) / 2)

    if nums[l] > nums[mid] and nums[r] > nums[mid]:
        print(nums[mid])
        break
    elif nums[l] > nums[mid] and nums[mid] > nums[r]:
        l = mid - 1
    elif nums[l] < nums[mid] and nums[mid] < nums[r]:
        r = mid
    elif nums[l] < nums[mid] and nums[mid] > nums[r]:
        l = mid