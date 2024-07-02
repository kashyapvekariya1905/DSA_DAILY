class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        rst = []
        for i in nums2:
            if count[i]>0:
                rst.append(i)
                count[i] -= 1
        return rst
