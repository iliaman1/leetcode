def searchInsert(nums: list[int], target: int) -> int:
        if nums[0] >= target:
            return 0

        if nums[-1] < target:
            return len(nums)

        if nums[-1] == target:
            return len(nums)-1

        for i in range(len(nums) - 1):
            if nums[i] < target and nums[i + 1] >= target:
                return i+1


# class Solution(object):
#     def searchInsert(self, nums, target):
#         nums.sort()
#         if target in nums:
# 	        return ((nums.index(target)))
#         else:
#             nums.append(target)
#             nums.sort()
#             return (nums.index(target))


# binary
# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         first=0
#         last=len(nums)-1
#         pf=0
#         pl=len(nums)-1
#         mid=(first+last)//2
#         while(first<=last):
#             mid=(first+last)//2
#             if(nums[mid]==target):
#                 return mid
#             elif(nums[mid]<target):
#                 pf=first
#                 first=mid+1
#             else:
#                 pl=last
#                 last=mid-1
#         mid=(pf+pl)//2
#         if(nums[mid]>target):
#             return mid
#         else:
#             return mid+1
