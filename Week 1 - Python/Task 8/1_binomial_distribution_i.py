# -*- coding: utf-8 -*-
"""1.  Binomial Distribution I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

import math
ratio = list(map(float, input().split()))
total = 6 
x = [3,4,5,6] 
m = ratio[0]/(ratio[0]+ratio[1]) 
n = ratio[1]/(ratio[0]+ratio[1]) 
prob = 0
for i in x: 
    prob1 = (math.factorial(total)/(math.factorial(i)*math.factorial(total-i))) * m**i * n**(total-i) 
    prob += prob1 
    prob = round(prob, 3)
print(prob)