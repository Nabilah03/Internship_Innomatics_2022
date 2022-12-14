# -*- coding: utf-8 -*-
"""3. Single Number III.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(xor, nums)
        y = x & (-x)
        result = reduce(xor, filter(lambda x: x & y, nums))
        return (result, x^result)