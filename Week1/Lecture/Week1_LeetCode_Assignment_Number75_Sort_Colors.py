#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
LeetCode practice
problem: 75. Sort Colors
"""

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

"""
Pseudo-codes: version 1. Brute-force bubble sort

isSwapped = True

while(isSwapped):
    for i from 1 to len(nums) do:
        isSwapped = False

        if nums[i]>nums[i+1] then:
            swap(nums[i], nums[i+1])
            isSwapped = True
"""

"""
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        isSwapped = True
        while (isSwapped):
            isSwapped = False
            for i in range(0, len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    isSwapped = True


# In[4]:


# Create an instance of Solution
solver = Solution()

nums = [2,0,2,1,1,0]

solver.sortColors(nums)
print(nums) #output [0, 0, 1, 1, 2, 2]


# In[5]:


# Create an instance of Solution
solver = Solution()

nums = [2,0,1]

solver.sortColors(nums)
print(nums) #output [0, 1, 2]


# In[ ]:




