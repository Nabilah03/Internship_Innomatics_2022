# -*- coding: utf-8 -*-
"""2. Find the Runner-Up Score.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])