# -*- coding: utf-8 -*-
"""13. Set .intersection() Operation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

n = int(input())
input1 = set(input().split())

n2 = int(input())
input2 = set(input().split())

input3 = input2.intersection(input1)

print(len(input3))