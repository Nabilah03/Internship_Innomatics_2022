# -*- coding: utf-8 -*-
"""12. Dot and Cross.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

import numpy

x = int(input())
m = numpy.array([input().split() for _ in range(x)], int)
n = numpy.array([input().split() for _ in range(x)], int)
print(numpy.dot(m, n))