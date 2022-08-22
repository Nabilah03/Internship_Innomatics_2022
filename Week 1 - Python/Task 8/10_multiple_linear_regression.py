# -*- coding: utf-8 -*-
"""10. Multiple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

from sklearn import linear_model

ip = list(map(int, str.split(input(), " ")))
x, y = ip[0], ip[1]

data = [list(float(x) for x in input().split()) for i in range(y)]

a = [[item[i] for i in range(x)] for item in data]
b = [item[-1] for item in data]

lm_model = linear_model.LinearRegression()
lm_model.fit(a, b)
m = lm_model.intercept_
n = lm_model.coef_

for i in range(int(input())):
    data = list(map(float, input().split()))
    res = [n[j]*data[j] for j in range(x)]
    print(m+sum(res))