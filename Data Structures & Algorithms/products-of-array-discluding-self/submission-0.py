class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            nums1=1
            for j in range(len(nums)):
                if i==j:
                    pass
                else:
                    nums1*=nums[j]
            list1.append(nums1)
        return list1