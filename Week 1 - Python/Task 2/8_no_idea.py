# -*- coding: utf-8 -*-
"""8. No Idea.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

x, y = input().split()

arr = input().split()

X = set(input().split())
Y = set(input().split())
print(sum([(i in X) - (i in Y) for i in arr]))