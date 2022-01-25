# Remove Duplicates from Sorted Array
# ------------------------------------------------------------------------------


class Solution:
    def removeDuplicates(nums):
        newNum = []
        for n in range(1, len(nums)):
            if nums[n] not in newNum:
                newNum.append(nums[n])
        return newNum
    print(removeDuplicates([10,10,20,30,40,40,50,60,70,60,60,60,80,50]))


def removeDuplicates(nums):

    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l+=1
    return l
print(removeDuplicates([1,1,2,3,4,4,5,6,7,8,5]))

class Solution:
    def removeDuplicates(nums):
        list_len = len(nums)
        while list_len > 1:
            list_len -= 1
            if nums[list_len] == nums[list_len-1]:
                del nums[list_len]
        return len(nums)
    print(removeDuplicates([1,1,2,3,4,4,5,6,7,8]))
