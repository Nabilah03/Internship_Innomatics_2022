# -*- coding: utf-8 -*-
"""3. Number of Students Doing Homework at a Given Time.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result=0
        x=zip(startTime, endTime)
        for i, j in x:
            if i<=queryTime<=j:
                result+=1
        return result