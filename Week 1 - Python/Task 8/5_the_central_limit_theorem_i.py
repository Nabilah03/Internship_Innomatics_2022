# -*- coding: utf-8 -*-
"""5. The Central Limit Theorem I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

import math

ip = int(input())
ip1 = int(input())
ip2 = int(input())
sgm = int(input())

ip2_sum = ip1 * ip2 
sgm_sum = math.sqrt(ip1) * sgm

def norm(ip, ip2, sgm):
    output = (ip - ip2)/sgm
    return 0.5*(1 + math.erf(output/(math.sqrt(2))))

print(round(norm(ip, ip2_sum, sgm_sum), 4))