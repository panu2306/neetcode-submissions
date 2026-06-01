class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums1):
            for j in range(len(nums2)):
                if(num == nums2[j]):
                    k = j
                    while(k < len(nums2)-1):
                        if(nums2[k] > num):
                            res.append(nums2[k])
                            break
                        k += 1
                    if(k == len(nums2)-1):
                        if(nums2[k] > num):
                            res.append(nums2[k])
                        else: 
                            res.append(-1)
                    
        return res

        