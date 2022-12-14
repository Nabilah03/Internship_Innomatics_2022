# -*- coding: utf-8 -*-
"""6. The Central Limit Theorem III.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
avg, sigma = 500, 80

avgS, sigmaS = avg, sigma/(100**0.5)

x = avg - (1.96*sigmaS)
y = avg + (1.96*sigmaS)

print(round(x,2))
print(round(y,2))