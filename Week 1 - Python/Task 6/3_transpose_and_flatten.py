# -*- coding: utf-8 -*-
"""3. Transpose and Flatten.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

import numpy

x, y = map(int, input().split())

output = numpy.array([input().strip().split() for _ in range(x)], int)
print (output.transpose())
print (output.flatten())