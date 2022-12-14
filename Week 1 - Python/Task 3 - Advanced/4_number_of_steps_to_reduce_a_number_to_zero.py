# -*- coding: utf-8 -*-
"""4. Number of Steps to Reduce a Number to Zero.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num > 0:
            if num % 2: num -= 1
            else: num /= 2
            result += 1
        return result