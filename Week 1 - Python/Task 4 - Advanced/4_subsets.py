# -*- coding: utf-8 -*-
"""4. Subsets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for i in nums:
            new_subs = []
            for sub in output:
                new_subs.append(sub+[i])
            output.extend(new_subs)
        return output