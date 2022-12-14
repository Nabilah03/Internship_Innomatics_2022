# -*- coding: utf-8 -*-
"""9. Least Square Regression Line.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

math, stat = [],[]

for i in range(5):
    x, y= map(int,input().split())
    math.append(x)
    stat.append(y)

def value1(a,b):
    n = len(a)
    ab =[a[i]*b[i] for i in range(n) ]
    a_square = [i**2 for i in a]
    # y_square = [i**2 for i in y]
    
    total = (n*(sum(ab))-((sum(a)*sum(b))))/float(((n*sum(a_square))-sum(a)**2))
    return total
    
def value2(a,b):
    a_mean = sum(a)/float(len(a))    
    b_mean = sum(b)/float(len(b))
    res = value1(a,b)
    res1 = b_mean - res*a_mean
    return res1,res
    
x,y = value2(math,stat)
print(x + y*80)