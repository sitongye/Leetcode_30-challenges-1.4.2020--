#2540. Minimum Common Value

# Explanation:
# Given two integer arrays nums1 and nums2, return the minimum common value that appears in both arrays.
# If there is no common value, return -1.

def findMinimumCommonValue(nums1, nums2):
    i, j = 0, 0
    min_common = float('inf')
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            min_common = min(min_common, nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return min_common if min_common != float('inf') else -1


class MySolution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1_idx = 0
        ptr2_idx = 0
        while ptr1_idx < len(nums1) and ptr2_idx < len(nums2):
            if nums1[ptr1_idx] == nums2[ptr2_idx]:
                return nums1[ptr1_idx]
            elif nums1[ptr1_idx] < nums2[ptr2_idx]:
                ptr1_idx += 1
            else:
                ptr2_idx += 1

        return -1

# Analysis:
# Time Complexity: O(n + m) where n is the length of nums1 and m is the length of nums2
# - We traverse both arrays once, making it linear in terms of the total number of elements.
# Space Complexity: O(1)
# - We use a constant amount of space for pointers and the minimum common value variable.
# - No additional data structures are used that scale with input size.
# Algorithm:
# 1. Initialize two pointers for each array.
# 2. Compare the elements at the pointers.
# 3. If they are equal, update the minimum common value and move both pointers.
# 4. If the element in nums1 is smaller, move the pointer in nums1.
# 5. If the element in nums2 is smaller, move the pointer in nums2.
# 6. Continue until one of the pointers reaches the end of its respective array.