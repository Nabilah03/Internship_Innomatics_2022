# -*- coding: utf-8 -*-
"""4. How Many Numbers Are Smaller Than the Current Number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        len_num=len(nums)
        arr=[]
        count=0
        for i in nums:
            for j in range(len_num):
               if (nums[j]-i)<0:
                   count+=1
            arr.append(count)
            count=0
        return arr