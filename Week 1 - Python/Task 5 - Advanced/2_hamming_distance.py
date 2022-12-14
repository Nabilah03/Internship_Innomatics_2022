# -*- coding: utf-8 -*-
"""1. Hamming Distance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        output, cal = x^y, 0
        while output>0:
            cal += output & 1
            output >>= 1
        return cal